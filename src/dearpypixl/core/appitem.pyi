"""Base implementations for DearPyGui item interfaces."""
from typing import *
import types

from dearpypixl.core.protocols import Item
from dearpypixl.core.protocols import ItemCallback
from dearpypixl.core.protocols import Array
from dearpypixl.core.interface import Interface
from dearpypixl.lib.items import mvStage
from dearpypixl.lib.items import mvTheme
from dearpypixl.lib.items import mvThemeColor
from dearpypixl.lib.items import mvThemeStyle
from dearpypixl.lib.items import mvFont
from dearpypixl.lib.items import mvHandlerRegistry
from dearpypixl.lib.items import mvItemHandlerRegistry
from dearpypixl.lib.items import mvThemeComponent
from dearpypixl.lib.items import mvTemplateRegistry


__all__ = (
    "AppItem",
    "ChildItem",
    "ContainerItem",
    "SupportsValueArray",
    "_HandlerItem",
    "_ElementItem",
)




class _ItemStateDict(TypedDict):
    ok: bool
    pos: Annotated[list[int], 2]
    active: NotRequired[bool]
    clicked: NotRequired[bool]
    left_clicked: NotRequired[bool]
    right_clicked: NotRequired[bool]
    middle_clicked: NotRequired[bool]
    edited: NotRequired[bool]
    activated: NotRequired[bool]
    deactivated: NotRequired[bool]
    deactivated_after_edit: NotRequired[bool]
    hovered: NotRequired[bool]
    focused: NotRequired[bool]
    visible: NotRequired[bool]
    resized: NotRequired[Annotated[list[int], 2]]
    rect_min: NotRequired[Annotated[list[int], 2]]
    rect_max: NotRequired[Annotated[list[int], 2]]
    rect_size: NotRequired[Annotated[list[int], 2]]
    content_region_avail: NotRequired[Annotated[list[int], 2]]

type _ItemStateDict = _ItemStateDict | Any

class _ItemInfoDict(TypedDict):
    children: Mapping[Literal[0, 1, 2, 3], list[Item]]
    type: str
    target: int
    parent: Item | None
    theme: Item | None
    handlers: Item | None
    font: Item | None
    container: bool
    hover_handler_applicable: bool
    active_handler_applicable: bool
    focus_handler_applicable: bool
    clicked_handler_applicable: bool
    visible_handler_applicable: bool
    edited_handler_applicable: bool
    activated_handler_applicable: bool
    deactivated_handler_applicable: bool
    deactivatedae_handler_applicable: bool
    toggled_open_handler_applicable: bool
    resized_handler_applicable: bool

type _ItemInfoDict = _ItemInfoDict | Any


class AppItemType(type):
    @final
    @property
    def __item_registry__(self, /) -> Mapping[str | int, type[AppItem]]: ...
    @final
    @property
    def __item_type__(self, /) -> type[AppItem]: ...
    @final
    @property
    def __item_slot__(self, /) -> int: ...
    @final
    @property
    def __item_command__(self, /) -> str: ...
    @final
    @property
    def __item_parents__(self, /) -> tuple[type[ContainerItem], ...]: ...
    @final
    @property
    def __item_children__(self, /) -> tuple[type[ChildItem], ...]: ...
    def __int__(self, /) -> int: ...
    def __index__(self, /) -> int: ...
    def __str__(self, /) -> str: ...
    def __repr__(self, /) -> str: ...
    def __hash__(self, /) -> int: ...
    def __eq__(self, other: Any, /) -> bool: ...


