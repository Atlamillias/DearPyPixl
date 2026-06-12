"""Contains various simple, standalone, custom item interface
types and functions.

High-level use of DearPyGui's functional API on items created by
these types is generally not supported — use the appropriate interface
instead.
"""
from dearpypixl.core import metautil
from dearpypixl.core import appitem
from dearpypixl.core.protocols import Descriptor, DataDescriptor
from dearpypixl.lib import items as _items
from dearpypixl import color as _colors
from dearpypixl import style as _styles

from dearpygui import _dearpygui

import typing
if typing.TYPE_CHECKING:
    from dearpypixl.core.protocols import Item, ItemChildCommand, Array




# [ functions ]

type _SelectorList = typing.Sequence[typing.Literal[0, 1] | bool]
type _CellFactory  = ItemChildCommand[_items.mvTableCell]

@typing.overload
def ribbon(columns: int, content_selectors: _SelectorList | None = ..., policy_selectors: _SelectorList | None = ..., /, *, cell_factory: _CellFactory = ..., spacer_factory: ItemChildCommand = ..., clipper: bool = ..., inner_width: int = ..., freeze_rows: int = ..., freeze_columns: int = ..., sort_multi: bool = ..., sort_tristate: bool = ..., resizable: bool = ..., reorderable: bool = ..., hideable: bool = ..., sortable: bool = ..., context_menu_in_body: bool = ..., row_background: bool = ..., borders_innerH: bool = ..., borders_outerH: bool = ..., borders_innerV: bool = ..., borders_outerV: bool = ..., no_host_extendX: bool = ..., no_host_extendY: bool = ..., no_keep_columns_visible: bool = ..., precise_widths: bool = ..., no_clip: bool = ..., pad_outerX: bool = ..., no_pad_outerX: bool = ..., no_pad_innerX: bool = ..., scrollX: bool = ..., scrollY: bool = ..., no_saved_settings: bool = ..., label: str | None = ..., use_internal_label: bool = ..., user_data: typing.Any | None = ..., tag: Item = ..., width: int = ..., height: int = ..., indent: int = ..., parent: Item = ..., before: Item = ..., source: Item = ..., callback: typing.Callable[..., typing.Any] | None = ..., show: bool = ..., filter_key: str = ..., pos: Array[int, typing.Literal[0] | typing.Literal[2]] = ..., **kwargs) -> tuple[_items.mvTableCell, ...]: ...  # pyrefly: ignore [invalid-overload]
@typing.overload
def ribbon(columns: int, content_selectors: _SelectorList | None = ..., policy_selectors: _SelectorList | None = ..., /, *, cell_factory: _CellFactory = ..., spacer_factory: ItemChildCommand = ..., **kwargs) -> tuple[_items.mvTableCell, ...]: ...
def ribbon(columns: int, content_selectors: _SelectorList | None = None, policy_selectors: _SelectorList | None = None, /, *, cell_factory: _CellFactory = _items.add_table_cell, spacer_factory: ItemChildCommand = _items.add_spacer, **kwargs) -> tuple[_items.mvTableCell, ...]:
    """A convenience function for creating simple, one-row layout
    tables containing a mix of "content" and "whitespace" columns.
    Content columns contain table cells while whitespace columns
    contain only spacers. Returns the list of cells created.

    Here's an example that creates a "justified" menu bar where
    the center remains vacant and stretchy:
    ```python
    import dearpypixl as dpx
    from dearpypixl.items import ribbon

    # DPG setup boilerplate
    ...

    def close_window(button, _, window, /):
        window.show = False

    with dpx.window() as window:
        l_cell, r_cell = ribbon(3, [1, 0, 1])

        with dpx.group(horizontal=True, parent=l_cell):
            dpx.add_button(label="File")
            dpx.add_button(label="Edit")
            dpx.add_button(label="View")
            dpx.add_button(label="Help")

        with r_cell:
            dpx.add_button(label="x", user_data=window, callback=close_window)

    dpx.start_dearpygui()
    ```

    :type columns: `int`
    :param columns: Number of total columns to create (min. 1).

    :type content_selectors: `Sequence[Literal[0, 1] | bool] | None` (optional)
    :param content_selectors: An ordered collection of booleans/integers
        indicating the role of each column (ordered by column index). The
        length of the sequence must be equal to *columns*. When `None`,
        this value is `[1] * columns`. Defaults to `None`.

        When a value is truthy, the column at that index is considered
        a "content" column and will contain a `mvTableCell` item. Columns
        that are not content columns will contain an a `mvSpacer` item
        instead. Additionally, the number of content columns indicates
        the number of  items returned by this function.

    :type policy_selectors: `Sequence[Literal[0, 1] | bool] | None` (optional)
    :param policy_selectors: An ordered collection of booleans/integers
        indicating the sizing policy of each column (ordered by column
        index). The length of the sequence must be equal to *columns*.
        Falls back to *content_selectors* when `None`. Defaults to `None`.

        When a value is truthy, the column at that index will use a
        "fixed" sizing policy. Otherwise, the column will use a "stretch"
        policy.

    :param **kwargs: Forwarded to `add_table()`. Note that the
        *policy* and *header_row* arguments will be ignored.

    :raises `ValueError`: *columns* is less than 1, or the length of
        *content_selectors* and/or *policy_selectors* does not match
        the number of columns.

    :rtype: `tuple[mvTableCell, ...]`
    :return: An ordered sequence of table cells created that should
        contain content.
    """
    if columns < 1:
        raise ValueError("must have at least 1 column")

    if content_selectors is None:
        content_selectors = [1] * columns
    elif columns != len(content_selectors):
        raise ValueError("number of values in `content_selectors` must be equal to `columns`")

    if policy_selectors is None:
        policy_selectors = content_selectors
    elif columns != len(policy_selectors):
        raise ValueError("number of values in `policy_selectors` must be equal to `columns`")

    kwargs["policy"]     = _dearpygui.mvTable_SizingFixedFit
    kwargs["header_row"] = False
    table = _items.table(**kwargs)

    t_row = table.add_table_row()
    items = []

    for cont_sel, policy_sel in zip(content_selectors, policy_selectors):
        if policy_sel:
            fixed   = True
            stretch = False
        else:
            fixed   = False
            stretch = True

        if cont_sel:
            table.add_table_column(width_fixed=fixed, width_stretch=stretch, no_clip=True)
            items.append(cell_factory(parent=t_row))
        else:
            table.add_table_column(width_fixed=fixed, width_stretch=stretch)
            spacer_factory(width=-1, parent=t_row)

    return (*items,)




