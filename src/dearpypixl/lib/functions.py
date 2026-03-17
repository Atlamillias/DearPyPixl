import typing as _typing

from dearpygui import  _dearpygui

from dearpypixl.core import appitem as _appitem

if _typing.TYPE_CHECKING:
    from dearpypixl.lib.items import mvWindowAppItem
    from dearpypixl.core.protocols import Array
    from dearpypixl.core.protocols import Item
    from dearpypixl.core.protocols import ItemCallback1
    from dearpypixl.core.protocols import ItemCallback2
    from dearpypixl.core.protocols import ItemCallback3




_globals = set(globals())
_globals.discard("_globals")


# [ homebrew ]

def get_interface_type(item: Item, /) -> type[_appitem.ChildItem | _appitem.ContainerItem]:
    type_name = _dearpygui.get_item_info(item)["type"]
    return _appitem.AppItem.__item_registry__[type_name]  # ty:ignore[invalid-return-type]


@_typing.overload
def get_root_parent(item: int | str, /) -> tuple[str, int | str | None]: ...  # pyright: ignore[reportInconsistentOverload]  # ty:ignore[invalid-overload]
def get_root_parent(item, /, *, __func=_dearpygui.get_item_info):
    """Get the type name and identifier of *item*'s top-level
    parent. If *item* is a top-level container, return its type
    name and identifier instead.

    :type item: `int | str`
    :param item: Item to query.

    :rtype: `tuple[str, int | str | None]`
    :returns: The type name and tag of the top-level container as a 2-tuple.

    :raises `SystemError`: DearPyGui-related error.
    """
    item_uuid = item
    type_name = ''

    while True:
        info =__func(item_uuid)

        parent = info["parent"]
        if parent is None:
            break

        item_uuid = parent
        type_name = info["type"]

    if item_uuid == item:
        return info["type"], item

    return type_name, item_uuid


@_typing.overload
def iter_item_parents(item: int | str, /) -> _typing.Iterator[tuple[str, int | str]]: ...  # pyright: ignore[reportInconsistentOverload]  # ty:ignore[invalid-overload]
def iter_item_parents(item: int | str, /, *, __func=_dearpygui.get_item_info) -> _typing.Iterator[tuple[str, int | str]]:
    """Return an iterator that yields the direct parent of the most
    recent item it outputs, starting from *item*. The iterator is
    exhausted once it yields the top-level parent of *item*. If *item*
    is a top-level container, the iterator will be empty.

    :type item: `int | str`
    :param item: Initial item. The first item yielded by the iterator
        will be this item's parent (if any).

    :rtype: `Iterator[tuple[str, int | str]]`
    :return: The type name and identifier of parent item(s) as a 2-tuple.
    """
    item_uuid = item

    while True:
        info =__func(item_uuid)

        parent = info["parent"]
        if parent is None:
            break

        item_uuid = parent
        type_name = info["type"]

        yield (type_name, item_uuid)


def get_item_index(item: int | str, /) -> int:
    """Return the position of *item* in its parent's child slot.

    :type item: `int | str`
    :param item: Child item identifier.

    :rtype: `int`
    :return: Position of *item* in the slot as a zero-index.

    :raises `ValueError`: *item* is not a child item
    :raises `SystemError`: DearPyGui-related error.
    """
    if isinstance(item, str):
        tag = _dearpygui.get_alias_id(item)
    else:
        tag = item

    item_info = _dearpygui.get_item_info(tag)

    parent = item_info["parent"]
    if not parent:
        raise ValueError(f"item {item!r} is not a child item")

    slot_index = item_info["target"]
    child_slot = _dearpygui.get_item_info(parent)["children"][slot_index]

    return child_slot.index(tag)