class AppItem[U = Any, V = Any, P: ContainerItem[Any, Any, Any, Any] | None = Any, C: ChildItem[Any, Any, Any, Any] | None = Any](Interface, int, metaclass=AppItemType):
    """Base class for DearPyGui item interface types. Implements the basic
    item interface protocol. Works with all items, regardless of the associated
    item's implementation type (e.g. the item's type in DearPyGui's source code).
    As such, it is used to create an interface for items whose type is not
    known or when a more concrete interface type does not exist.

    Interfaces are created like normal Python objects. The constructor accepts
    an optional `tag` positional-or-keyword argument which can be an item's
    identi


    Subclassing :py:class:`AppItem` (directly or indirectly)
    conflicts. For subclassing, it's recommended
    to use the more concrete :py:class:`ContainerItem` and :py:class:`ChildItem`
    classes instead.

    """
    @classmethod
    def create(cls, /, *, tag: Item = ..., **kwargs) -> Self:
        """Dedicated constructor method for DearPyPixl interface
        objects. Calling this method creates a new item and interface.
        The interface is returned.

        In most cases, user-defined subclasses should override this method
        in place of `__new__()` and/or `__init__()`.

        :raises `SystemError`: DearPyGui-related error.
        """
    def destroy(self, /) -> None:
        """Dedicated destructor method for DearPyPixl interface
        objects. At minimum, calling this method sets the interface in
        an unusable state and deletes the associated item (if any).
        This method should not throw an error even if the item and/or
        interface has already been destroyed.

        The default implementation of this method is roughly equivelent
        to `dearpygui.delete_item(self)` but suppresses any `SystemError`
        thrown by DearPyGui. In most cases, user-defined subclasses should
        override this method to clean up any resource created as a result
        of :py:meth:`create()`.
        """
    def exists(self, /) -> bool:
        """Return `True` if a DearPyGui item currently exists whose integer
        identifier matches the integer value of this interface.

        If this method returns `False`, the bound interface is considered to
        be in an unstable state — nearly any method call or property access
        attempt will result in `SystemError`.
        """
    @property
    def tag(self, /) -> Item:
        """**[*get*]** the associated item's unique integer or string
        identifier (integer by default)."""
    @property
    def uuid(self, /) -> int:
        """**[*get*]** the associated item's unique integer identifier."""
    @property
    def alias(self, /) -> str | None:
        """**[*get*, *set*, *del*]** the associated item's unique string
        identifier.

        :raises `SystemError`: DearPyGui-related error.
        """
    @alias.setter
    def alias(self, value: str | None, /) -> None: ...
    @alias.deleter
    def alias(self, /) -> None: ...
    @property
    def label(self, /) -> str | None:
        """**[*get*, *set*, *del*]** the associated item's informal name.
        Some items use this as their display name when rendered.

        Deleting the attribute sets it to `None` instead.

        :raises `SystemError`: DearPyGui-related error.
        """
    @label.setter
    def label(self, value: str | None, /) -> None: ...
    @label.deleter
    def label(self, /) -> None: ...
    @property
    def user_data(self, /) -> U | Any:
        """**[*get*, *set*, *del*]** the associated item's user data.

        Deleting the attribute sets it to `None` instead.

        :raises `SystemError`: DearPyGui-related error.
        """
    @user_data.setter
    def user_data(self, value: U | None, /) -> None: ...
    @user_data.deleter
    def user_data(self, /) -> None: ...
    @property
    def use_internal_label(self, /) -> bool: ...
    @use_internal_label.setter
    def use_internal_label(self, value: bool, /) -> None: ...
    @overload
    def delete(self, /) -> None: ...
    @overload
    def delete(self, /, *, children_only: bool, slot: Literal[-1, 0, 1, 2, 3] = -1) -> None:
        """Destroy the item associated with the interface, or associated
        item's children.

        Similar to `dearpygui.delete_item(self, children_only=children_only, slot=slot)`.

        **NOTE**: It is recommended to use :py:meth:`destroy()` over this method
        in most contexts since it not only deletes the item, but also frees the
        state and resources used by user-derived interfaces.

        :type children_only: `bool`
        :param children_only: If `True`, the associated item's children
            will be destroyed but not the item itself.

        :type slot: `Literal[-1, 0, 1, 2, 3]` (optional)
        :param slot: When *children_only* is `True`, this indicates the target
            child slot that will be emptied. The value must be the index of the
            target slot (`0`, `1`, `2`, or `3`) or `-1` to empty all slots. Defaults
            to `-1`.

        :raises `SystemError`: DearPyGui-related error.
        """
    def configure(self, *, label: str | None = ..., user_data: U | None = ..., use_internal_label: bool = ..., **kwargs) -> None:
        """Update the item associated with the interface.

        Similar to `dearpygui.configure_item(self, **kwargs)`.

        :raises `SystemError`: DearPyGui-related error.
        """
    def configuration(self, /) -> dict[Literal["label", "use_internal_label", "user_data"] | str, Any] | Any:
        """Return the associated item's settings.

        Similar to `dearpygui.get_item_configuration(self)`.

        :raises `SystemError`: DearPyGui-related error.
        """
    def information(self, /) -> _ItemInfoDict:
        """Return various information of the associated item.

        Similar to `dearpygui.get_item_info(self)`.

        :raises `SystemError`: DearPyGui-related error.
        """
    @property
    def pos(self, /) -> Array[int, Literal[2]]:
        """[**get**] the x and y coordinates of the item's top-left corner.
        Returns `[0, 0]` for items without geometry.
        """
    def state(self, /) -> _ItemStateDict:
        """Return the associated item's state(s).

        Similar to `dearpygui.get_item_state(self)`.

        :raises `SystemError`: DearPyGui-related error.
        """
    @overload
    def children(self, /, slot: Literal[-1] = ...) -> dict[Literal[0, 1, 2, 3], list[Item]]:
        """Return the associated item's child slots as returned via
        `dearpygui.get_item_children(self, -1)`.

        Similar to `dearpygui.get_item_children(self, slot)`.

        :type slot: `Literal[-1]`
        :param slot: Defaults to `-1`.

        :raises `SystemError`: DearPyGui-related error.
        """
    @overload
    def children(self, /, slot: Literal[0, 1, 2, 3]) -> list[ChildItem]:
        """Return the item's children in the specified slot as
        :py:class:`ChildItem` interfaces.

        Similar to `dearpygui.get_item_children(self, slot)`.

        :type slot: `Literal[0, 1, 2, 3]`
        :param slot: Index of the child slot to return.

        :raises `SystemError`: DearPyGui-related error.
        """
    def focus(self, /) -> None:
        """Sets focus to the item.

        Similar to `dearpygui.focus_item(self)`.

        :raises `SystemError`: DearPyGui-related error.
        """
    @property
    def parent(self, /) -> P:
        """**[*get*]** the item's direct parent.

        Similar to `dearpygui.get_item_parent(self)`

        :raises `SystemError`: DearPyGui-related error.
        """
    @property
    def parents(self, /) -> Sequence[ContainerItem]:
        """**[*get*]** the list of parent items from the item's root. The
        first and last item(s) in the list will be this item's root
        and direct parents, respectively.

        :raises `SystemError`: DearPyGui-related error.
        """
    @property
    def root_parent(self, /) -> ContainerItem | None:
        """**[*get*]** the item's top-level parent.

        :raises `SystemError`: DearPyGui-related error.
        """
    @property
    def theme(self, /) -> mvTheme | None:
        """**[*get*, *set*, *del*]** the item's theme. Colors and styles in
        the theme are propegated to the item's children.

        Deleting the attribute sets it to `None` instead.

        Similar to `dearpygui.get_item_info(self)["theme"]`

        :raises `SystemError`: DearPyGui-related error.
        """
    @theme.setter
    def theme(self, value: mvTheme | Item | None, /) -> None: ...
    @theme.deleter
    def theme(self, /) -> None: ...
    @property
    def font(self, /) -> mvFont | None:
        """**[*get*, *set*, *del*]** the item's font. Fonts are propegated to
        the item's children.

        Deleting the attribute sets it to `None` instead.

        Similar to `dearpygui.get_item_info(self)["font"]`

        :raises `SystemError`: DearPyGui-related error.
        """
        ...
    @font.setter
    def font(self, value: mvFont | Item | None, /) -> None: ...
    @font.deleter
    def font(self, /) -> None: ...
    @property
    def handlers(self, /) -> mvItemHandlerRegistry | None:
        """**[*get*, *set*, *del*]** the item's event handler registry.

        Deleting the attribute sets it to `None` instead.

        Similar to `dearpygui.get_item_info(self)["handlers"]`

        :raises `SystemError`: DearPyGui-related error.
        """
    @handlers.setter
    def handlers(self, value: mvItemHandlerRegistry | Item | None, /) -> None: ...
    @handlers.deleter
    def handlers(self, /) -> None: ...
    @property
    def value(self, /) -> V:
        """**[*get*, *set*]** the associated item's or interface's value.

        :raises `SystemError`: DearPyGui-related error.
        """
    @value.setter
    def value(self, value: V, /) -> None: ...
    def __new__(cls, /, tag: Item | Literal[0]) -> Self: ...
    def __repr__(self, /) -> str: ...
    def __int__(self, /) -> int:
        """
        :rtype: `int`
        :return: The associated item's unique identifier.
        """
    @final
    def __bool__(self, /) -> bool: ...