# [ classes — primitive bases ]

# Most new types here don't inherit from an `mv*` base directly
# to allow each type finer control over which settings are
# exposed as some may become internal-only. However, we almost
# always use a child window or group as our "root" item and want
# to expose their states.

def _cast_method[O, **P, T](method: typing.Callable[typing.Concatenate[O, P], T], /) -> typing.Callable[P, T]:
    return method  # type: ignore

def _delegator_property[T](path, source, type: T) -> T:
    return metautil.create_compitem_prop_delegate(path, source)  # type: ignore

def _delegate_callback(self, callback, app_data = None, /):
    match metautil.get_positional_arity(callback):
        case 0: callback()
        case 1: callback(self)
        case 2: callback(self, app_data)
        case _: callback(self, app_data, self.user_data)


type _ItemPosition = DataDescriptor[list[int], Array[int, typing.Literal[0, 2]]]

class _mvGroupComposite(_items.ChildItem):
    __slots__ = ()

    pos: _ItemPosition = _items.mvGroup.pos  # type: ignore
    hovered: Descriptor[bool] = _items.mvGroup.hovered
    active: Descriptor[bool] = _items.mvGroup.active
    activated: Descriptor[bool] = _items.mvGroup.activated
    deactivated: Descriptor[bool] = _items.mvGroup.deactivated
    deactivated_after_edit: Descriptor[bool] = _items.mvGroup.deactivated_after_edit
    focused: Descriptor[bool] = _items.mvGroup.focused
    clicked: Descriptor[bool] = _items.mvGroup.clicked
    left_clicked: Descriptor[bool] = _items.mvGroup.left_clicked
    right_clicked: Descriptor[bool] = _items.mvGroup.right_clicked
    middle_clicked: Descriptor[bool] = _items.mvGroup.middle_clicked
    visible: Descriptor[bool] = _items.mvGroup.visible
    edited: Descriptor[bool] = _items.mvGroup.edited
    content_region_avail: Descriptor[bool] = _items.mvGroup.content_region_avail
    rect_size: Descriptor[Array[int, typing.Literal[2]]] = _items.mvGroup.rect_size
    resized: Descriptor[bool] = _items.mvGroup.resized
    rect_min: Descriptor[Array[int, typing.Literal[2]]] = _items.mvGroup.rect_min
    rect_max: Descriptor[Array[int, typing.Literal[2]]] = _items.mvGroup.rect_max

    create = _items.mvGroup.create   # type: ignore
    state = _cast_method(_items.mvGroup.state)   # type: ignore
    _delegate_callback = _delegate_callback

    def refresh(self, /) -> None: pass

class _mvChildWindowComposite(_items.ChildItem):
    __slots__ = ()

    pos: _ItemPosition = _items.mvChildWindow.pos  # type: ignore
    hovered: Descriptor[bool] = _items.mvChildWindow.hovered
    active: Descriptor[bool] = _items.mvChildWindow.active
    activated: Descriptor[bool] = _items.mvChildWindow.activated
    deactivated: Descriptor[bool] = _items.mvChildWindow.deactivated
    focused: Descriptor[bool] = _items.mvChildWindow.focused
    content_region_avail: Descriptor[Array[int, typing.Literal[2]]] = _items.mvChildWindow.content_region_avail
    rect_size: Descriptor[Array[int, typing.Literal[2]]] = _items.mvChildWindow.rect_size
    resized: Descriptor[bool] = _items.mvChildWindow.resized

    create = _items.mvChildWindow.create  # type: ignore
    state = _cast_method(_items.mvChildWindow.state) # type: ignore
    _delegate_callback = _delegate_callback

    def refresh(self, /) -> None: pass




# [ classes ]

