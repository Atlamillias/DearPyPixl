import types
import functools
import typing
from typing import Any

from dearpygui import _dearpygui

from . import interface
from . import parsing
from . import protocols
from . import appitem
from .appitem import AppItem  # export
from .protocols import Item, ItemCallback, mvMat4, Array, property, true, false

if typing.TYPE_CHECKING:
    from dearpypixl.items import mvThemeComponent




# [ itemtype registry ]

_REGISTRY = interface.Interface.__itemtype_registry__

REGISTRY: typing.Mapping[str, type[appitem.AppItem]] = types.MappingProxyType(_REGISTRY)


@typing.overload
def register[T: type[interface.Interface]](cls: T, /, name: str = ..., *, force: bool = ...) -> T: ...
@typing.overload
def register[T: type[interface.Interface]](name: str = ..., *, force: bool = ...) -> typing.Callable[[T], T]: ...
def register(cls = None, /, name: str = '', *, force = False) -> Any:  # pyright: ignore[reportInconsistentOverload]

    if isinstance(cls, str):
        assert not name
        cls, name = None, cls

    def wrapper(cls):
        nonlocal name
        if not name:
            name = cls.__name__
            if name.startswith("mv"):
                name = f"mvAppItemType::{name}"

        if force or name not in _REGISTRY:
            _REGISTRY[cls.__name__ if not name else name] = cls
        else:
            raise ValueError(f"{name!r} already registered")

        return cls

        return wrapper

    if cls is None:
        return wrapper

    return wrapper(cls)




# [ API mixin types ]

@staticmethod
@functools.cache
def _parse_element(category: int, target: int, type: str):
    if type.endswith('mvThemeColor'):
        elem_defs = parsing.theme_color_info()
    else:
        elem_defs = parsing.theme_style_info()

    for definition in elem_defs.values():
        if definition.target == target and definition.category == category:
            return definition

    raise RuntimeError('could not identify theme element.')


class ThemeAPI:
    __slots__ = ()

    @staticmethod
    def identify_element(element: Item, /) -> parsing.ThemeElementInfo:
        config = _dearpygui.get_item_configuration(element)
        return _parse_element(
            config['category'], config['target'], _dearpygui.get_item_info(element)['type'],
        )


class FontAPI:
    __slots__ = ()

    def get_text_size(self: Any, text: str, *, wrap_width: int = -1) -> list[float]:
        return _dearpygui.get_text_size(text, wrap_width=wrap_width, font=self)  # pyright: ignore[reportReturnType]