class ChildItem[U = Any, V = Any, P: ContainerItem[Any, Any, Any, Any] = Any, C: ChildItem[Any, Any, Any, Any] | None = Any](AppItem[U, V, P, C]):
    """An item that cannot exist without a parenting item. Some children
    require specific types of parents.
    """
    def move(self, /, *, parent: Item = 0, before: Item = 0) -> None:
        """Relocate the item.

        Similar to `dearpygui.move_item(self, parent=parent, before=before)`.

        :type parent: `int | str`
        :param parent: Container to parent this item. When null, the
            item's parent will not change. Note that changing the item's
            parent is processed prior to processing the *before* argument.
            Defaults to `0`.

        :type before: `int | str`
        :param before: Child item of this item's parent — this item will
            be placed before that item (inserted before the child of the
            appropriate child slot owned by the parent). Note that the target
            child slot for this item and the referenced child must match. When
            null, this item will be added as the parent's newest child (appended
            to the end of the appropriate child slot owned by the parent).

        :raises `SystemError`: DearPyGui-related error.
        """
    def move_up(self, /) -> None:
        """Move the item up, or back one position in the child slot
        that contains it.

        :raises `SystemError`: DearPyGui-related error.
        """
    def move_down(self, /) -> None:
        """Move the item down, or forward one position in the child
        slot that contains it.

        Similar to `dearpygui.move_item_down(self)`.

        :raises `SystemError`: DearPyGui-related error.
        """
    def unstage(self, /) -> None:
        """Remove this item from its stage parent and move it to the
        item currently atop the container stack.

        The child's current parent must be a `myAppItemType::mvStage`
        item. Additionally, the container stack cannot be empty.
        Finally, the top-most item on the container stack must be a
        suitable parent for the item.

        Similar to `dearpygui.unstage_item(self)`.

        :raises `SystemError`: DearPyGui-related error.
        """