class InputTextCombo(_mvGroupComposite):
    """Creates/manages a combo box with a text input in place of the
    preview field.

    The item value is set via dropdown menu selection or by pressing
    the ENTER/RETURN key when the text input is focused. Both update
    methods invoke the :py:attr:`on_edit_callback` callable (if set).

    Clicking the dropdown arrow button displays the items menu. The
    :py:attr:`on_activate_callback` callable is invoked (if set) *before*
    showing the menu. This gives users an opportunity to update
    :py:attr:`items` before they are displayed as options.

    This item's label is not rendered, unlike most inputs which have
    their labels rendered to the right of the input field.

    Structure
    ---------
    This item's primary components consist of:
    - 1 `mvGroup` i.e. `self`
    - 1 `mvInputText`, as `f"{self.tag}/input"`: Text input item.
    - 1 `mvButton`, as `f"{self.tag}/button"`: Drop-down button.
    - 1 `mvWindowAppItem`, as `f"{self.tag}/menu"`: Menu displayed when the
        drop-down button is clicked.
    - *n* `mvSelectable`: Drop-down menu items.

    References
    ----------
    - :py:meth:`init_button()`
    - :py:meth:`init_item()`
    """
    __slots__ = ()

    @property
    def value(self, /) -> str:
        return _dearpygui.get_item_configuration(f"{self.tag}/input")["hint"]
    @value.setter
    def value(self, value: str, /) -> None:
        item = f"{self.tag}/input"
        _dearpygui.set_value(item, '')
        _dearpygui.configure_item(item, hint=value)

    @property
    def items(self, /) -> tuple[typing.Any, ...]:
        return tuple(_dearpygui.get_item_configuration(f"{self.tag}/menu")["user_data"])
    @items.setter
    def items(self, value: typing.Sequence[typing.Any], /) -> None:
        items = []
        stage = _items.add_stage()
        try:
            group = _items.add_child_window(parent=stage, border=False, autosize_x=True, autosize_y=True)
            for v in value:
                s = str(v)
                self.init_item(s, parent=group)
                items.append(s)
        except:
            stage.destroy()
            raise
        else:
            menu = f"{self.tag}/menu"
            _dearpygui.configure_item(menu, user_data=items)
            _dearpygui.delete_item(menu, children_only=True, slot=1)
            stage.unstage(menu)

    @property
    def on_activate_callback(self, /):
        return _dearpygui.get_item_configuration(f"{self.tag}/button")["user_data"]
    @on_activate_callback.setter
    def on_activate_callback(self, value: typing.Callable | None, /) -> None:
        _dearpygui.configure_item(f"{self.tag}/button", user_data=value)
    @on_activate_callback.deleter
    def on_activate_callback(self, /) -> None:
        _dearpygui.configure_item(f"{self.tag}/button", user_data=None)

    @property
    def on_edit_callback(self, /):
        return _dearpygui.get_item_configuration(f"{self.tag}/input")["user_data"]
    @on_edit_callback.setter
    def on_edit_callback(self, value: typing.Callable | None, /) -> None:
        _dearpygui.configure_item(f"{self.tag}/input", user_data=value)
    @on_edit_callback.deleter
    def on_edit_callback(self, /) -> None:
        _dearpygui.configure_item(f"{self.tag}/input", user_data=None)

    _OTHER_CONFIG = frozenset(("items", "on_edit_callback", "on_activate_callback"))

    # mvInputText config
    no_spaces = _delegator_property("input", _items.mvInputText.no_spaces, DataDescriptor[bool])
    uppercase = _delegator_property("input", _items.mvInputText.uppercase, DataDescriptor[bool])
    tab_input = _delegator_property("input", _items.mvInputText.tab_input, DataDescriptor[bool])
    decimal = _delegator_property("input", _items.mvInputText.decimal, DataDescriptor[bool])
    hexadecimal = _delegator_property("input", _items.mvInputText.hexadecimal, DataDescriptor[bool])
    readonly = _delegator_property("input", _items.mvInputText.readonly, DataDescriptor[bool])
    password = _delegator_property("input", _items.mvInputText.password, DataDescriptor[bool])
    scientific = _delegator_property("input", _items.mvInputText.scientific, DataDescriptor[bool])
    auto_select_all = _delegator_property("input", _items.mvInputText.auto_select_all, DataDescriptor[bool])
    no_horizontal_scroll = _delegator_property("input", _items.mvInputText.no_horizontal_scroll, DataDescriptor[bool])
    always_overwrite = _delegator_property("input", _items.mvInputText.always_overwrite, DataDescriptor[bool])
    no_undo_redo = _delegator_property("input", _items.mvInputText.no_undo_redo, DataDescriptor[bool])
    escape_clears_all = _delegator_property("input", _items.mvInputText.escape_clears_all, DataDescriptor[bool])
    elide_left = _delegator_property("input", _items.mvInputText.elide_left, DataDescriptor[bool])

    _INPUT_CONFIG = frozenset((
        'no_spaces', 'uppercase', 'tab_input', 'decimal', 'hexadecimal', 'readonly',
        'password', 'scientific', 'auto_select_all', 'no_horizontal_scroll',
        'always_overwrite', 'no_undo_redo', 'escape_clears_all', 'elide_left'
    ))

    # mvGroup config
    width: DataDescriptor[int] = _items.mvGroup.width
    indent: DataDescriptor[int] = _items.mvGroup.indent
    show: DataDescriptor[bool] = _items.mvGroup.show
    filter_key: DataDescriptor[str] = _items.mvGroup.filter_key
    tracked: DataDescriptor[bool] = _items.mvGroup.tracked
    track_offset: DataDescriptor[float] = _items.mvGroup.track_offset
    enabled: DataDescriptor[bool] = _items.mvGroup.enabled

    _GROUP_CONFIG = frozenset((
        "label", "use_internal_label", "user_data", "width", "indent",
        "show", "filter_key", "tracked", "track_offset", "enabled",
    ))

    @classmethod
    def create(  # type: ignore
        cls,
        /,
        items: typing.Sequence[typing.Any] = (),
        default_value: str = '',
        *,
        on_edit_callback = None,
        on_activate_callback = None,
        # mvGroup kwargs
        label: str | None = None,
        use_internal_label: bool = True,
        user_data: typing.Any | None = None,
        tag: Item = 0,
        width: int = 0,
        indent: int = -1,
        parent: Item = 0,
        before: Item = 0,
        show: bool = True,
        filter_key: str = "",
        tracked: bool = False,
        track_offset: float = 0.5,
        enabled: bool = True,
        pos: Array[int, typing.Literal[0, 2]] = (),
        # mvInputText kwargs
        no_spaces: bool = False,
        uppercase: bool = False,
        tab_input: bool = False,
        decimal: bool = False,
        hexadecimal: bool = False,
        readonly: bool = False,
        password: bool = False,
        scientific: bool = False,
        auto_select_all: bool = False,
        no_horizontal_scroll: bool = False,
        always_overwrite: bool = False,
        no_undo_redo: bool = False,
        escape_clears_all: bool = False,
        elide_left: bool = False,
        **kwargs
    ):
        self = cls(_items.add_group(
            label=label, use_internal_label=use_internal_label, user_data=user_data,
            tag=tag, width=width, indent=indent, parent=parent, before=before, show=show,
            filter_key=filter_key, tracked=tracked, track_offset=track_offset,
            enabled=enabled, pos=pos,
        ))

        path = self.tag

        with _items.table(
            tag=f"{path}/_ribbon", parent=self, header_row=False, precise_widths=True, no_pad_innerX=True,
            no_pad_outerX=True, policy=_dearpygui.mvTable_SizingFixedFit, pos=(0, 0)
        ) as table:

            with table.add_table_row():

                table.add_table_column(width_stretch=True)
                _items.add_input_text(
                    tag=f"{path}/input", width=-1, on_enter=True, callback=self.on_edit,
                    no_spaces=no_spaces, uppercase=uppercase, tab_input=tab_input, decimal=decimal,
                    hexadecimal=hexadecimal, readonly=readonly, password=password, scientific=scientific,
                    auto_select_all=auto_select_all, no_horizontal_scroll=no_horizontal_scroll,
                    always_overwrite=always_overwrite, no_undo_redo=no_undo_redo,
                    escape_clears_all=escape_clears_all, elide_left=elide_left,
                )

                table.add_table_column()
                self.init_button(tag=f"{path}/button", callback=self.on_activate)

        _items.add_window(tag=f"{path}/menu", popup=True, visible=False, user_data=())

        self.on_activate_callback = on_activate_callback
        self.on_edit_callback     = on_edit_callback
        self.items                = items
        self.value                = default_value

        return self

    def destroy(self, /) -> None:
        try:
            _dearpygui.delete_item(f"{self.tag}/menu", children_only=False, slot=-1)
        except SystemError:
            pass
        super().destroy()

    def configure(self, **kwargs):
        GROUP_CONFIG = self.__class__._GROUP_CONFIG
        INPUT_CONFIG = self.__class__._INPUT_CONFIG
        OTHER_CONFIG = self.__class__._OTHER_CONFIG

        group_config = {}
        input_config = {}

        pos = kwargs.pop("pos", None)
        if pos is not None:
            group_config['pos'] = pos

        for k,v in kwargs.items():
            if k in GROUP_CONFIG:
                group_config[k] = v
            elif k in INPUT_CONFIG:
                input_config[k] = v
            elif k in OTHER_CONFIG:
                setattr(self, k, v)

        _dearpygui.configure_item(self, **group_config)
        _dearpygui.configure_item(f"{self.tag}/input", **input_config)

    def configuration(self, /) -> dict[str, typing.Any]:
        group_config = _dearpygui.get_item_configuration(self)
        input_config = _dearpygui.get_item_configuration(f"{self.tag}/input")

        config = {}

        for option in self.__class__._GROUP_CONFIG:
            config[option] = group_config[option]
        for option in self.__class__._INPUT_CONFIG:
            config[option] = input_config[option]
        for option in self.__class__._OTHER_CONFIG:
            config[option] = getattr(self, option)

        return config

    def show_menu(self, /):
        state = self.state()
        width = state["rect_size"][0]
        pos   = state["rect_min"][0], state["rect_max"][1]
        _dearpygui.configure_item(f"{self.tag}/menu", show=True, pos=pos, min_size=(width, 100), width=width)

    def hide_menu(self, /):
        _dearpygui.configure_item(f"{self.tag}/menu", show=False)

    def init_button(self, /, *, parent: Item = 0, tag: Item = 0, callback = None) -> Item:
        """Returns an item that will be used to display the item menu when
        clicked. Called one time only when the combo box is created. May be
        overridden to return a different type of item (default is `mvButton`).

        *callback* is provided by the constructor. If the item supports the
        `callback` setting, then this should simply be forwarded to the item
        factory as the *callback* keyword or similar argument. Alternatively,
        the callback can be fired via an "on click" or "on activation" event
        handler.

        The item's `user_data` setting is managed by the caller and should not
        be set.

        Setting the item's size to a delta (e.g. `width=-1`) may cause it to be
        pushed it into the clipping region when rendered.
        """
        return _items.add_button(
            tag=tag, parent=parent, callback=callback, arrow=True, direction=_dearpygui.mvDir_Down
        )

    def _on_item_select(self, sender, state, value, /):
        _dearpygui.set_value(sender, False)
        self.on_edit(sender, value, self.on_edit_callback)
        # BUG: pretty sure popups should hide automatically, but clicking a
        # selectable doesn't seem to do so
        self.hide_menu()

    def init_item(self, value: str, /, *, parent: Item = 0, tag: Item = 0) -> Item:
        """Creates an item representing a single value within :py:attr:`items`.
        Called when :py:attr:`items` is updated.

        *value* is the string representation of an object in :py:attr:`items`.
        The item is expected to render this as its `label` or similar.

        Clicking or activating the item should update the combo box value and
        hide the dropdown menu. This is facilitated by the implementation of
        :py:meth:`add_item()` and not the caller (unlike :py:meth:`add_button()`,
        where the caller provides the callback).
        """
        return _items.add_selectable(
            label=value, parent=parent, tag=tag, width=1000,
            callback=self._on_item_select, user_data=value,
        )

    def on_activate(self, sender, value, callback, /):
        """DearPyGui callback that runs :py:attr:`on_activate_callback`, then
        displays the dropdown menu."""
        # run the callback first to give it a chance to update our items list
        if callback is not None:
            self._delegate_callback(callback, value)

        self.show_menu()

    def on_edit(self, sender, value, callback, /):
        """DearPyGui callback that updates the item's current value, then
        runs :py:attr:`on_edit_callback`."""
        self.value = value

        if callback is not None:
            self._delegate_callback(callback, value)