def insert_item(index: _typing.SupportsIndex, item: int | str, /, *, parent: int | str = 0) -> None:
    """Move *item* to a different position and optionally to a
    different container.

    Similar to `dearpygui.move_item(item, before=other_item)`, but
    the item's new position is referenced via index instead of a specific
    item (e.g. *before*).

    where *other_item* is obtained calculating *before* using
    :type index: `_typing.SupportsIndex`
    :param index: _description_

    :type item: `int | str`
    :param item: Child item to move.

    :type parent: `int | str` (optional)
    :param parent: New parent for *item*. Defaults to `0`.

    :raises `ValueError`: *item* is not a child item
    :raises `SystemError`: DearPyGui-related error.
    """
    item_info = _dearpygui.get_item_info(item)

    old_parent = item_info["parent"]
    if not old_parent:
        raise ValueError(f"item {item!r} is not a child item")

    slot_index = item_info["target"]
    child_slot = _dearpygui.get_item_info(parent or old_parent)["children"][slot_index]

    _dearpygui.move_item(item, parent=parent, before=child_slot[index])


type _AcceptsSender[T: Item, T2, T3] = ItemCallback1[T] | ItemCallback2[T, T2] | ItemCallback3[T, T2, T3]

@_typing.overload
def cast_sender_as[T: Item, T2 = _typing.Any, T3 = _typing.Any]() -> _typing.Callable[[_AcceptsSender[_appitem.AppItem, T2, T3]], _AcceptsSender[Item, T2, T3]]: ...
@_typing.overload
def cast_sender_as[T: _appitem.AppItem, T2 = _typing.Any, T3 = _typing.Any](item_type: type[T], /) -> _typing.Callable[[_AcceptsSender[T, T2, T3]], _AcceptsSender[Item, T2, T3]]: ...
@_typing.overload
def cast_sender_as[T: _appitem.AppItem, T2 = _typing.Any, T3 = _typing.Any](item_type: type[T], callback: _AcceptsSender[T, T2, T3], /) -> _AcceptsSender[Item, T2, T3]: ...
def cast_sender_as(item_type = _appitem.AppItem, callback = None, /):
    """A wrapper for Dear PyGui callbacks that accept at least one
    positional argument. Instead of an item identifier as the first
    positional argument (e.g. *sender*), the callback will receive an
    interface for that item instead.

    :type item_type: `type[AppItem]` (optional)
    :param item_type: The interface class to use. Defaults to `AppItem`.

    :type callback: `Callable` (optional)
    :param callback: A function that will be used as a Dear PyGui callback
        that accepts at least one positional argument. Defaults to `None`.
    """
    import functools

    def wrap_callback(callback, /):

        @functools.wraps(callback)
        def wrapped(sender, *args, __callback=callback, __item_type=item_type):
            return __callback(__item_type(tag=sender), *args)

        return wrapped

    if callback is None:
        return wrap_callback

    return wrap_callback(callback)




# [ re-implementations ]

class Mutex:
    """An alternative implementation and drop-in replacement for
    `dearpygui.mutex()`. It carries slightly less overhead compared to the
    former, in addition to implementing the :py:meth:`acquire()` and
    :py:meth:`release()` methods similar to other Python lock objects.
    """
    __slots__ = ()

    # allows a single object to act as a drop-in replacement for `with dearpygui.mutex(): ...`
    # instead of creating a new object every call
    def __call__(self, /) -> None:
        pass

    acquire = staticmethod(_dearpygui.lock_mutex)
    release = staticmethod(_dearpygui.unlock_mutex)

    __enter__ = acquire

    def __exit__(self, exc_type=None, error=None, traceback=None, /) -> None:
        self.release()  # type: ignore

mutex = Mutex()
_globals.add("Mutex")  # don't export on `from __name__ import *`


