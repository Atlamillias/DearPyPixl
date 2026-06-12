"""Contains utilities that help improve interoperability between
Python and DearPyGui. Many interface types exposed in this module
implement a specific Python protocol (`MutableSequence`,
`WritableBuffer`, etc), allowing them to be used in both data-oriented
and UI code.
"""
import threading

from dearpypixl.core import appitem
from dearpypixl.core import metautil
from dearpygui import _dearpygui

import typing
if typing.TYPE_CHECKING:
    from dearpypixl.core.protocols import Item
    from dearpypixl.core.protocols import Array




# [ ValueArray ]

class ValueArray[V = typing.Any, U = typing.Any](appitem.CompositeItem, appitem.AppItem[U, V, None, typing.Any]):
    """Creates/manages a `mvValueRegistry` and its children in child slot
    1. The interface behaves similarly to a mutable, homogeneous array that
    exposes and manages the values of those children. While data-oriented
    code can treat it as any other mutable sequence, UI code can use the
    registry's children as sources for other items. Users can register
    any number of callbacks that fire on value item creation, deletion, or
    update.

    Direct :py:class:`ValueArray` instances are **not** generic. Inner
    value types are limited to the value storage type of `mv*Value` items
    created by the :py:meth:`create_value_item()` method.

    Most interface operations are made thread-safe using a reentrant lock.
    However, iteration is *not* one of them, so it is recommended to hold
    the :py:attr:`lock` during iteration.

    Note that `__getattr__()` does not operate on child slots (the default
    behavior inherited from :py:class:`AppItem`), but the values and
    lifetimes of the registry's children in child slot 1 instead.

    Unlike `list`, operations that result in creating a new sequence
    (such as concationation) instead perform in-place mutation e.g.
    `seq + ['hello', 'world']` is equivelent to `seq += ['hello', 'world']`.
    However, the :py:meth:`copy()` method *will* return a new item/interface.

    The interface also implements the :py:meth:`appendleft()`,
    :py:meth:`extendleft()`, :py:meth:`popleft()` and :py:meth:`rotate()`
    methods, whose behaviors mirror those found on `collections.deque`.

    Users should not directly manage the registry's children in child slot
    1 as it may cause undefined behavior.

    References
    ----------
    - :py:meth:`create_value_item()`
    - :py:meth:`update_value_item()`
    - :py:meth:`delete_value_item()`
    - :py:attr:`on_value_create`
    - :py:attr:`on_value_update`
    - :py:attr:`on_value_delete`
    - :py:attr:`on_value_reorder`

    :vartype on_value_create: `EventContainer[[Self, Item]]`
    :var on_value_create: A `list`-like object containing callbacks to
        invoke immediately following the creation of a new value
        item. Callbacks will receive the registry and item in context
        as arguments.

    :vartype on_value_update: `EventContainer[[Self, Item, Any]]`
    :var on_value_update: A `list`-like object containing callbacks to
        invoke immediately following the update of an existing value
        item. Callbacks will receive the registry, the item in context,
        and the item's new value as arguments.

    :vartype on_value_delete: `EventContainer[[Self, Item]]`
    :var on_value_delete: A `list`-like object containing callbacks to
        invoke immediately before deleting a value item.
        Callbacks will receive the registry and item in context as arguments.

    :vartype on_value_reorder: `EventContainer[[Self, list[Item], list[Item]]]`
    :var on_value_reorder: A `list`-like object containing callbacks to
        invoke immediately after reordering items in child slot 1. Callbacks
        will receive the registry and reordered child slot 1 as arguments.
    """
    on_value_create: metautil.EventContainer[[typing.Self, Item]]
    on_value_update: metautil.EventContainer[[typing.Self, Item, V]]
    on_value_delete: metautil.EventContainer[[typing.Self, Item]]
    on_value_reorder: metautil.EventContainer[[typing.Self, typing.Sequence[Item]]]

    _lock: threading.Lock | threading.RLock

    @property
    def lock(self, /) -> threading.Lock | threading.RLock:
        return self._lock

    _command: typing.Callable[..., Item] | None

    @property
    def command(self, /) -> typing.Callable[..., Item] | None:
        return self._command

    @property
    def items(self, /) -> list[int]:
        """[***get***] all items in child slot 1."""
        return _dearpygui.get_item_info(self)["children"][1]

    @property
    def value(self, /) -> list[V]: # pyrefly: ignore [bad-override]
        """[***get***, ***set***] the values of all `mvStringValue` children in
        the registry as a sequence of strings.

        The registry always has a number of `mvStringValue` children equal to
        the length of its value. Children and value elements are associated by
        index and can be paired via `zip(self.items, self.value)`. On set, the
        number of `mvStringValue` children parented by the registry will update
        accordingly to match the length of the value.
        """
        with self._lock:
            value = _dearpygui.get_values(_dearpygui.get_item_info(self)["children"][1])
        return value
    @value.setter
    def value(self, value: typing.Iterable[V], /) -> None:
        if not value:
            self.clear()
        else:
            self[:] = value

    _position = -1

    @property
    def position(self, /) -> int:
        """[***get***] the last append or insertion index. A positive
        integer is returned for insertions while `-1` is returned for
        appends.
        """
        return self._position

    _maxlen = None

    @property
    def maxlen(self, /) -> int | None:
        return self._maxlen
    @maxlen.setter
    def maxlen(self, value: int | None, /) -> None:
        if value is None:
            self._maxlen = None
            return
        if value < 0:
            raise ValueError(f"`maxlen` must be a positive integer or `None` -- got {value!r}")
        with self._lock:
            self._maxlen = value
            self._trunc(-1, _dearpygui.get_item_info(self)["children"][1])
    @maxlen.deleter
    def maxlen(self, /) -> None:
        del self._maxlen

    @typing.overload
    @classmethod
    def create(cls, /, command: typing.Callable[..., Item] | None = ..., *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> typing.Self: ...  # pyrefly: ignore [bad-override, inconsistent-overload]
    @typing.overload
    @classmethod
    def create(cls, iterable: typing.Iterable[V], /, command: typing.Callable[..., Item] | None = ..., *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> typing.Self: ...
    @classmethod
    def create(cls, iterable = None, /, command = None, *, label=None, use_internal_label=True, user_data=None, tag=0, **kwargs) -> typing.Self:
        if command is None:
            # static `_command` or overridden `create_value_item()`
            if cls._command is not None or cls.create_value_item is not __class__.create_value_item:
                command = cls._command
            elif callable(iterable):
                command, iterable = iterable, command
            elif iterable is None:
                raise TypeError(f"{cls.__name__}.create() missing 1 required parameter `command`")
            else:
                raise TypeError("`command` argument not callable")

        self = cls(tag=_dearpygui.add_value_registry(
            label=label,  # type: ignore
            use_internal_label=use_internal_label, tag=tag, user_data={"user_data": user_data}
        ))

        self._lock = threading.RLock()
        self._command = command  # type: ignore
        self.on_value_create = metautil.EventContainer(positional_only=True, parg_count=2)
        self.on_value_update = metautil.EventContainer(positional_only=True, parg_count=3)
        self.on_value_delete = metautil.EventContainer(positional_only=True, parg_count=2)
        self.on_value_reorder = metautil.EventContainer(positional_only=True, parg_count=2)

        if iterable:
            self.extend(iterable)

        return self

    def create_value_item(self, /) -> Item:
        """Called internally to create a new value child item. Returns
        the item created.

        The default implementation is equivelent to `self.command(parent=self)`,
        but overriding implementations may ignore :py:attr:`command` entirely.

        Does not emit events.
        """
        return self._command(parent=self)  # pyrefly: ignore [not-callable]

    def update_value_item(self, item: Item, value: V, /) -> None:
        """Called internally to update the value of an existing `mvStringValue`
        parented by the registry.

        Does not emit events.
        """
        _dearpygui.set_value(item, value)

    def delete_value_item(self, item: Item = 0, /) -> None:
        """Called internally to delete an existing `mvStringValue` parented
        by the registry, or all value items when *item* is null.

        Does not emit events.
        """
        if item:
            _dearpygui.delete_item(item, children_only=False, slot=-1)
        else:
            _dearpygui.delete_item(self, children_only=True, slot=1)

    def _trunc(self, index: typing.Literal[0, -1], children, /):
        if (maxlen := self._maxlen) is None or (offset := len(children) - maxlen) <= 0:
            return

        if index < 0:
            iterator = range(index, index-offset, -1)
        else:
            iterator = range(index, (index + offset))

        del_item = self.delete_value_item
        callback = self.on_value_delete

        for i in iterator:
            item = children[i]
            callback(self, item)
            del_item(item)

    def __len__(self, /) -> int:
        """Return the number of children in child slot 1."""
        return len(_dearpygui.get_item_info(self)["children"][1])

    def __iter__(self, /) -> typing.Iterator[V]:
        """Iterate through the values of items in child slot 1."""
        get_value = _dearpygui.get_value
        for item in _dearpygui.get_item_info(self)["children"][1]:
            try:
                yield get_value(item)
            except SystemError:  # item no longer exists?
                continue

    def __reversed__(self, /) -> typing.Iterator[V]:
        get_value = _dearpygui.get_value

        items = _dearpygui.get_item_info(self)["children"][1]
        items.reverse()
        for item in items:
            try:
                yield get_value(item)
            except SystemError:  # item no longer exists?
                continue

    def __contains__(self, other: typing.Any, /) -> bool:
        """Checks if *other* equals a value of an item in child slot 1."""
        if isinstance(other, str):
            return False

        get_value = _dearpygui.get_value
        for item in _dearpygui.get_item_info(self)["children"][1]:
            try:
                value = get_value(item)
            except SystemError:  # item no longer exists?
                continue

            if other == value:
                return True

        return False

    @typing.overload
    def __getitem__(self, index: typing.SupportsIndex, /) -> V: ...  # type: ignore
    @typing.overload
    def __getitem__(self, slice: slice, /) -> list[V]: ...  # type: ignore
    def __getitem__(self, index, /):
        """Return the value(s) of item(s) in child slot 1 at the given index
        or slice."""
        with self._lock:
            items = _dearpygui.get_item_info(self)["children"][1][index]
            value = (_dearpygui.get_values if type(items) is list else _dearpygui.get_value)(items)
        return value

    @typing.overload
    def __setitem__(self, index: typing.SupportsIndex, value: V, /) -> None: ...
    @typing.overload
    def __setitem__(self, slice: slice, value: typing.Iterable[V], /) -> None: ...
    def __setitem__(self, index, value, /) -> None:
        """Update the value(s) of item(s) in child slot 1 at the given index
        or slice.

        Updates via slice assignment will create or delete items as needed when
        the length of *value* differs from the number of items/values found
        given the slice.
        """
        with self._lock:
            children = _dearpygui.get_item_info(self)["children"][1]

            if isinstance(index, slice):
                assert not isinstance(value, str)
                items = children[index]
                lines = value

                n_items = len(items)
                n_lines = len(lines)
                reorder = False

                if n_lines > n_items:
                    reorder  = True
                    iterator = range(n_lines - n_items)

                    callback = self.on_value_create
                    for _ in iterator:
                        item = self.create_value_item()
                        items.append(item)
                        self._position = -1
                        callback(self, item)

                elif n_items > n_lines:
                    iterator = range(n_items - n_lines)

                    callback = self.on_value_delete
                    for _ in iterator:
                        item = items.pop()
                        callback(self, item)
                        self.delete_value_item(item)

                callback = self.on_value_update
                for item, line in zip(items, lines):
                    self.update_value_item(item, line)
                    callback(self, item, line)

                if reorder:
                    children[index] = items
                    _dearpygui.reorder_items(self, 1, children)  # pyrefly: ignore [bad-argument-type]

                self._trunc(-1, children)

            else:
                self.update_value_item(children[index], value)

    @typing.overload
    def __delitem__(self, index: typing.SupportsIndex, /) -> None: ...
    @typing.overload
    def __delitem__(self, slice: slice, /) -> None: ...
    def __delitem__(self, index, /):
        """Delete the item(s) in child slot 1 at the given index or slice."""
        callback = self.on_value_delete

        with self._lock:
            items = _dearpygui.get_item_info(self)["children"][1][index]
            if type(items) is list:
                for item in items:
                    callback(self, item)
                    self.delete_value_item(item)
            else:
                self.delete_value_item(items)

    def __copy__[T](self, memo=None, /) -> typing.Self:
        config = self.configuration()
        return self.create(
            self.value,
            label=config["label"], use_internal_label=config["use_internal_label"], user_data=config["user_data"]
        )

    def copy(self, /) -> typing.Self:
        return self.__copy__()

    def sort(self, /, *, key: typing.Callable[[V], typing.Any] | None = None, reverse: bool = False) -> None:
        """Sorts the items in child slot 1 based on their values.

        Emits an "on reorder" event.
        """
        if key is None:
            if reverse:
                self.reverse()
            return

        def _key(x, key=key):
            return key(x[0])

        with self._lock:
            items = _dearpygui.get_item_info(self)["children"][1]
            if not items:
                return

            values = _dearpygui.get_values(items)

            items = [i for s, i in sorted(zip(values, items), key=_key, reverse=reverse)]
            _dearpygui.reorder_items(self, 1, items)
            self.on_value_reorder(self, items)

    def reverse(self, /) -> None:
        """Reverse the order of items in child slot 1.

        Emits an "on reorder" event.
        """
        with self._lock:
            items = _dearpygui.get_item_info(self)["children"][1]

            if items:
                items.reverse()
                _dearpygui.reorder_items(self, 1, items)
                self.on_value_reorder(self, items)

    def index(self, value: V, /, start: typing.SupportsIndex = 0, stop: typing.SupportsIndex | None = None) -> int:
        """Return the index where an item's value in child slot 1 matches *value*."""
        # TODO: revise later (perf)
        with self._lock:
            values = _dearpygui.get_values(_dearpygui.get_item_info(self)["children"][1])

        if stop is not None:
            return values.index(value, start, stop)
        return values.index(value, start)

    def insert(self, index: typing.SupportsIndex, value: V, /) -> None:
        """Create and insert a new `mvStringValue` item *index* and set its value
        to *value*.

        Emits an "on create" and "on update" event.
        """
        index = int(index)

        with self._lock:
            children = _dearpygui.get_item_info(self)["children"][1]

            # mirrors `deque.insert()` with `maxlen` set
            if (maxlen := self._maxlen) is not None and len(children) >= maxlen:
                raise IndexError("insert would cause the sequence length to exceed `maxlen`")

            if index < 0:
                index %= len(children)

            # value items don't accept the `before` argument, so a
            # reorder is necessary
            item = self.create_value_item()
            children.insert(index, item)
            _dearpygui.reorder_items(self, 1, children)  # pyrefly: ignore [bad-argument-type]
            self._position = index
            self.on_value_create(self, item)

            self.update_value_item(item, value)
            self.on_value_update(self, item, value)

    def append(self, value: V, /) -> None:
        """Create a new `mvStringValue` item and set its value to *value*.

        Emits an "on create" and "on update" event.
        """
        with self._lock:
            item = self.create_value_item()
            self._position = -1
            self.on_value_create(self, item)

            self.update_value_item(item, value)
            self.on_value_update(self, item, value)

            if self._maxlen is not None:  # avoid DLL call if possible
                self._trunc(0, _dearpygui.get_item_info(self)["children"][1])

    def appendleft(self, value: V, /) -> None:
        """Create and insert a new `mvStringValue` item *index* and set its value
        to *value*.

        Emits an "on create" and "on update" event.
        """
        with self._lock:
            children = _dearpygui.get_item_info(self)["children"][1]

            # value items don't accept the `before` argument, so a
            # reorder is necessary
            item = self.create_value_item()
            children.insert(0, item)
            _dearpygui.reorder_items(self, 1, children)  # pyrefly: ignore [bad-argument-type]
            self._position = 0
            self.on_value_create(self, item)

            self.update_value_item(item, value)
            self.on_value_update(self, item, value)

            self._trunc(-1, children)

    def extend(self, values: typing.Iterable[V], /) -> None:
        """Create new value items equal to the number of strings in
        *value* and update the value of each.

        Emits an "on create" and "on update" event for every item created.
        """
        created_callback = self.on_value_create
        updated_callback = self.on_value_update
        with self._lock:
            for s in values:
                item = self.create_value_item()
                self._position = -1
                created_callback(self, item)
                self.update_value_item(item, s)
                updated_callback(self, item, s)

            if self._maxlen is not None:  # avoid DLL call if possible
                self._trunc(0, _dearpygui.get_item_info(self)["children"][1])

    def extendleft(self, values: typing.Iterable[V], /) -> None:
        """Create new value items equal to the number of strings in
        *value* and update the value of each.

        Emits an "on create" and "on update" event for every item created.
        """
        created_callback = self.on_value_create
        updated_callback = self.on_value_update
        with self._lock:
            children = _dearpygui.get_item_info(self)["children"][1]

            if not hasattr(values, '__getitem__'):
                values = tuple(values)

            items = [self.create_value_item() for _ in values]
            children[:0] = items

            _dearpygui.reorder_items(self, 1, children)

            for i, (item, value) in enumerate(zip(items, values)):
                self._position = i
                created_callback(self, item)
                self.update_value_item(item, value)
                updated_callback(self, item, value)

    __add__ = __iadd__ = extend  # type: ignore

    def rotate(self, offset: int, /) -> None:
        """Offset items/values a number of positions equal to the absolute
        value of *offset*. The direction of rotation is determined by the
        sign of *offset* -- a positive value rotates to the right, while a
        negative value rotates to the left.

        Emits an "on reorder" event if the new order differs from the
        previous order.
        """
        if not offset:
            return

        if offset < 0:
            cw = False
            offset *= cw
        else:
            cw = True

        with self._lock:
            children = _dearpygui.get_item_info(self)["children"][1]
            length   = len(children)

            offset %= length  # eliminate wrap-around
            if not offset:
                return

            if cw:
                idst = slice(None, 0)
                isrc = slice(length-offset, length+1)
            else:
                idst = slice(-1, None)
                isrc = slice(0, offset)

            children[idst] = children[isrc]
            del children[isrc]

            _dearpygui.reorder_items(self, 1, children)
            self.on_value_reorder(self, children)

    def remove(self, value: V, /) -> None:
        """Destroy the first item in child slot 1 with a value equal to
        *value*.

        Emits an "on delete" event.
        """
        get_value = _dearpygui.get_value
        callback  = self.on_value_delete

        with self._lock:
            children = _dearpygui.get_item_info(self)["children"][1]

            for item in children:
                if get_value(item) == value:
                    callback(self, item)
                    self.delete_value_item(item)
                    break

        raise ValueError(f"{value!r} not in self")

    def pop(self, index: typing.SupportsIndex = -1, /) -> V:
        """Return the value of the item in child slot 1 at *index*, deleting
        the item in the process.

        Emits an "on delete" event.
        """
        with self._lock:
            item = _dearpygui.get_item_info(self)["children"][1][index]
            self.on_value_delete(self, item)

            value = _dearpygui.get_value(item)
            self.delete_value_item(item)

        return value

    def popleft(self, /) -> V:
        """Return the value of the first item in child slot 1, deleting
        the item in the process.

        Emits an "on delete" event.
        """
        return __class__.pop(self, 0)

    def clear(self, /) -> None:
        """Destroys all items in child slot 1, emptying the registry.

        Emits a number of "on delete" events.

        ***NOTE**: For performance reasons, all items in child slot 1 are
        destroyed together **after** :py:attr:`on_value_delete` is
        invoked for each item. This includes any items created as a result
        of the callback(s).*
        """
        callback = self.on_value_delete
        with self._lock:
            if len(callback):
                for item in _dearpygui.get_item_info(self)["children"][1]:
                    callback(self, item)
            self.delete_value_item()

def add_string_value_array[U](iterable: typing.Iterable[str], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[str, U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_string_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_int_value_array[U](iterable: typing.Iterable[int], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[int, U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_int_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_int4_value_array[U](iterable: typing.Iterable[typing.Sequence[int]], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[typing.Sequence[int], U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_int4_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_bool_value_array[U](iterable: typing.Iterable[bool], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[bool, U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_bool_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_color_value_array[U](iterable: typing.Iterable[Array[int | float, typing.Literal[3, 4]]], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[Array[int | float, typing.Literal[3, 4]], U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_color_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_float_value_array[U](iterable: typing.Iterable[float], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[float, U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_float_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_float4_value_array[U](iterable: typing.Iterable[Array[float, typing.Literal[4]]], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[Array[float, typing.Literal[4]], U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_float4_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_floatvect_value_array[U](iterable: typing.Iterable[typing.Sequence[float]], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[typing.Sequence[float], U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_float_vect_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_double_value_array[U](iterable: typing.Iterable[float], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[float, U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_double_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_double4_value_array[U](iterable: typing.Iterable[Array[float, typing.Literal[4]]], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[Array[float, typing.Literal[4]], U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_double4_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)

def add_series_value_array[U](iterable: typing.Iterable[typing.Sequence[float]], /, *, label: str | None = None, use_internal_label: bool = True, user_data: U | None = None, tag: int | str = 0, **kwargs) -> ValueArray[typing.Sequence[float], U]:
    """Create and return a new :py:class:`ValueArray` item/interface."""
    return ValueArray.create(iterable, command=_dearpygui.add_series_value, label=label, use_internal_label=use_internal_label, tag=tag, user_data=user_data, **kwargs)


class StringValueArray[U = typing.Any](ValueArray[str, U]):
    """A :py:class:`ValueArray` that contains only string
    values. In addition, it defines the :py:meth:`write()` and
    :py:meth:`writelines()` methods, allowing it to be used as a
    writable stream in many contexts.
    """
    def create_value_item(self, /) -> Item:
        return _dearpygui.add_string_value(parent=self)

    def write(self, s: str, /) -> int:
        """Evaluate `self.append(s)`, then return the length of the
        string appended."""
        self.append(s)
        return len(s)

    def writelines(self, lines: typing.Iterable[str], /) -> None:
        """Return `self.extend(lines)`."""
        self.extend(lines)

    def flush(self, /) -> None:
        return


#class LineBuffer[U = typing.Any](ValueArray[str, U]):
#    """A :py:class:`ValueArray` item/interface representing the
#    lines of text in a file or string. Strings added to the buffer
#    containing newlines are automatically expanded into multiple
#    entries.
#
#    When mutating the buffer, strings and string sequences used as
#    arguments/operands are non-distinct. For example, the buffer
#    treats `"hello\nworld"`, `["hello\nworld"]`, and `["hello",
#    "world"]` as if they were equal, regardless of the operation
#    in context -- `buffer.append("hello\nworld")`,
#    `buffer.append(["hello\nworld"])`, and `buffer.extend("hello\nworld")`
#    all evaluate to `buffer.extend(["hello", "world"])`.
#    """
#
#    _newline = "\n"
#
#    def _normalize_argument(self, iterable: typing.Iterable[str], /):
#        if isinstance(iterable, str):
#            return iterable.split(self._newline)
#
#        newline = self._newline
#        result  = []
#        for s in iterable: result.extend(s.split(newline))
#
#        return result