add_input_text_combo = InputTextCombo.create


class ItemSelector(appitem.CompositeItem, _items.mvCombo):
    """Creates/manages a combo box for selecting existing DearPyGui items.
    Available selections/values are limited to those included in the array
    returned from calling the :py:attr:`itemgetter` callable. The
    :py:attr:`formatter` callable determines the display label of each item
    shown in the combo's dropdown menu.

    The combo box is implicitly refreshed through various API interactions.
    For example, most interactions will null the current value if it is no longer
    an existing item. Others such as clicking the dropdown button also update the
    list of available selections with the latest results using :py:attr:`itemgetter`
    and :py:attr:`formatter`. Regardless, the item can be explicitly refreshed by
    calling the :py:meth:`refresh()` method.

    By default, the combo box is bound to a global item handler registry that
    parents a single on-click handler -- this provides a "refresh" opportunity
    when the dropdown button is clicked but before the menu is rendered. If
    :py:attr:`handlers` is set to another handler registry, it will become the
    parent of a new on-click handler that refreshes the combo box when any item
    bound to that registry is clicked. Note that any handler created this way is
    automatically destroyed when updating :py:attr:`handlers` or when the
    :py:meth:`destroy()` method is called. Setting :py:attr:`handlers` to null
    automatically re-binds the default global item handler registry.

    Notes
    -----
    - :py:attr:`value` does not return the string value displayed in the
        preview, but the item it represents
    - :py:attr:`itemgetter` determines the items to display, while
        :py:attr:`formatter` determines *how* to display them
    - updates to :py:attr:`value` are limited to the items returned by
        the :py:attr:`itemgetter` callable (including programatic updates)
    - setting :py:attr:`value` to any null value is equivelent to `None`
    - an "empty" selection is always available via UI -- selecting it
        sets :py:attr:`value` to `None`
    - when the combo box is refreshed, :py:attr:`value` is implicitly set to
        `None` when the current non-null value does not represent an existing
        item e.g. the item was deleted, etc.
    - :py:attr:`callback` is invoked on *any* update to :py:attr:`value`,
        implicit or otherwise
    - selections are *not* static -- :py:attr:`itemgetter` is called
        periodically to update available selections/values
    - :py:attr:`handlers` is never `None`
    - :py:attr:`items` is read-only and returns the result of
        :py:attr:`self.itemgetter()`

    :vartype itemgetter: `Callable[[], Sequence[int | str]]
    :var itemgetter: A callable that returns a sequence of existing item
        identifiers or aliases to make available for selection. Defaults
        to `dearpygui.get_all_items()`.

    :vartype formatter: `Callable[[int | str], str]
    :var formatter: Called for every item returned by :py:attr:`itemgetter`,
        returning the string representation e.g. "label" to render for each.
        Defaults to `repr()`.
    """

    itemgetter:  typing.Callable[[], list[Item]] = staticmethod(_dearpygui.get_all_items)  # type: ignore
    formatter: typing.Callable[[Item], str] = staticmethod(repr)

    @classmethod
    def create(  # type: ignore
        cls,
        /,
        itemgetter:  typing.Callable[[], list[Item]] | None = None,
        formatter: typing.Callable[[Item], str] | None = None,
        *,
        label: str | None = None,
        use_internal_label: bool = True,
        user_data: typing.Any | None = None,
        tag: Item = 0,
        width: int = 0,
        indent: int = -1,
        parent: Item = 0,
        before: Item = 0,
        callback: typing.Callable | None = None,
        popup_align_left: bool = False,
        no_arrow_button: bool = False,
        no_preview: bool = False,
        fit_width: bool = False,
        height_mode: int = 1,
        source: Item = 0,
        show: bool = True,
        enabled: bool = True,
        filter_key: str = "",
        drop_callback: typing.Callable | None = None,
        drag_callback: typing.Callable | None = None,
        payload_type: str = "$$DPG_PAYLOAD",
        tracked: bool = False,
        track_offset: float = 0.5,
        pos: Array[int, typing.Literal[0, 2]] = (),
        default_value: int | str | None = None,
        **kwargs
    ):
        self = super().create(
            label=label, use_internal_label=use_internal_label, user_data=user_data, tag=tag,
            width=width,  indent=indent,  parent=parent,  before=before,
            popup_align_left=popup_align_left, no_arrow_button=no_arrow_button, no_preview=no_preview,
            fit_width=fit_width, height_mode=height_mode, source=source, show=show, enabled=enabled,
            filter_key=filter_key, drop_callback=drop_callback, drag_callback=drag_callback,
            payload_type=payload_type, tracked=tracked, track_offset=track_offset, pos=pos,
        )
        _dearpygui.configure_item(self, callback=self.on_edit)

        if itemgetter is not None:
            self.itemgetter = itemgetter
        if formatter is not None:
            self.formatter = formatter

        self.callback = callback
        self.handlers = self._get_handler_registry()

        if default_value:
            self.value = default_value

        return self

    def destroy(self, /) -> None:
        try   : _dearpygui.delete_item(f"{self.tag}/handler")
        except: pass
        super().destroy()

    def configure(self, *args, **kwargs) -> None:
        if "callback" in kwargs:
            self.callback = kwargs.pop('callback')
        kwargs.pop("items", None)
        super().configure(**kwargs)

    def configuration(self, /):
        config = super().configuration()
        config["callback"] = self.callback
        config["items"]    = self.items
        return config

    # `reprlist` and `itemlist` -- coupling them makes updates atomic(-enough)
    _caches: tuple[typing.Sequence[str], typing.Sequence[Item]] = (('',), (0,))

    def _refresh_value(self, caches: tuple[typing.Sequence[str], typing.Sequence[Item]] | None = None, /):
        if caches is None:
            caches = self._caches
        reprlist, itemlist = caches

        v_repr = _dearpygui.get_value(self)
        v_item = itemlist[reprlist.index(v_repr)]

        formatter = self.formatter

        if v_item:
            if not _dearpygui.does_item_exist(v_item):
                v_item = 0
                v_repr = ''
                _dearpygui.set_value(self, '')

                callback = self.callback
                if callback is not None:
                    _delegate_callback(self, callback, None)
            elif v_repr != (s := formatter(v_item)):
                _dearpygui.set_value(self, s)
                v_repr = s

        return (v_repr, v_item)

    def _refresh_caches(self, /):
        formatter = self.formatter

        itemlist = self.itemgetter()
        reprlist = [formatter(item) for item in itemlist]
        itemlist.insert(0, 0)
        reprlist.insert(0, '')

        caches = self._caches = (reprlist, itemlist)
        _dearpygui.configure_item(self, items=reprlist)

        return caches

    def refresh(self, /) -> None:
        self._refresh_value()
        self._refresh_caches()

    @property
    def items(self, /) -> typing.Sequence[Item]:  # pyrefly: ignore [bad-override]
        return self.itemgetter()

    # we use the `callback` setting in our implementation, so store the
    # user-level callback in the instance dictionary
    @property
    def callback(self, /) -> typing.Callable | None:
        return self.__dict__["callback"]
    @callback.setter
    def callback(self, value: typing.Callable | None, /) -> None:
        self.__dict__["callback"] = value
    @callback.deleter
    def callback(self, /) -> None:
        self.__dict__["callback"] = None

    @property
    def value(self, /) -> Item | None:
        return self._refresh_value()[1] or None
    @value.setter
    def value(self, value: str | Item | None, /) -> None:
        callback = self.callback

        if not value:
            _dearpygui.set_value(self, '')

            if callback is not None:
                _delegate_callback(self, callback, None)

            return

        reprlist, itemlist = self._refresh_caches()
        if value in reprlist:
            value = itemlist[reprlist.index(value)]  # pyrefly: ignore
        if value not in itemlist:
            if _dearpygui.does_item_exist(value or 0):
                raise ValueError(f"cannot select {value!r} item -- excluded from itemgetter result")
            if value is None or isinstance(value, (str, int)):
                raise ValueError(f"{value!r} is not an item")
            raise TypeError(f"expected an existing item's identifier or string representation, got {value!r}")

        _dearpygui.set_value(self, self.formatter(value))

        if callback is not None:
            _delegate_callback(self, callback, value)
    @value.deleter
    def value(self, /) -> None:
        _dearpygui.set_value(self, '')

    # we need an additional event to fire when the dropdown button is clicked
    # but before showing the menu -- `handlers` should never be `None`
    @property
    def handlers(self, /) -> _items.mvItemHandlerRegistry:
        item = _dearpygui.get_item_info(self)["handlers"]; assert item is not None
        return _items.mvItemHandlerRegistry(item)
    @handlers.setter
    def handlers(self, value: Item | None, /, *, __func=_dearpygui.get_item_info) -> None:
        # exists when `self.handlers != self._get_handler_registry()`
        handler = f"{self.tag}/handler"
        if _dearpygui.does_item_exist(handler):
            try   : _dearpygui.delete_item(handler)
            except: pass

        default_handlers = __class__._get_handler_registry()
        if value and value != default_handlers:
            _items.add_item_clicked_handler(tag=handler, parent=value, callback=self.on_click)
        else:
            value = default_handlers
        _dearpygui.bind_item_handler_registry(self, value)
    @handlers.deleter
    def handlers(self, /) -> None:
        self.handlers = None

    @staticmethod
    def _get_handler_registry():
        alias = "ItemSelector::handlers"

        if _dearpygui.does_item_exist(alias):
            return _items.mvItemHandlerRegistry(alias)

        handlers = _items.item_handler_registry(tag=alias)
        _items.add_item_clicked_handler(parent=handlers, callback=__class__._on_click)

        return handlers

    @staticmethod
    def _on_click(handler: Item, app_data: tuple[int, Item], /) -> None:
        __class__(app_data[1]).on_click(handler, app_data)

    def on_click(self, handler: Item, app_data: tuple[int, Item], /) -> None:
        self.refresh()

    def on_edit(self, sender: Item, value: str, /):
        values = self._refresh_value()

        callback = self.__dict__["callback"]
        if callback is not None:
            _delegate_callback(self, callback, values[1])