def popup(parent: int | str, mousebutton: int = _dearpygui.mvMouseButton_Right, modal: bool = False, tag: int | str = 0, min_size: Array[int, _typing.Literal[2]] = (100, 100), max_size: Array[int, _typing.Literal[2]] = (30000, 30000), no_move: bool = False, no_background: bool = False) -> mvWindowAppItem:
    mvWindowAppItem = _appitem.AppItem.__item_registry__[_dearpygui.mvWindowAppItem]
    window = mvWindowAppItem.create(
        popup = True if not modal else False,
        modal=modal,
        show=False,
        tag=tag,
        autosize=True,
        min_size=min_size,
        max_size=max_size,
        no_move=no_move,
        no_background=no_background
    )

    try:
        handler_registry = _dearpygui.add_item_handler_registry(label=None, user_data=None, use_internal_label=True, tag=0, show=True)  # ty:ignore[invalid-argument-type]
        _dearpygui.add_item_clicked_handler(mousebutton, parent=handler_registry, callback=lambda: window.configure(show=True))
        _dearpygui.bind_item_handler_registry(parent, handler_registry)
    except:
        try: _dearpygui.delete_item(handler_registry)
        except: pass

        try: _dearpygui.delete_item(window)
        except: pass

        raise

    return window  # ty:ignore[invalid-return-type]




# [ direct imports ]