class ContainerItem[U = Any, V = Any, P: ContainerItem[Any, Any, Any, Any] | None = Any, C: ChildItem[Any, Any, Any, Any] = Any](AppItem[U, V, P, C]):
    """An item that can parent other items. Some child items require
    specific types of parents.

    Containers are supported by the `with` statement — pushing the
    associated item into DearPyGui's container stack and popping
    the stack as the statement exits.

    :vartype __item_index_slot__: `ClassVar[Literal[0, 1, 2, 3]]`
    :var __item_index_slot__: The child slot index affected by
        the `__getitem__` and `__setitem__` methods. This is `1` for
        most containers and `2` for drawing containers.

        Can be changed via subclassing to have `__getitem__` and
        `__setitem__` target a different slot.

    :vartype __item_index_type__: `ClassVar[type[ChildItem]]`
    :var __item_index_type__: The item interface type used to
        wrap children returned by `__getitem__`. This is
        :py:class:`ChildItem` by default, but containers with limited
        pools of children (like handler registries) may use a more
        applicable interface type.

        Can be set to a different value via subclassing.

    """
    def __enter__(self, /) -> Self: ...
    @overload
    def __exit__(self, exc_type: None = ..., exc_value: None = ..., traceback: None = ..., /) -> Any: ...
    @overload
    def __exit__[E: BaseException](self, exc_type: type[E], exc_value: E, traceback: types.TracebackType, /) -> Any: ...
    __item_index_slot__: ClassVar[Literal[0, 1, 2, 3]]
    __item_index_type__: ClassVar[type[ChildItem]]
    @overload
    def __getitem__(self, index: SupportsIndex, /) -> C: ...
    @overload
    def __getitem__(self, slice: slice, /) -> list[C]: ...
    @overload
    def __delitem__(self, index: SupportsIndex, /) -> None: ...
    @overload
    def __delitem__(self, slice: slice, /) -> None: ...
    def index(self, item: Item, /, *, slot: Literal[0, 1, 2, 3, -1, -2, -3, -4] | None = ...) -> int:
        """Get the position of *item* within the specified child slot.

        :type item: `Item`
        :param item: Child item identifier.

        :type slot: `Literal[0, 1, 2, 3, -1, -2, -3, -4] | None` (optional)
        :param slot: Index (positive or negative) of the child slot to check.
            When `None`, all child slots will be checked. Defaults to `None`.

        :raises `IndexError`: *slot* is not a valid child slot index.

        :raises `ValueError`: *item* is not not parented by this container,
            or is not in the specified child slot.

        :raises `SystemError`: DearPyGui-related error.
        """
    def insert(self, index: SupportsIndex, item: Item, /, slot: Literal[0, 1, 2, 3, -1, -2, -3, -4] | None = ...) -> None:
        """Move *item* to this container, positioning it at *index* within
        the appropriate child slot.

        Similar to
        ```python
        parent = self
        before = dearpygui.get_item_children(parent, slot)[index]
        dearpygui.move_item(item, parent=parent, before=before)
        ```

        :type index: `SupportsIndex`
        :param index: Position of *item* in the child slot.

        :type item: `Item`
        :param item: Identifier of the child item to move.

        :type slot: `Literal[0, 1, 2, 3, -1, -2, -3, -4] | None` (optional)
        :param slot: Index (positive or negative) of the child slot *item*
            will be stored in. Note that the correct slot is determined
            automatically when unspecified, but must query DearPyGui to do so.
            Defaults to `None`.

        :raises `IndexError`: *slot* is not a valid child slot index.

        :raises `SystemError`: DearPyGui-related error.
        """
    @overload
    def reorder(self, new_order: Sequence[Item], /) -> None: ...
    @overload
    def reorder(self, slot: Literal[0, 1, 2, 3, -1, -2, -3, -4], new_order: Sequence[Item], /) -> None:
        """Re-arrange one of the container's child slots.

        Similar to `dearpygui.reorder_items(self, slot, new_order)`.

        :type slot: `Literal[0, 1, 2, 3, -1, -2, -3, -4]` (optional)
        :param slot: Index  (positive or negative) of the child slot to
            update. When not provided, the the container's
            :py:attr:`__item_index_slot__` is used as the slot index.

        :type new_order: `Sequence[Item]`
        :param new_order: All children in the child slot to update (in the
            desired order).

        :raises `IndexError`: *slot* is not a valid child slot index.

        :raises `SystemError`: DearPyGui-related error, but likely *new_order*
            is invalid.
        """