add_item_selector = ItemSelector.create



class SplitLabelButton(_mvChildWindowComposite):
    """Creates/manages a button that renders a two-part text value within it,
    justified left and right respectively.

    Split label buttons are similar to `mvButton` items except it's `value` is
    rendered (not `label`) and the text is not center-aligned. The user can
    access/manage the value as a single string via the :py:attr:`value` property
    (where parts are delimited using `"##"`) or individually via :py:attr:`l_text`
    and :py:attr:`r_text`. They are particularly useful as menu items that
    have associated hotkeys.

    Structure
    ---------
    This item's primary components consist of:
    - 1 `mvChildWindow` i.e. `self`
    - 1 `mvButton`, as `f"{self.tag}/hitbox"`: The item's clickable element.
    - 2 `mvTableCell`, as `f"{self.tag}/"`l_cell"`, `f"{self.tag}/"`r_cell"`
        Parents the items displaying `self.value`.
    - 2 `mvText`, as `f"{self.tag}/"`l_item"`, `f"{self.tag}/"`r_item"`:
        The left/right items displaying `self.value`.

    References
    ----------
    - :py:meth:`init_ribbon()`
    - :py:meth:`init_l_item()`
    - :py:meth:`init_r_item()`

    """
    __slots__ = ()

    @property
    def value(self, /) -> str:
        """[***get**, **set**, **del***] both left and right text values
        as a single string where `"##"` is used as a delimiter.

        On access, the delimiter will only be included when the right text
        value is not empty. If the delimiter is at the start of the string,
        the left text value is empty. An empty string indicates both values
        are empty.

        On set, the right text value will be cleared if the new value is
        missing the delimiter. If the new value starts with the delimiter,
        the left text value is cleared. An empty string clears both values.
        """
        l_text = self.l_text
        r_text = self.r_text
        if r_text:
            return f"{l_text}##{r_text}"
        return l_text
    @value.setter
    def value(self, value: str | None, /) -> None:
        if not value:
            self.l_text = self.r_text = ''
            return
        l_text, _, r_text = value.partition("##")
        self.l_text = l_text
        self.r_text = r_text
    @value.deleter
    def value(self, /) -> None:
        self.l_text = self.r_text = ''

    @property
    def l_text(self, /) -> str:
        """[***get**, **set**, **del***] the left-aligned text value.

        :py:attr:`l_text` and :py:attr:`r_text` manage the underlying item's
        stored value *and* `label` setting by default. Override them as needed
        to adjust this behavior.
        """
        path = f"{self.tag}/l_item"
        return _dearpygui.get_value(path) or _dearpygui.get_item_configuration(path)["label"] or ''
    @l_text.setter
    def l_text(self, value: str, /) -> None:
        path = f"{self.tag}/l_item"
        _dearpygui.set_value(path, value)
        _dearpygui.configure_item(path, label=value)
    @l_text.deleter
    def l_text(self, /) -> None:
        self.l_text = ''

    @property
    def r_text(self, /) -> str:
        """[***get**, **set**, **del***] the right-aligned text value.

        :py:attr:`l_text` and :py:attr:`r_text` manage the underlying item's
        stored value *and* `label` setting by default. Override them as needed
        to adjust this behavior.
        """
        path = f"{self.tag}/r_item"
        return _dearpygui.get_value(path) or _dearpygui.get_item_configuration(path)["label"] or ''
    @r_text.setter
    def r_text(self, value: str, /) -> None:
        path = f"{self.tag}/r_item"
        _dearpygui.set_value(path, value)
        _dearpygui.configure_item(path, label=value)
    @r_text.deleter
    def r_text(self, /) -> None:
        self.r_text = ''

    callback: DataDescriptor[typing.Callable | None] = metautil.create_compitem_prop_delegate('hitbox', _items.mvButton.user_data)  # type: ignore
    enabled: DataDescriptor[bool] = metautil.create_compitem_prop_delegate('hitbox', _items.mvButton.enabled)  # type: ignore

    autosize_x = _items.mvChildWindow.autosize_x
    flattened_navigation = _items.mvChildWindow.flattened_navigation
    auto_resize_x = _items.mvChildWindow.auto_resize_x
    width = _items.mvChildWindow.width
    indent = _items.mvChildWindow.indent
    show = _items.mvChildWindow.show
    filter_key = _items.mvChildWindow.filter_key
    drop_callback = _items.mvChildWindow.drop_callback
    payload_type = _items.mvChildWindow.payload_type
    tracked = _items.mvChildWindow.tracked
    track_offset = _items.mvChildWindow.track_offset

    @typing.overload
    @classmethod
    def create(cls, /, *, autosize_x: bool = ..., flattened_navigation: bool = ..., always_use_window_padding: bool = ..., resizable_x: bool = ..., resizable_y: bool = ..., always_auto_resize: bool = ..., auto_resize_x: bool = ..., label: str | None = ..., use_internal_label: bool = ..., user_data: typing.Any = ..., tag: Item = ..., width: int = ..., height: int = ..., indent: int = ..., parent: Item = ..., before: Item = ..., show: bool = ..., filter_key: str = ..., drop_callback: typing.Callable | None = ..., payload_type: str = ..., tracked: bool = ..., track_offset: float = ..., pos: Array[int, typing.Literal[0, 2]] = ...) -> typing.Self: ...  # type: ignore
    @typing.overload
    @classmethod
    def create(cls, default_value: str = '', /, callback: typing.Callable | None = None, *, enabled: bool = ..., **kwargs) -> typing.Self: ...
    @classmethod
    def create(cls, default_value: str = '', /, callback: typing.Callable | None = None, *, enabled: bool = True, **kwargs):
        kwargs["auto_resize_y"]        = True
        kwargs["no_scrollbar"]         = True
        kwargs["no_scroll_with_mouse"] = True
        kwargs["border"]               = False
        kwargs["frame_style"]          = False
        self = cls(tag=_items.add_child_window(**kwargs))

        path = f"{self.tag}"

        _items.add_button(
            tag=f"{path}/hitbox", parent=self,
            enabled=enabled, width=-1, pos=(0, 0), callback=self.on_activate,
        )

        l_cell, r_cell = self.init_ribbon(parent=self)
        self.init_l_item(parent=l_cell, tag=f"{path}/l_item")
        self.init_r_item(parent=r_cell, tag=f"{path}/r_item")

        self.value = default_value
        self.callback = callback

        return self

    def configure(self, **kwargs) -> None:
        if "enabled" in kwargs:
            self.enabled = kwargs.pop("enabled")
        if "callback" in kwargs:
            self.callback = kwargs.pop("callback")
        _dearpygui.configure_item(self, **kwargs)

    def configuration(self, /) -> dict[str, typing.Any]:
        config = _dearpygui.get_item_configuration(self)
        config["enabled"] = self.enabled
        config["callback"] = self.callback
        return config

    @property
    def rect_min(self, /) -> list[int]:
        return _dearpygui.get_item_state(f"{self.tag}/hitbox")['rect_min']

    @property
    def rect_max(self, /) -> list[int]:
        return _dearpygui.get_item_state(f"{self.tag}/hitbox")['rect_max']

    def state(self, /):
        state = _dearpygui.get_item_state(f"{self.tag}/hitbox")
        state.update(_dearpygui.get_item_state(self))
        return state

    @staticmethod
    def _get_ribbon_theme() -> _items.mvTheme:
        alias = "LabelButton::cell_theme"
        if _dearpygui.does_item_exist(alias):
            return _items.mvTheme(alias)

        theme = _items.add_theme(tag=alias)
        with theme.add_theme_component():
            _colors.button((0, 0, 0, 0), tag=f"{alias}/button")
            _colors.button_hovered((0, 0, 0, 0), tag=f"{alias}/button_hovered")
            _colors.button_active((0, 0, 0, 0), tag=f"{alias}/button_active")
            _styles.cell_padding((-1, 0), tag=f"{alias}/cell_padding")

        return theme

    def init_ribbon(self, /, parent: Item = 0) -> tuple[_items.ContainerItem, _items.ContainerItem]:
        """Creates the inner layout item(s) that will parent the split label
        button's left and right value items. Called one time only while creating
        the split label button.

        This method creates a `mvTable` item and returns two `mvTableCell` items
        by default, but may be overridden to create a different child item(s).
        The returned items must be containers that can parent items returned by
        :py:meth:`init_l_item()` and :py:meth:`init_r_item()` respectively.

        The items returned by the default implementation are assigned aliases
        equivelent to `f"{self.tag}/l_cell"` and `f"{self.tag}/r_cell"`. These
        are for user convenience and are not used internally.
        """
        path = f"{self.tag}"

        # BUG: `ribbon()` is not used because `does_item_exist()` fails w/aliases
        # if the alias is assigned after the item's creation
        # XXX: similar to `ribbon(5, (0, 1, 0, 1, 0), (1, 1, 0, 1, 1), **kwargs)`
        with _items.table(parent=parent, width=-1, no_pad_innerY=True, precise_widths=True) as table:
            row = _items.add_table_row(parent=table)

            _items.add_table_column(width_fixed=True, no_clip=True)
            _items.add_spacer(parent=row)

            _items.add_table_column(width_fixed=True)
            l_cell = _items.add_table_cell(tag=f"{path}/l_cell", parent=row)

            _items.add_table_column(width_stretch=True)
            _items.add_button(parent=row)

            _items.add_table_column(width_fixed=True, no_clip=True)
            r_cell = _items.add_table_cell(tag=f"{path}/r_cell", parent=row)

            _items.add_table_column(width_fixed=True)
            _items.add_spacer(parent=row)

        table.theme = self._get_ribbon_theme()

        return (l_cell, r_cell)

    def init_l_item(self, /, parent: Item = 0, tag: Item = 0) -> Item:
        """Creates the "left" value item. Called one time only while creating
        the split label button.

        This method creates a `mvText` item by default, but may be overridden
        to create a different child item. The item created must have geometry
        and, ideally, displays its stored value or `label` setting when
        rendered.

        Note that the default :py:attr:`l_text` and :py:attr:`r_text` properties
        manage the item's value *and* label.
        """
        return _items.add_text(parent=parent, tag=tag)

    def init_r_item(self, /, parent: Item = 0, tag: Item = 0) -> Item:
        """Creates the "right" value item. Called one time only while creating
        the split label button.

        This method creates a `mvText` item by default, but may be overridden
        to create a different child item. The item created must have geometry
        and, ideally, displays its stored value or `label` setting when
        rendered.

        Note that the default :py:attr:`l_text` and :py:attr:`r_text` properties
        manage the item's value *and* label.
        """
        return _items.add_text(parent=parent, tag=tag)

    def on_activate(self, sender, value, user_data, /) -> None:
        if (callback := self.callback) is not None:
            self._delegate_callback(callback, value)

add_split_label_button = SplitLabelButton.create