from dearpygui.dearpygui import (
    run_callbacks as run_callbacks,
    get_major_version as get_major_version,
    get_minor_version as get_minor_version,
    get_dearpygui_version as get_dearpygui_version,
    configure_item as configure_item,
    configure_app as configure_app,
    configure_viewport as configure_viewport,
    start_dearpygui as start_dearpygui,
    show_style_editor as show_style_editor,
    show_metrics as show_metrics,
    show_about as show_about,
    show_debug as show_debug,
    show_documentation as show_documentation,
    show_font_manager as show_font_manager,
    show_item_registry as show_item_registry,
    get_item_slot as get_item_slot,
    is_item_container as is_item_container,
    get_item_parent as get_item_parent,
    get_item_children as get_item_children,
    get_item_type as get_item_type,
    get_item_theme as get_item_theme,
    get_item_font as get_item_font,
    get_item_disabled_theme as get_item_disabled_theme,
    enable_item as enable_item,
    disable_item as disable_item,
    set_item_label as set_item_label,
    set_item_source as set_item_source,
    set_item_pos as set_item_pos,
    set_item_width as set_item_width,
    set_item_height as set_item_height,
    set_item_indent as set_item_indent,
    set_item_track_offset as set_item_track_offset,
    set_item_payload_type as set_item_payload_type,
    set_item_callback as set_item_callback,
    set_item_drag_callback as set_item_drag_callback,
    set_item_drop_callback as set_item_drop_callback,
    track_item as track_item,
    untrack_item as untrack_item,
    set_item_user_data as set_item_user_data,
    show_item as show_item,
    hide_item as hide_item,
    get_item_label as get_item_label,
    get_item_filter_key as get_item_filter_key,
    is_item_tracked as is_item_tracked,
    is_item_search_delayed as is_item_search_delayed,
    get_item_indent as get_item_indent,
    get_item_track_offset as get_item_track_offset,
    get_item_width as get_item_width,
    get_item_height as get_item_height,
    get_item_callback as get_item_callback,
    get_item_drag_callback as get_item_drag_callback,
    get_item_drop_callback as get_item_drop_callback,
    get_item_user_data as get_item_user_data,
    get_item_source as get_item_source,
    is_item_hovered as is_item_hovered,
    is_item_active as is_item_active,
    is_item_focused as is_item_focused,
    is_item_clicked as is_item_clicked,
    is_item_left_clicked as is_item_left_clicked,
    is_item_right_clicked as is_item_right_clicked,
    is_item_middle_clicked as is_item_middle_clicked,
    is_item_visible as is_item_visible,
    is_item_edited as is_item_edited,
    is_item_activated as is_item_activated,
    is_item_deactivated as is_item_deactivated,
    is_item_deactivated_after_edit as is_item_deactivated_after_edit,
    is_item_toggled_open as is_item_toggled_open,
    is_item_ok as is_item_ok,
    is_item_shown as is_item_shown,
    is_item_enabled as is_item_enabled,
    get_item_pos as get_item_pos,
    get_available_content_region as get_available_content_region,
    get_item_rect_size as get_item_rect_size,
    get_item_rect_min as get_item_rect_min,
    get_item_rect_max as get_item_rect_max,
    set_viewport_clear_color as set_viewport_clear_color,
    set_viewport_small_icon as set_viewport_small_icon,
    set_viewport_large_icon as set_viewport_large_icon,
    set_viewport_pos as set_viewport_pos,
    set_viewport_width as set_viewport_width,
    set_viewport_height as set_viewport_height,
    set_viewport_min_width as set_viewport_min_width,
    set_viewport_max_width as set_viewport_max_width,
    set_viewport_min_height as set_viewport_min_height,
    set_viewport_max_height as set_viewport_max_height,
    set_viewport_title as set_viewport_title,
    set_viewport_always_top as set_viewport_always_top,
    set_viewport_resizable as set_viewport_resizable,
    set_viewport_vsync as set_viewport_vsync,
    set_viewport_decorated as set_viewport_decorated,
    get_viewport_clear_color as get_viewport_clear_color,
    get_viewport_pos as get_viewport_pos,
    get_viewport_width as get_viewport_width,
    get_viewport_client_width as get_viewport_client_width,
    get_viewport_client_height as get_viewport_client_height,
    get_viewport_height as get_viewport_height,
    get_viewport_min_width as get_viewport_min_width,
    get_viewport_max_width as get_viewport_max_width,
    get_viewport_min_height as get_viewport_min_height,
    get_viewport_max_height as get_viewport_max_height,
    get_viewport_title as get_viewport_title,
    is_viewport_always_top as is_viewport_always_top,
    is_viewport_resizable as is_viewport_resizable,
    is_viewport_vsync_on as is_viewport_vsync_on,
    is_viewport_decorated as is_viewport_decorated,
    apply_transform as apply_transform,
    bind_colormap as bind_colormap,
    bind_font as bind_font,
    bind_item_font as bind_item_font,
    bind_item_handler_registry as bind_item_handler_registry,
    bind_item_theme as bind_item_theme,
    bind_theme as bind_theme,
    capture_next_item as capture_next_item,
    clear_selected_links as clear_selected_links,
    clear_selected_nodes as clear_selected_nodes,
    create_context as create_context,
    create_fps_matrix as create_fps_matrix,
    create_lookat_matrix as create_lookat_matrix,
    create_orthographic_matrix as create_orthographic_matrix,
    create_perspective_matrix as create_perspective_matrix,
    create_rotation_matrix as create_rotation_matrix,
    create_scale_matrix as create_scale_matrix,
    create_translation_matrix as create_translation_matrix,
    create_viewport as create_viewport,
    delete_item as delete_item,
    destroy_context as destroy_context,
    does_alias_exist as does_alias_exist,
    does_item_exist as does_item_exist,
    empty_container_stack as empty_container_stack,
    fit_axis_data as fit_axis_data,
    focus_item as focus_item,
    generate_uuid as generate_uuid,
    get_active_window as get_active_window,
    get_alias_id as get_alias_id,
    get_aliases as get_aliases,
    get_all_items as get_all_items,
    get_app_configuration as get_app_configuration,
    get_axis_limits as get_axis_limits,
    get_callback_queue as get_callback_queue,
    get_clipboard_text as get_clipboard_text,
    get_colormap_color as get_colormap_color,
    get_delta_time as get_delta_time,
    get_drawing_mouse_pos as get_drawing_mouse_pos,
    get_file_dialog_info as get_file_dialog_info,
    get_focused_item as get_focused_item,
    get_frame_count as get_frame_count,
    get_frame_rate as get_frame_rate,
    get_global_font_scale as get_global_font_scale,
    get_item_alias as get_item_alias,
    get_item_configuration as get_item_configuration,
    get_item_info as get_item_info,
    get_item_state as get_item_state,
    get_item_types as get_item_types,
    get_mouse_drag_delta as get_mouse_drag_delta,
    get_mouse_pos as get_mouse_pos,
    get_platform as get_platform,
    get_plot_mouse_pos as get_plot_mouse_pos,
    get_plot_query_rects as get_plot_query_rects,
    get_selected_links as get_selected_links,
    get_selected_nodes as get_selected_nodes,
    get_text_size as get_text_size,
    get_total_time as get_total_time,
    get_value as get_value,
    get_values as get_values,
    get_viewport_configuration as get_viewport_configuration,
    get_windows as get_windows,
    get_x_scroll as get_x_scroll,
    get_x_scroll_max as get_x_scroll_max,
    get_y_scroll as get_y_scroll,
    get_y_scroll_max as get_y_scroll_max,
    highlight_table_cell as highlight_table_cell,
    highlight_table_column as highlight_table_column,
    highlight_table_row as highlight_table_row,
    is_dearpygui_running as is_dearpygui_running,
    is_key_down as is_key_down,
    is_key_pressed as is_key_pressed,
    is_key_released as is_key_released,
    is_mouse_button_clicked as is_mouse_button_clicked,
    is_mouse_button_double_clicked as is_mouse_button_double_clicked,
    is_mouse_button_down as is_mouse_button_down,
    is_mouse_button_dragging as is_mouse_button_dragging,
    is_mouse_button_released as is_mouse_button_released,
    is_table_cell_highlighted as is_table_cell_highlighted,
    is_table_column_highlighted as is_table_column_highlighted,
    is_table_row_highlighted as is_table_row_highlighted,
    is_viewport_ok as is_viewport_ok,
    last_container as last_container,
    last_item as last_item,
    last_root as last_root,
    load_image as load_image,
    lock_mutex as lock_mutex,
    maximize_viewport as maximize_viewport,
    minimize_viewport as minimize_viewport,
    move_item as move_item,
    move_item_down as move_item_down,
    move_item_up as move_item_up,
    output_frame_buffer as output_frame_buffer,
    pop_container_stack as pop_container_stack,
    push_container_stack as push_container_stack,
    remove_alias as remove_alias,
    render_dearpygui_frame as render_dearpygui_frame,
    reorder_items as reorder_items,
    reset_axis_limits_constraints as reset_axis_limits_constraints,
    reset_axis_ticks as reset_axis_ticks,
    reset_axis_zoom_constraints as reset_axis_zoom_constraints,
    reset_pos as reset_pos,
    sample_colormap as sample_colormap,
    save_image as save_image,
    save_init_file as save_init_file,
    set_axis_limits as set_axis_limits,
    set_axis_limits_auto as set_axis_limits_auto,
    set_axis_limits_constraints as set_axis_limits_constraints,
    set_axis_ticks as set_axis_ticks,
    set_axis_zoom_constraints as set_axis_zoom_constraints,
    set_clip_space as set_clip_space,
    set_clipboard_text as set_clipboard_text,
    set_exit_callback as set_exit_callback,
    set_frame_callback as set_frame_callback,
    set_global_font_scale as set_global_font_scale,
    set_item_alias as set_item_alias,
    set_item_children as set_item_children,
    set_primary_window as set_primary_window,
    set_table_row_color as set_table_row_color,
    set_value as set_value,
    set_viewport_resize_callback as set_viewport_resize_callback,
    set_x_scroll as set_x_scroll,
    set_y_scroll as set_y_scroll,
    setup_dearpygui as setup_dearpygui,
    show_imgui_demo as show_imgui_demo,
    show_implot_demo as show_implot_demo,
    show_item_debug as show_item_debug,
    show_tool as show_tool,
    show_viewport as show_viewport,
    split_frame as split_frame,
    stop_dearpygui as stop_dearpygui,
    toggle_viewport_fullscreen as toggle_viewport_fullscreen,
    top_container_stack as top_container_stack,
    unhighlight_table_cell as unhighlight_table_cell,
    unhighlight_table_column as unhighlight_table_column,
    unhighlight_table_row as unhighlight_table_row,
    unlock_mutex as unlock_mutex,
    unset_table_row_color as unset_table_row_color,
    unstage as unstage,
)

globals()["__all__"] = tuple(set(globals()) - _globals)