class DrawingAPI:
    __slots__ = ()

    __itemtype_indexer_slot__ = 2

    @staticmethod
    def create_fps_matrix(eye: protocols.Vec4[float], pitch: float, yaw: float) -> mvMat4:
        """Helper function for creating a "first person shooter" matrix.

        Args:
            * eye:

            * pitch:

            * yaw:
        """
        return _dearpygui.create_fps_matrix(eye, pitch, yaw)  # type: ignore

    @staticmethod
    def create_lookat_matrix(eye: protocols.Vec4[float], target: protocols.Vec4[float], up: protocols.Vec4[float]) -> mvMat4:
        return _dearpygui.create_lookat_matrix(eye, target, up)  # type: ignore

    @staticmethod
    def create_orthographic_matrix(left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> mvMat4:
        """Helper function for creating a orthographic matrix.

        Args:
            * left: Position of the clipping plane's left-most edge.

            * right: Position of the clipping plane's right-most edge.

            * bottom: Position of the clipping plane's lower-most edge.

            * top: Position of the clipping plane's upper-most edge.

            * zNear: Value used to calculate the minimum corner of the
            clipping plane.

            * zFar: Value used to calculate the maxmimum corner of the
            clipping plane.
        """
        return _dearpygui.create_orthographic_matrix(left, right, bottom, top, zNear, zFar)

    @staticmethod
    def create_perspective_matrix(fov: float, aspect: float, zNear: float, zFar: float) -> mvMat4:
        """Helper function for creating a perspective matrix.

        Args:
            * fov: Field-of-view angle.

            * aspect: Aspect ratio value.

            * zNear: Nearest z-axis point in the perspective.

            * zFar: Farthest z-axis point in the perspective.
        """
        return _dearpygui.create_perspective_matrix(fov, aspect, zNear, zFar)

    @staticmethod
    def create_rotation_matrix(angle: float, axis: protocols.Vec4[float]) -> mvMat4:
        """Helper function for creating a rotation matrix from a given
        angle and four-dimensional vector.

        Args:
            angle: The angle of rotation.

            axis: A four-dimensional vector that will be used
            to create the matrix.
        """
        return _dearpygui.create_rotation_matrix(angle, axis)  # type: ignore

    @staticmethod
    def create_scale_matrix(scales: protocols.Vec4[float]) -> mvMat4:
        """Helper function for creating a scaling matrix from a
        four-dimensional vector.

        Args:
            scales: A four-dimensional vector that will be used
            to create the matrix.
        """
        return _dearpygui.create_scale_matrix(scales)  # type: ignore

    @staticmethod
    def create_translation_matrix(translation: protocols.Vec4[float]) -> mvMat4:
        """Helper function for creating a translation matrix from a four-
        dimensional vector.

        Args:
            translation: A four-dimensional vector that will be used
            to create the matrix.
        """
        return _dearpygui.create_translation_matrix(translation)  # type: ignore




# [ behavior mixin types ]

class SupportsRect:
    __slots__ = ()

    width : property[int, int, true] = appitem.item_config_property(0)
    height: property[int, int, true] = appitem.item_config_property(0)

    @property
    def pos(self: typing.Any, /) -> list[int]:
        return _dearpygui.get_item_state(self)["pos"]
    @pos.setter
    def pos(self: typing.Any, value: typing.Sequence[int], /) -> None:
        _dearpygui.configure_item(self, pos=value)
    @pos.deleter
    def pos(self: typing.Any, /) -> None:
        _dearpygui.configure_item(self, pos=())

    resized: property[bool] = appitem.item_state_property()
    rect_min: property[list[int]] = appitem.item_state_property()
    rect_max: property[list[int]] = appitem.item_state_property()
    rect_size: property[list[int]] = appitem.item_state_property()
    content_region_avail: property[list[int]] = appitem.item_state_property()

    def _get_rect_min(self: Any, state) -> list[int]:
        value = state.get("rect_min")
        if value is None:
            return state["pos"]
        return value

    rect_min = typing.cast(
        property[list[int]],
        property(lambda self: self._get_rect_min(_dearpygui.get_item_state(self)))
    )

    def _get_rect_max(self: Any, state) -> list[int]:
        value = state.get("rect_max")
        if value is not None:
            return value

        x_pos, y_pos = state['pos']
        config = _dearpygui.get_item_configuration(self)
        return [x_pos + config["width"], y_pos + config["height"]]

    rect_max = typing.cast(
        property[list[int], typing.Never],
        property(lambda self: self._get_rect_max(_dearpygui.get_item_state(self)))
    )

    class _SizedItemState(interface.ItemStateDict):
        resized: bool
        rect_size: list[int]  # type: ignore
        rect_min: list[int]  # type: ignore
        rect_max: list[int]  # type: ignore
        pos: list[int]  # type: ignore
        content_region_avail: list[int]

    def state(self: Any) -> _SizedItemState:
        state = _dearpygui.get_item_state(self)
        state["rect_min"] = self._get_rect_min(state)
        state["rect_max"] = self._get_rect_max(state)
        return state # pyright: ignore[reportReturnType]


class SupportsValueArray[T]:
    __slots__ = ()

    def get_value(self: Any) -> list[T]:
        return _dearpygui.get_value(self) or []

    def set_value(self: Any, value: Array[T], /) -> None:
        _dearpygui.set_value(self, value)

    def __len__(self: Any) -> int:
        value = self.get_value()
        return 0 if not value else len(value)

    def __iter__(self) -> typing.Iterator[T]:
        return iter(self.get_value())

    def __reversed__(self) -> typing.Iterator[T]:
        yield from reversed(self.get_value())

    def __contains__(self: Any, value: T) -> bool:
        return value in self.get_value()

    @typing.overload
    def __getitem__(self: Any, index: typing.SupportsIndex, /) -> T: ...
    @typing.overload
    def __getitem__(self: Any, slice: slice, /) -> list[T]: ...
    def __getitem__(self: Any, index: Any, /) -> Any:
        return self.get_value()[index]

    @typing.overload
    def __setitem__(self: Any, index: typing.SupportsIndex, value: T, /) -> None: ...
    @typing.overload
    def __setitem__(self: Any, index: slice, value: typing.Sequence[T], /) -> None: ...
    def __setitem__(self: Any, index: Any, /, value: Any) -> None:
        item_value = self.get_value()
        item_value[index] = value
        self.set_value(value)

    def __eq__(self: Any, other: Any, /) -> bool:
        value = self.get_value()
        size = len(value)
        try:
            if len(other) != size:
                return False
            return all(value[i] == other[i] for i in range(size))
        except TypeError:
            return False


class SupportsCallback[CB: ItemCallback = Any]:
    __slots__ = ()

    def __call__(self: Any, app_data: Any = None, user_data: Any = None, /) -> None:
        callback = _dearpygui.get_item_configuration(self)["callback"]

        if callback:
            match len(callback.__code__.co_argcount):
                case 0:
                    callback()
                case 1:
                    callback(self)
                case 2:
                    callback(self, app_data)
                case _:
                    callback(self, app_data, user_data)

    __code__: types.CodeType = __call__.__code__

    @property
    def callback(self: Any) -> CB | None:
        """[get, set, del] the item's assigned callback. Dear PyGui
        calls this when a certain condition is met (varies based on
        the item)."""
        return _dearpygui.get_item_configuration(self)["callback"]
    @callback.setter
    def callback(self: Any, value: CB | None, /) -> None:
        _dearpygui.configure_item(self, callback=value)
    @callback.deleter
    def callback(self: Any, /) -> None:
        _dearpygui.configure_item(self, callback=None)




# [ core item types ]

@register
class ChildItem[U = Any, V = Any, P: ContainerItem[Any, Any, Any, Any] = Any](appitem.AppItem[U, V, P]):
    """A standard item. It can be parented by other items."""
    __slots__ = ()

    root_parent: property[RootItem, typing.Never]  # type: ignore

    def unstage(self) -> None:
        """Remove this item from its stage parent and move it to the
        item currently atop the container stack.

        A `mvStage` must be parenting this item when calling this
        method. Additionally, the container stack cannot be empty.
        Finally, the top-most item on the container stack must be a
        suitable parent for the item.
        """
        return _dearpygui.unstage(self)

    def move(self, *, parent: Item = 0, before: Item = 0) -> None:
        """Relocate the item.

        :type parent: `int | str`
        :param parent: Container  that will become this item's
            parent. If unspecified, the item's parent will not change.

        :type before: `int | str`
        :param before: Child item parented by *parent* (or this item's
            current parent if *parent* is unspecified). This item will
            be placed before that item. If unspecified, this item will
            be added as the parent's newest child.
        """
        return _dearpygui.move_item(self, parent=parent, before=before)  # type: ignore

    def move_up(self) -> None:
        """Move the item up, or back one position in the child slot
        that contains it."""
        return _dearpygui.move_item_up(self)

    def move_down(self) -> None:
        """Move the item down, or forward one position in the child
        slot that contains it.
        """
        return _dearpygui.move_item_down(self)

    def insert(self, index: typing.SupportsIndex, *, parent: Item = 0) -> None:
        """Similar to :py:meth:`move()` using the *before* keyword,
        except the item's new position amongst the parent's children
        is determined via 0-index.

        For a basic item such as a button,
        `button.insert(0, parent=new_parent)` is roughly equivelent to
        `button.move(parent=new_parent, before=new_parent.children()[button.child_slot_target()][0])`.

        :type index: `int | str`
        :param index: The new position of the item amongst other items
            in the child slot that will contain it.

        :type parent: `int | str`
        :param parent: Container item that will become this item's
            parent. If unspecified, the item's parent will not change.
        """
        item_info = _dearpygui.get_item_info(self)

        # XXX: DPG will do some extra work if we pass `parent` when
        # we aren't actually reparenting the item, so leave it default
        # when possible
        if parent is None or parent == 0:
            parent_item = item_info["parent"]
        else:
            parent_item = parent

        slot_index = self._get_child_slot_target(item_info["type"])
        child_slot = _dearpygui.get_item_info(parent_item)["children"][slot_index]

        _dearpygui.move_item(self, parent=parent, before=child_slot[index])

type ChildItemT = ChildItem[Any, Any, Any]


@register
class ContainerItem[U = Any, V = Any, P: ContainerItem[Any, Any, Any, Any] | None = Any, C: ChildItem[Any, Any, Any] = Any](
    appitem.AppItem[U, V, P]
):
    """An item that can parent other items. Some items may require
    specific types of parents.
    """
    __slots__ = ()

    def push(self) -> bool:
        """Push this item atop the container stack."""
        return _dearpygui.push_container_stack(self)

    def __enter__(self) -> typing.Self:
        _dearpygui.push_container_stack(self)
        return self

    @staticmethod
    def pop() -> None:
        """Pop the top-most item off the container stack (if any)."""
        _dearpygui.pop_container_stack()

    def __exit__(self, exc_type = None, value = None, traceback = None, /) -> None:
        _dearpygui.pop_container_stack()

    def reorder(self, /, slot: typing.Literal[0, 1, 2, 3], new_order: list[Item] | tuple[Item, ...]) -> None:
        """Re-arrange an item's children within a specific slot.

        :type slot: `Literal[0, 1, 2, 3]`
        :param slot: The index of the target slot.

        :type new_order: `list[int | str] | tuple[int | str, ...]`
        :param new_order: The contents of the target slot, arranged as
            desired.

        An example of reversing the positions of rows in a table:
        >>> table = ...
        >>> rows = table.children(1)
        >>> rows.reverse()
        >>> table.reorder(1, rows)
        """
        # BUG/TODO: `new_order` parameter isn't typed to support aliases
        _dearpygui.reorder_items(self, slot, new_order)  # pyright: ignore[reportArgumentType]

    __itemtype_indexer_slot__: typing.ClassVar[typing.Literal[0, 1, 2, 3]] = 1
    __itemtype_indexer_type__: typing.ClassVar[type[ChildItem]] = ChildItem  # pyright: ignore[reportGeneralTypeIssues]

    @typing.overload
    def __getitem__(self, index: typing.SupportsIndex, /) -> C: ...
    @typing.overload
    def __getitem__(self, slice: slice, /) -> list[C]: ...
    def __getitem__(self, index, /): # pyright: ignore[reportInconsistentOverload]
        res = _dearpygui.get_item_info(self)["children"][self.__itemtype_indexer_slot__][index]
        if hasattr(res, '__iter__'):
            item_type = self.__itemtype_indexer_type__
            interface = self._interface
            return [interface(item_type, axis) for axis in res]
        return self._interface(self.__itemtype_indexer_type__, res)

    @typing.overload
    def __delitem__(self, index: typing.SupportsIndex, /) -> None: ...
    @typing.overload
    def __delitem__(self, slice: slice, /) -> None: ...
    def __delitem__(self, index, /):
        res = _dearpygui.get_item_info(self)["children"][1][index]
        if hasattr(res, '__iter__'):
            delete = _dearpygui.delete_item
            for axis in res:
                delete(axis, children_only=False, slot=-1)

    def index(self, item: Item, /) -> int:
        if isinstance(item, str):
            tag = _dearpygui.get_alias_id(item)
        else:
            tag = item

        return _dearpygui.get_item_info(self)["children"][self.__itemtype_indexer_slot__].index(tag)

type ContainerItemT = ContainerItem[Any, Any, Any, Any]


@register
class RootItem[U = Any, C: ChildItemT = Any, V: Any = None](ContainerItem[U, V, None, C]):
    """Top-level container. It cannot be parented by other items, making
    `RootItem` and `ChildItem` mutually exclusive."""
    __slots__ = ()

    @property
    def root_parent(self) -> None:
        return None

    @property
    def parent(self) -> None:
        return None

    @property
    def parents(self) -> typing.Sequence[ContainerItem]:
        return []

type RootItemT = RootItem[Any, Any, Any]


class CompositeItem:
    __slots__ = ()

    components: typing.Collection = ()

def _build_CompositeItem() -> typing.Any:
    class Class:
        __slots__ = ()

        components: typing.Collection = ()

        @property
        def user_data(self) -> typing.Any:
            return self.__dict__.get("user_data", None)
        @user_data.setter
        def user_data(self, value: typing.Any, /) -> None:
            self.__dict__["user_data"] = value
        @user_data.deleter
        def user_data(self, /) -> None:
            self.__dict__["user_data"] = None

        def __init__(self: typing.Any, /, tag: Item = 0) -> None:
            user_data = _dearpygui.get_item_configuration(self)["user_data"]
            if user_data is None:
                _dearpygui.configure_item(self, user_data=self.__dict__)
            else:
                self.__dict__ = user_data

        def destroy(self, /, *, _delete_item=_dearpygui.delete_item) -> None:
            for item in self.components:
                destructor = getattr(item, "destroy", None)
                if callable(destructor):
                    destructor()
                else:
                    try:
                        _delete_item(item, children_only=False, slot=-1)
                    except SystemError:
                        pass

            try:
                self.__dict__.clear()
            except AttributeError:
                pass

            super().destroy()  # type: ignore

        _MISSING = object()

        def configure(self: typing.Any, /, user_data=_MISSING, __missing=_MISSING, **kwargs):
            super().configure(**kwargs)  # type: ignore
            if user_data is not __missing:
                self.user_data = user_data  # type: ignore

        del _MISSING

        def configuration(self: typing.Any, /):
            config = super().configuration()  # type: ignore
            config["user_data"] = self.user_data
            return config

    Class.__qualname__ =  CompositeItem.__qualname__
    Class.__name__ =  CompositeItem.__name__

    funcs = (
        Class.user_data.fget, Class.user_data.fset, Class.user_data.fdel,
        Class.__init__, Class.configure, Class.configuration
    )
    for func in funcs:
        func.__qualname__ = f"{CompositeItem.__name__}.{func.__name__}"  # type: ignore

    globals()["CompositeItem"] = Class
    del Class, funcs, func  # type: ignore
    del globals()["_build_CompositeItem"]

_build_CompositeItem()




# [ derived mixin types ]

class ChildContainerItem[U = Any, V = Any, P: ContainerItemT = Any, C: ChildItemT = Any](
    ContainerItem[U, V, P, C], ChildItem[U, V, P],
):
    __slots__ = ()


class ChildValueArrayItem[U = Any, V: int | float = float, P: ContainerItemT = Any](
    SupportsValueArray[V], ChildItem[U, list[V], P]
):
    __slots__ = ()


class ChildCallbackItem[U = Any, V = Any, P: ContainerItemT = Any, CB: ItemCallback = Any](
    SupportsCallback[CB], ChildItem[U, V, P]
):
    __slots__ = ()




# [ generic interfaces ]

class GenericChildItem[U = Any, V = Any, P: ContainerItemT = Any](ChildItem[U, V, P]):
    __slots__ = ()

    @typing.final
    @staticmethod
    def __itemtype_command__(*args, tag: int | str = 0, **kwargs) -> typing.Never:
        raise NotImplementedError

    @typing.final
    @classmethod
    def create(cls, /, *args, **kwargs) -> typing.Never:
        raise NotImplementedError

    def __getattr__(self, name: str, /) -> Any:
        try:
            return _dearpygui.get_item_configuration(self)[name]
        except (KeyError, SystemError):
            raise AttributeError(f"{type(self).__name__!r} object has no attribute {name!r}")


class ValueArrayItem[U = Any, V = Any, P: ContainerItemT = Any](SupportsValueArray[V], GenericChildItem[U, list[V], P]):
    __slots__ = ()


class ElementItem[U = Any, V: int | float = float](ThemeAPI, ValueArrayItem[U, V, "mvThemeComponent"]):
    __slots__ = ()

    @property
    def category(self) -> int:
        return _dearpygui.get_item_configuration(self)["category"]

    @property
    def target(self, /) -> int:
        return _dearpygui.get_item_configuration(self)["target"]

    def identity(self, /) -> parsing.ThemeElementInfo:
        return self.identify_element(self)


class HandlerItem[U = Any, CB: ItemCallback = Any](ChildCallbackItem[U, None, RootItem, CB]):
    __slots__  = ()

    show: property[bool, bool, false] = appitem.item_config_property()