class CompositeItem:
    """A mixin class for creating interfaces of custom or complex items.

    A composite item is an item that requires one or more other items
    to function. They are the higher-level, more "complete" components
    of a user interface. The item, item dependencies, and other resources
    required by the item are created and freed via :py:meth:`create()`
    and :py:meth:`destroy()` methods, respectively.

    The state of a composite item interface is stored in their associated
    item's `user_data`. When an interface is created, it checks the item's
    `user_data` field. If the value is not a Python `dict` object, it is
    set to the interface's `__dict__` attribute. Otherwise, the interface's
    `__dict__` is set to the returned dictionary. This behavior:
    * allows users to implement their own custom item classes the way
    they typically would — implementing :py:meth:`AppItem.create()` instead
    of `__new__()` or `__init__()` is the only difference
    * removes the need to synchronize the item's state with that of a specific
    object
    * keeps the relationship between DearPyGui items and DearPyPixl
    interfaces consistent — items are stateful, interfaces are not, and any
    number of interfaces can exist for any one item
    * reduces Python reference management and object coupling — if your code can
    access the composite item's identifier, it has access your custom API just
    by creating a new interface object
    * is transparent — this class overrides :py:property:`AppItem.user_data`,
    :py:meth:`AppItem.configure()`, and :py:meth:`AppItem.configuration()` so
    your own `user_data` can be managed as normal

    Since any additional state is tied to a specific item, :py:meth:`AppItem.delete()`
    or `dearpygui.delete_item(item)` is enough to free most resources *eventually*.
    Lingering interface references may prevent Python from deallocating the state
    dictionary in a timely manner, and resources like database connections may
    remain alive longer than desired if not explicitly closed. The interface
    destructor method :py:meth:~`CompositeItem.destroy()` facilitates this clean up
    by:
    - calling the `destroy()` method (if applicable, otherwise `dearpygui.delete_item(item)`)
    on every object in the :py:attr:`components` collection
    - deleting the associated item via `dearpygui.delete_item(item)`
    - clearing the interface's state dictionary
    :py:meth:~`CompositeItem.destroy()` can be overriden as necessary.

    ***NOTE**: :py:class:`CompositeItem` is **not** a subclass of :py:class:`AppItem`.
    However, the resulting class that uses it as a base should be a subclass of
    :py:class:`AppItem`. Additionally, this solid base class should be listed before
    other :py:class:`AppItem` bases. When compile-time optimizations are disabled (e.g.
    `__debug__ = True`), a warning will be issued when creating the class with an
    incorrect order of bases, or when the resulting class is not a subclass of
    :py:class:`AppItem`.*

    ***NOTE**: The `__dict__` attribute of :py:class`ComponentItem` objects must be
    writable. This is mostly redundant, however, as a subclass cannot declare non-empty
    `__slots__` as a consequence of deriving from :py:class:`AppItem` (a subclass of
    `int`).*

    :vartype components: `Collection[AppItem | Item]`
    :var components: Other items that should be destroyed when calling
        the interface's :py:meth:`AppItem.destroy()` method. These are
        dependencies created along with the associated item and interface via
        :py:meth:`create()` that would not otherwise be destroyed when the item
        is deleted e.g. theme, handler registry, etc.
    """
    components: Collection = ()
    def __init__(self: Any, /, tag: Item = ...) -> None: ...


class SupportsValueArray[T]:
    def __len__(self: Any) -> int: ...
    def __iter__(self) -> Iterator[T]: ...
    def __reversed__(self) -> Iterator[T]: ...
    def __contains__(self: Any, value: T) -> bool: ...
    @overload
    def __getitem__(self: Any,  index: SupportsIndex, /) -> T: ...
    @overload
    def __getitem__(self: Any,  slice: slice, /) -> list[T]: ...
    @overload
    def __setitem__(self: Any,  index: SupportsIndex, value: T, /) -> None: ...
    @overload
    def __setitem__(self: Any,  index: slice, value: Sequence[T], /) -> None: ...
    def __eq__(self: Any,  other: Any, /) -> bool: ...
    def get_value(self: Any) -> list[T]: ...
    def set_value(self: Any, value: Array[T], /) -> None: ...


@final
class _ElementItem[U = Any, V: int | float = Any, P: mvThemeComponent | mvTemplateRegistry = mvThemeComponent](SupportsValueArray[V], ChildItem[U, list[V], P, None]):
    @property
    def target(self, /) -> int:
        """[**get**] the unique ID of the item attribute affected by this
        theme color or style, e.g.
        `dearpygui.dearpygui.get_item_configuration(self)["target"]`.
        """
    @property
    def category(self, /) -> int:
        """[**get**] the theme color's or style's category ID, e.g.
        `dearpygui.dearpygui.get_item_configuration(self)["category"]`.
        """
    def identify(self, /) -> tuple[type[mvThemeColor | mvThemeStyle], str, str, str, str]:
        """Return a 4-tuple containing: the item's resolved interface type, the
        element's simplified name, the element's full name, the element category
        name, and element target name. The "simplified" name matches the name of
        a function in either the :py:module:~`dearpypixl.color` or
        :py:module:~`dearpypixl.style` modules, while the element's full name,
        category name, and target name match the name of a constant in
        `dearpygui.dearpygui`.
        """

@final
class _HandlerItem[U = Any, P: mvHandlerRegistry | mvItemHandlerRegistry | mvTemplateRegistry | mvStage = Any](ChildItem[U, None, P, None]):
    @property
    def callback(self, /) -> ItemCallback | None: ...
    @callback.setter
    def callback(self, value: ItemCallback | None, /) -> None: ...
    @callback.deleter
    def callback(self, /) -> None: ...
    @property
    def show(self, /) -> bool: ...
    @show.setter
    def show(self, value: bool, /) -> None: ...
