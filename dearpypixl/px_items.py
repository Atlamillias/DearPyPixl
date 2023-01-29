import inspect
import functools
from dearpygui import (
    dearpygui,
    _dearpygui,
)
from .px_typing import (
    # typing
    overload,
    Any,
    Callable,
    Generic,
    Literal,
    TypeVar,
    Sequence,
    Self,
    # px_typing
    T, P,
    ItemId,
    Array,
    DPGTypeId,
    DPGCommand,
    DPGCallback,
    DPGItemConfig,
    DPGItemInfo,
    DPGItemState,
    DPG_STATES_DICT
)
from . import px_utils
from .px_utils import (
    get_config,
    get_info,
    get_state,
    get_value,
    set_config,
    set_value,
    generate_uuid,
)


__all__ = [
    # bases/mixins
    "AppItemType",
    "PositionedItem",
    "SizedItem",
    "ValueAbleItem",
    "ValueArrayItem",
    "CallableItem",
    "HandlerItem",
    "ContainerItem",
    "WindowItem",
    "RootItem",
    "RegistryItem",

    # functions
    "type_from_callable",
]


dearpygui.create_context()


########################################
########## MEMBER DESCRIPTORS ##########
########################################

_GT = TypeVar("_GT")
_ST = TypeVar("_ST")

class DPGProperty:
    __slots__ = ("_key")

    def __init__(self, key: str = None):
        self._key = key

    def __set_name__(self, cls, name: str):
        self._key = self._key or name


class Config(Generic[_GT, _ST], DPGProperty):
    __slots__ = ()

    def __get__(self, inst: 'AppItemType', cls) -> _GT | Self:
        try:
            return inst.configuration()[self._key]
        except (TypeError, SystemError):
            if inst is None:
                return self
            raise

    def __set__(self, inst: 'AppItemType', value: _ST) -> None:
        eval(f"inst.configure({self._key}=value)")  # no dict/unpacking


class Info(Generic[_GT], DPGProperty):
    __slots__ = ()

    def __get__(self, inst: 'AppItemType', cls) -> _GT | Self:
        try:
            return inst.information()[self._key]
        except (TypeError, SystemError):
            if inst is None:
                return self
            raise


class State(Generic[_GT], DPGProperty):
    __slots__ = ()

    def __get__(self, inst: 'AppItemType', cls) -> _GT | Self:
        try:
            key = self._key
            return inst.state().get(key, None) or DPG_STATES_DICT[key]
        except (TypeError, SystemError):
            if inst is None:
                return self
            raise


###########################################
######### APPITEM METACLASS STUFF #########
###########################################

def _null_command(*args, tag: ItemId | None = None, **kwargs) -> ItemId:
    return tag

def _metadata_conflict_check(command, identity, *bases: Sequence[type['AppItemType']]) -> bool:
    """Return True if using *bases* to create a new itemtype would cause
    a functional conflict.
    """
    try:
        bases = [b for b in bases if issubclass(b, AppItemType)]
    except NameError:  # AppItemBase
        return False
    # The command/identity must be identical (or the default) between all bases
    # and the new type's namespace.
    commands = {b.command for b in bases}
    commands.add(command)
    commands.discard(_APPITEMT_COMMAND)
    identities = {b.identity for b in bases}
    identities.add(identity)
    identities.discard(_APPITEMT_IDENTITY)
    return any(len(s) > 1 for s in (commands, identities))


_APPITEMT_COMMAND  = _null_command
_APPITEMT_IDENTITY = _dearpygui.mvAll, "mvAppItem",


class AppItemMeta(type):
    identity: DPGTypeId
    command : DPGCommand

    def __new__(
        mcls,
        name     : str,
        bases    : tuple[type[object], ...],
        namespace: dict[str],
         *,
        command : DPGCommand = None,
        identity: DPGTypeId  = None,
        **kwargs
    ):
        command   = namespace.get("command", command)
        identity  = namespace.get("identity", identity)
        type_kwds = command, identity
        # This framework heavily abuses multiple inheritance. It's possible that the new
        # type may inherit key attributes from different, yet incomplete itemtype bases.
        # Since these attributes may conflict, setup for a new "complete" itemtype is only
        # executed if all key attrs/args are included together when defining the new class,
        # and NOT just "exist" together through inheritance.
        if all(type_kwds):
            # Ensure that the special keywords/attributes are appropriate.
            if not callable(command):
                raise TypeError("`callable` is not callable.")
            try:
                _, _ = identity
            except TypeError:
                raise TypeError("`identity` must a 2-tuple containing an interger and string.") from None
            namespace["identity"] = identity
            namespace["command"]  = staticmethod(command) if not isinstance(
                                    command, staticmethod) else command
            cls = super().__new__(mcls, name, bases, namespace, **kwargs)

            # Edit class signature to include command parameters.
            cmd_sig    = inspect.signature(command)
            cls_params  = (
                inspect.Parameter(name="cls", kind=inspect.Parameter.POSITIONAL_OR_KEYWORD),
                *cmd_sig.parameters.values()
            )
            cls.__signature__ = cmd_sig.replace(parameters=cls_params, return_annotation=Self)

            # For appropriate annotations, set a `Config` descriptor on the class
            # for each. This is skipped if the annotation exists as an attribute
            # (almost always inherited).
            for annotation in cls.__annotations__:
                # Never overwrite an existing member.
                if (annotation in cls.__signature__.parameters
                and not hasattr(cls, annotation)):
                    cfg_property = Config()
                    setattr(cls, annotation, cfg_property)
                    cfg_property.__set_name__(cls, annotation)
        # Otherwise, ensure that the new class won't have an identity crisis.
        elif _metadata_conflict_check(command or _APPITEMT_COMMAND, identity or _APPITEMT_IDENTITY, *bases):
            raise TypeError(f"could not resolve bases for {name!r}.")
        else:
            cls = super().__new__(mcls, name, bases, namespace, **kwargs)

        return cls

    def __repr__(cls) -> str:
        return f"<class {cls.__qualname__!r}>"

    def __str__(cls) -> str:
        return cls.identity[1]

    def __int__(cls) -> int:
        return cls.identity[0]



###########################################
########## APPITEMTYPE & MIXINS ###########
###########################################

class AppItemBase(int, Generic[P], metaclass=AppItemMeta):
# The "base" is split into two base classes for organizational purposes. AppItemBase
# contains only class-bound members and dunder methods. AppItemType is the actual base
# class containing the bulk API. The only direct subclass of AppItemBase should be
# AppItemType -- no exceptions.

    @overload
    def __new__(cls, *args: P.args, **kwargs: P.kwargs) -> Self: ...
    def __new__(cls, *args: P.args, tag: ItemId = 0, **kwargs: P.kwargs) -> Self:
        # XXX Assign item uuid for a future item (`__init__`) or already existing item.
        # optimized for missing tags
        if not tag:
            return super().__new__(cls, generate_uuid())

        if isinstance(tag, int):
            int_id = tag
        if not isinstance(tag, str):
            raise TypeError(f"expected int, str identifier (got {int_id})")
        # a string alias is being used; fetch the existing id or create a new one
        if _dearpygui.does_alias_exist(tag):
            int_id = _dearpygui.get_alias_id(tag)
        else:
            int_id = generate_uuid()
            _dearpygui.set_item_alias(int_id, tag)
        return super().__new__(cls, int_id)

    @overload
    def __init__(self, *args: P.args, **kwargs: P.kwargs) -> None: ...
    def __init__(self, *args: P.args, tag: ItemId = 0, **kwargs: P.kwargs) -> None:
        # XXX Create a DPG item for the item uuid generated in `__new__`.
        super().__init__()
        try:
            self.command(*args, tag=self, **kwargs)
        except SystemError:
            if not _dearpygui.does_item_exist(self):
                raise px_utils.err_create_item(self.real, self.command, *args, **kwargs) from None
            # interface w/existing item

    def __repr__(self):
        repr_str = ", ".join(
            f"{optn}={val!r}"
            for optn, val in self.configuration().items()
        )
        return f"{type(self).__qualname__}(tag={self.real!r}, parent={self.parent}, {repr_str})"

    def __getitem__(self, indexes: tuple[Literal[0, 1, 2, 3], int]):
        """Return a child of this item in a specific slot at index, via
        `self[slot, index]`.
        """
        try:
            slot, index = indexes
        except TypeError:
            raise ValueError("expected `[slot, index]`") from None
        slot = get_info(self)["children"][slot]
        return slot[index]

    def __getattr__(self, name: str) -> Any:  # fallback config getter
        try:
            return self.configuration()[name]
        except KeyError:
            raise AttributeError(
                f"{type(self).__qualname__!r} object has no attribute {name!r}."
            ) from None

    def __enter__(self) -> Self:  # dynamic class typing help
        """If this item is a container, temporarily place it atop the
        container stack.

        `TypeError` is raised if the item is not a container item.
        """
        raise TypeError

    command : DPGCommand = _APPITEMT_COMMAND
    identity: DPGTypeId  = _APPITEMT_IDENTITY

    @px_utils.classproperty
    def is_container(cls) -> bool:
        """Return True if items of this type can contain other non-root
        items."""
        # A more accurate check would be to call `is_item_container`,
        # but the item would need to exist first.
        return issubclass(cls, ContainerItem)

    @px_utils.classproperty
    def is_root_item(cls) -> bool:
        """Return True if items of this type are containers, but they themselves
        cannot be parented."""
        return issubclass(cls, RootItem)

    @px_utils.classproperty
    def is_value_able(cls) -> bool:
        """Return True if items of this type have a writable value."""
        return issubclass(cls, ValueAbleItem)

    @px_utils.classproperty
    def is_plot_item(cls) -> bool:
        """Return True if items of this type are included in DearPyGui's plotting API."""
        identity = cls.identity[1]
        return any(s in identity for s in ("Plot", "mvAnnotation"))

    @px_utils.classproperty
    def is_node_item(cls) -> bool:
        """Return True if items of this type are included in DearPyGui's node API."""
        return "Node" in cls.identity[1]

    @px_utils.classproperty
    def is_table_item(cls) -> bool:
        """Return True if items of this type are included in DearPyGui's table API."""
        return "mvTable" in cls.identity[1]

    @px_utils.classproperty
    def is_draw_item(cls) -> bool:
        """Return True if items of this type are included in DearPyGui's drawing API."""
        return "mvDraw" in cls.identity[1]

    @px_utils.classproperty
    def target_slot(cls) -> int:  # XXX `target` would conflict with some items
        """Return the index of the slot that items of this type are stored in when parented."""
        # <https://dearpygui.readthedocs.io/en/latest/documentation/container-slots.html#slots>
        str_id = cls.identity[1].split("mvAppItemType::")
        if str_id in ("mvFileExtension", "mvFontRangeHint", "mvNodeLink",
        "mvAnnotation", "mvDragLine", "mvDragPoint", "mvLegend", "mvTableColumn"):
            return 0
        elif cls.is_draw_item:
            return 2
        elif str_id == "mvDragPayload":
            return 3
        return 1  # dearpygui.get_item_info(...) includes this even for root items

    # XXX The below methods create and return a new type, or an
    # instance of a new type.
    @classmethod
    def pixlate_type(cls) -> type["PixlatedItem[P]" | Self]:
        """Create and return a subclass of this class that extends higher-level
        information-related methods and properties to return `AppItemType` instances
        where an item identifier would be returned.
        """
        return type(
            f"Pyxlated{cls.__qualname__.replace('mv', '')}", (PixlatedItem, cls), {}
        )

    @classmethod
    def template_type(cls, *args: P.args, **kwargs: P.kwargs) -> type['TemplateItem[P]' | Self]:
        """Return an instance of a newly-created template item subclass of this
        class, where its attributes are used as keyword arguments when called.
        Calling the instance will return an item instance of its superclass --
        the same class the `.template` method was originally called on to create
        the template class.

        Calling the `.template` method of a template item will return a new
        instance of the template item's class *without* creating a new template
        item class.

        Read the `TemplateItem` docstring for more information.
        """
        return type(
            f"{cls.__qualname__.replace('mv', '')}Template",
            (TemplateItem, cls),
            {},
        )(*args, **kwargs)



class AppItemType(AppItemBase, Generic[P]):
    """Provides an object-oriented interface for DearPyGui items."""

    __signature__: inspect.Signature

    label             : Config[str | None , str ] = Config()
    user_data         : Config[Any, Any ]         = Config()
    use_internal_label: Config[bool, bool]        = Config()

    parent: Info[ItemId] = Info()

    is_ok                    : State[bool       ] = State(key="ok")
    is_hovered               : State[bool | None] = State(key="hovered")                  # |
    is_active                : State[bool | None] = State(key="active")                   # |
    is_focused               : State[bool | None] = State(key="focused")                  # |
    is_clicked               : State[bool | None] = State(key="clicked")                  # |
    is_left_clicked          : State[bool | None] = State(key="left_clicked")             # |
    is_right_clicked         : State[bool | None] = State(key="right_clicked")            # |- `-> None` == unsupported state for the item
    is_middle_clicked        : State[bool | None] = State(key="middle_clicked")           # |
    is_visible               : State[bool | None] = State(key="visible")                  # |
    is_edited                : State[bool | None] = State(key="edited")                   # |
    is_activated             : State[bool | None] = State(key="activated")                # |
    is_deactivated           : State[bool | None] = State(key="deactivated")              # |
    is_deactivated_after_edit: State[bool | None] = State(key="deactivated_after_edit")   # |

    @property
    def tag(self) -> int:
        """Return the item's unique integer identifier."""
        return self.real

    @property
    def alias(self) -> str | None:
        """Return the item's unique string identifier."""
        return dearpygui.get_item_alias(self)

    def delete(self, children_only: bool = False, slot: Literal[-1, 0, 1, 2, 3] = -1) -> None:
        """Destroy this item and/or this item's children.

        Args:
            * children_only: If True, only this item's children are destroyed, and
            only those in *slot*. Default is False.

            * slot: If *children_only* is True, items in this slot are destroyed.
            Default is -1 (all slots).

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        _dearpygui.delete_item(self, children_only=children_only, slot=slot)

    @overload
    def configure(self, *, label: str = ..., show: bool = ..., user_data: Any = ..., use_internal_label: bool = ..., **config) -> None: ...
    def configure(self, **kwargs) -> None:
        """Update the item's writable settings.

        Args:
            * label: Display name for the item.

            * show: If False, hide the item from the user interface. Can be used
            to deactivate or disable some items likr registries, handlers, etc.

            * user_data: Any object. Uses are user-implemented.

            * use_internal_label: If True, '##self.tag' is appended to *label*. This
            change is hidden where *label* would be displayed in the user interface.

            Other keyword-only arguments vary between items.

        The available configuration options for an item are not made apparent.
        Many of the keyword arguments used by the item type's constructor/initializer
        are writable. Common keyword arguments `parent`, `tag`, and `default_*` cannot
        be updated this way. If a `default_*` argument is used by the item type's
        constructor/initializer, it can likely be updated using the `set_value` method.

        `TypeError` is raised if this item exists and its configuration could
        not be updated. `SystemError` is raised in all other cases where this
        call to DearPyGui fails.
        """
        try:
            set_config(self, **kwargs)
        except SystemError:
            if _dearpygui.does_item_exist(self):
                raise TypeError(
                    f"Error configuring {type(self).__qualname__!r} instance. Verify that the arguments are appropriate."
                ) from None
            raise

    def configuration(self) -> DPGItemConfig:
        """Return the item's various settings.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        # `get_item_configuration` can include keys that aren't always used by
        # the item, so `eval("repr(self)")` would throw an error.
        # Filtering these out doesn't completely fix it for all items, though.
        params = self.__signature__.parameters
        return {k:v for k, v in get_config(self).items() if k in params}

    def information(self) -> DPGItemInfo:
        """Return details about the item.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        return get_info(self)

    def state(self) -> DPGItemState:
        """Return the item's status.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        return get_state(self)

    @overload
    def children(self) -> dict[Literal[0, 1, 2, 3], list[ItemId]]: ...
    @overload
    def children(self, slot: Literal[0, 1, 2, 3]) -> list[ItemId]: ...
    def children(self, slot: Literal[-1, 0, 1, 2, 3] = -1) -> dict[Literal[0, 1, 2, 3], list[ItemId]] | list[ItemId]:
        """Return one or all slots containing the item's children.

        Args:
            * slot: The slot to return. Default is -1 (all slots).

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        # if the item isn't a container everything will be empty
        return dearpygui.get_item_children(self, slot)

    def move(self, parent: ItemId = 0, before: ItemId = 0) -> None:
        """Move this non-root item to another container item and/or before another
        item.

        Args:
            * parent: The unique identifier of the container item that will serve as
            this item's parent. Default is 0 (do not re-parent).

            * before: The unique identifier of an item parented by *parent*, or this
            item's current parent if *parent* is 0. This item will be inserted before
            it in the same slot. This item must be appropriate for the slot. Default
            is 0 (append to the end of the appropriate slot, or "add normally").

        `TypeError` is raised if this item is a root item. `SystemError` is raised
        in all other cases where this call to DearPyGui fails.
        """
        _dearpygui.move_item(self, parent=parent, before=before)

    def move_up(self) -> None:
        """In the slot that contains this item, swap the positions of this non-root
        item and the item that preceeds it.

        `TypeError` is raised if this item is a root item. `SystemError` is raised
        in all other cases where this call to DearPyGui fails.
        """
        _dearpygui.move_item_up(self)

    def move_down(self) -> None:
        """In the slot that contains this item, swap the positions of this non-root
        item and the item that follows it.

        `TypeError` is raised if this item is a root item. `SystemError` is raised
        in all other cases where this call to DearPyGui fails.
        """
        _dearpygui.move_item_down(self)

    def unstage(self) -> None:
        """Move this non-root item from the stage container item parenting it to the
        item atop the container stack.

        `TypeError` is raised if this item is a root item. `SystemError` is raised if
        this item is not parented by a stage container, and in all other cases where
        this call fails.
        """
        _dearpygui.unstage(self)

    def reorder(self, slot: Literal[0, 1, 2, 3], new_order: Sequence[ItemId]) -> None:
        """Rearrange the item's children within a chosen slot.

        Args:
            * slot: Index of the target slot.

            * new_order: The new order of the item's children. The sequence
            must contain the identifiers of **all** items in the target slot.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        _dearpygui.reorder_items(self, slot, new_order)

    def focus(self) -> None:
        """Focus the item.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        _dearpygui.focus_item(self)

    @property
    def value(self) -> Any:
        """Return the item's stored value."""
        return self.get_value()
    @value.setter
    def value(self, value: Any) -> None:
        self.set_value(value)

    def get_value(self) -> Any:
        """Return the item's value.

        This will always return None if the item cannot store a value.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        return get_value(self)

    def set_value(self, value: Any) -> None:
        """Update the item's value.

        Args:
            * value: The new value to apply to the item. The type of *value*
            varies between items. Does not raise an error if the item cannot
            hold a value.

        Does nothing if the item cannot store a value.

        `SystemError` is raised if the value's type is not appropriate for the
        item, and in all other cases where this call to DearPyGui fails.
        """
        set_value(self, value)

    @property
    def theme(self) -> ItemId | None:
        """Return the item's bound theme."""
        return self.get_theme()
    @theme.setter
    def theme(self, value: ItemId) -> None:
        return self.set_theme(value)

    def get_theme(self) -> ItemId | None:
        """Return the item's bound item handler registry.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        return self.information()["theme"]

    def set_theme(self, theme: ItemId = 0) -> None:
        """Bind this item to a theme item.

        Args:
            * theme: A theme item's unique identifier. Default is 0 (unbind this item
            from the currently bound theme item if applicable).

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        _dearpygui.bind_item_theme(self, theme)

    @property
    def handlers(self) -> ItemId | None:
        """Return the item's bound item handler registry."""
        return self.get_handlers()
    @handlers.setter
    def handlers(self, value: ItemId) -> None:
        return self.set_handlers(value)

    def get_handlers(self) -> ItemId | None:
        """Return the item's bound item handler registry.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        # XXX currently works for an unofficial DPG build -- pending PR to main
        return self.information().get("handlers", None)

    def set_handlers(self, handler_registry: ItemId = 0) -> None:
        """Bind this item to a item handler registry item.

        Args:
            * handler_registry: A item handler registry item's unique identifier.
            Default is 0 (unbind this item from the currently bound item handler
            registry item if applicable).

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        _dearpygui.bind_item_handler_registry(self, handler_registry)

    @property
    def font(self) -> ItemId | None:
        return self.get_font()
    @font.setter
    def font(self, value: ItemId) -> None:
        self.set_font(value)

    def get_font(self) -> ItemId | None:
        """Return the item's bound font item.

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        return self.information()["font"]

    def set_font(self, font: ItemId = 0) -> None:
        """Bind this item to a font item.

        Args:
            * font: A font item's unique identifier. Default is 0 (unbind this
            item from the currently bound font item if applicable).

        `SystemError` is raised in all cases where this call to DearPyGui fails.
        """
        _dearpygui.bind_item_font(self, font)

    @property
    def root_parent(self) -> ItemId:
        return self.get_root_parent()

    def get_root_parent(self) -> ItemId:
        """Return the top-most item in this item's parential tree."""
        return px_utils.get_root_parent(self)




class PositionedItem(AppItemType):
    """A rendered DearPyGui item that can have a set position."""
    is_resized          : bool            = State(key="resized")
    rect_min            : Array[int, int] = State()
    rect_max            : Array[int, int] = State()
    rect_size           : Array[int, int] = State()
    content_region_avail: Array[int, int] = State()

    @property
    def pos(self) -> Array[int, int]:
        return self.state()["pos"]
    @pos.setter
    def pos(self, value: Array[int, int]) -> None:
        self.configure(pos=value)


class SizedItem(PositionedItem):
    """A rendered DearPyGui item with a bounding box. Can be resized."""

    # Every item with `pos` has sizing support. However, they are not
    # always configured through the `width` and `height` keywords. This
    # covers the common case.

    width : int = Config()
    height: int = Config()

    @property
    def rect(self) -> tuple[int, int, int, int]:
        cfg = get_config(self)
        return *self.pos, cfg["width"], cfg["height"]
    @rect.setter
    def rect(self, value: Array[int, int, int, int]) -> None:
        x, y, wt, ht = value
        set_config(self, pos=(x, y), width=wt, height=ht)




class ValueAbleItem(AppItemType):
    """A DearPyGui item that can store a value."""


class ValueArrayItem(ValueAbleItem, Generic[T]):
    """A DearPyGui item that stores an array of values."""

    def __str__(self):
        return self.get_value()

    def __add__(self, other: Any) -> Self:
        self.set_value(self.get_value().__add__(other))
        return self

    def __iadd__(self, other: Any) -> Self:
        self.set_value(self.get_value().__iadd__(other))
        return self

    def __mul__(self, other: Any) -> Self:
        self.set_value(self.get_value().__mul__(other))
        return self

    def __imul__(self, other: Any) -> Self:
        self.set_value(self.get_value().__imul__(other))
        return self

    def __setitem__(self, index: int, value: T) -> None:
        item_value = self.get_value()
        item_value.__setitem__(index, value)
        self.set_value(item_value)

    @px_utils.forward_method("get_value", call=True)
    def __getitem__(self, index: int) -> T: ...
    @px_utils.forward_method("get_value", call=True)
    def __delitem__(self, index: int): ...
    @px_utils.forward_method("get_value", call=True)
    def __contains__(self, value: T): ...
    @px_utils.forward_method("get_value", call=True)
    def __reversed__(self): ...
    @px_utils.forward_method("get_value", call=True)
    def __str__(self): ...
    @px_utils.forward_method("get_value", call=True)
    def __len__(self): ...
    @px_utils.forward_method("get_value", call=True)
    def __iter__(self): ...
    @px_utils.forward_method("get_value", call=True)
    def __bool__(self): ...
    @px_utils.forward_method("get_value", call=True)
    def __lt__(self, other: Any): ...
    @px_utils.forward_method("get_value", call=True)
    def __le__(self, other: Any): ...
    @px_utils.forward_method("get_value", call=True)
    def __gt__(self, other: Any): ...
    @px_utils.forward_method("get_value", call=True)
    def __ge__(self, other: Any): ...
    @px_utils.forward_method("get_value", call=True)
    def __eq__(self, other: Any): ...
    @px_utils.forward_method("get_value", call=True)
    def count(self, value: Any) -> int: ...
    @px_utils.forward_method("get_value", call=True)
    def index(self, value: T, start: int = 0, stop: int = None) -> int: ...

    def append(self, value: T) -> None:
        """Add *value* to the end of this item's values."""
        item_value = self.get_value()
        item_value.append(value)
        self.set_value(item_value)

    def extend(self, iterable: Sequence[T]) -> None:
        """Append values in *iterable* to this item's values."""
        item_value = self.get_value()
        item_value.extend(iterable)
        self.set_value(item_value)

    def pop(self, index: int = -1) -> T:
        """Remove and return the last value at *index*."""
        item_value = self.get_value()
        value = item_value.pop(index)
        self.set_value(item_value)
        return value

    def insert(self, index: int, value: T):
        """Insert *value* before *index*."""
        item_value = self.get_value()
        item_value.insert(index, value)
        self.set_value(item_value)

    def remove(self, value: T):
        """Remove the first occurance of *value*."""
        item_value = self.get_value()
        item_value.remove(value)
        self.set_value(item_value)

    def sort(self, *, key: Callable[[T], Any] = None, reverse: bool = False) -> None:
        """Sort values in-place."""
        item_value = self.get_value()
        item_value.sort(key=key, reverse=reverse)
        self.set_value(item_value)

    def reverse(self) -> None:
        """Reverse item values in-place."""
        self.set_value(self.get_value()[::-1])

    def get_value(self) -> list[T]:
        return get_value(self)




class CallableItem(AppItemType):
    """A DearPyGui item that supports an optional callback, which can be invoked
    by calling the item. The item can also be passed as a callback-related
    argument for other items."""

    callback: DPGCallback[P] = Config()

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> None:
        self.callback(*args, *kwargs)

    __code__ = __call__.__code__


class HandlerItem(CallableItem):
    """A DearPyGui item that fires a callback on certain events."""




class ContainerItem(AppItemType):
    """A DearPyGui item that can contain other items."""

    def __enter__(self) -> Self:
        self.push_stack()
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.pop_stack()

    def push_stack(self) -> None:
        _dearpygui.push_container_stack(self)

    def pop_stack(self) -> bool:
        if _dearpygui.top_container_stack() == self:
            _dearpygui.pop_container_stack()
            return True
        return False


class WindowItem(ContainerItem):  # AFAIK "mvWindowAppItem" and "mvChildWindow" only
    """A DearPyGui container item that supports scrolling on both axis."""

    x_scroll_max: float = property(
        lambda self:_dearpygui.get_x_scroll_max(self),
        doc="Return the end horizontal scroll position."
    )
    x_scroll_pos: float = property(
        lambda self:_dearpygui.get_x_scroll(self),
        lambda self, value: _dearpygui.set_x_scroll(self, value),
        doc="Get/set the horizontal scroll position of the item."
    )
    y_scroll_max: float = property(
        lambda self:_dearpygui.get_y_scroll_max(self),
        doc="Return the end vertical scroll position."
    )
    y_scroll_pos: float = property(
        lambda self:_dearpygui.get_y_scroll(self),
        lambda self, value: _dearpygui.set_y_scroll(self, value),
        doc="Get/set the vertical scroll position of the item."
    )


class RootItem(ContainerItem):
    """A top-level DearPyGui container item. It cannot be parented."""

    def move(self, *args, **kwargs) -> TypeError:
        raise TypeError(f"{type(self).__qualname__} item cannot be moved.")

    move_up   = move
    move_down = move
    unstage   = move


class RegistryItem(RootItem):
    """A top-level DearPyGui container item. It cannot be parented, and
    it (and its child items) are not typically rendered."""




_ITEM_TO_CONST = {
    # inferred_item_name   : dpg_constant_name         -> logical_output           (the_problem)
    "2d_histogram_series"  : "mv2dHistogramSeries",  # -> "mv3DHistogramSeries"    ("d" needs to be lowercase)
    "3d_slider"            : "mvSlider3D",           # -> "mv3DSlider"             (uniquely named)
    "hline_series"         : "mvHLineSeries",        # -> "mvHlineSeries"          ("l" needs to be uppercase)
    "vline_series"         : "mvVLineSeries",        # -> "mvVlineSeries"          ("l" needs to be uppercase)
    "plot_annotation"      : "mvAnnotation",         # -> "mvPlotAnnotation"       (remove "Plot")
    "subplots"             : "mvSubPlots",           # -> "mvSubplots"             ("p" needs to be uppercase)
    "text_point"           : "mvLabelSeries",        # -> "mvTextPoint"            (completely different name)
    "draw_rectangle"       : "mvDrawRect",           # -> "mvDrawRectangle"        (drop "angle")
    "draw_image_quad"      : "mvDrawQuad",           # -> "mvDrawImageQuad"        (drop "image")
    "draw_bezier_quadratic": "mvDrawBezierQuad"      # -> "mvDrawBezierQuadratic"  (drop "ratic")
}

def type_from_callable(command: DPGCommand[P, ItemId]) -> type[AppItemType[P]]:
    """Create and return a new AppItemType from a DearPyGui item-creating
    function.

    Args:
        * command: A function object that return or yield an item identifier.
        All functions that create items in the `dearpygui.dearpygui` namespace
        are supported (except `popup`).


    Details from both the function and `dearpygui.dearpygui` module are used
    to help create the class. For example, its name will mirror the item's
    internal DearPyGui type name:
    >>> # import dearpygui.dearpygui as dearpygui
    ...
    >>> Window = type_from_callable(dearpygui.window)  # or `dearpygui.add_window`
    >>> repr(Window)
    <class 'mvWindowAppItem'>

    Type information is exposed via the `.identity` class property -- as a
    2-tuple containing the type's internal enumeration value, and string
    representation as returned by `dearpygui.get_item_info(...)['type']`.
    >>> Window.identity
    (33, 'mvAppItemType::mvWindowAppItem')
    >>> Window.identity[0] == dearpygui.mvWindowAppItem
    True
    >>> dpg_wndw = dearpygui.add_window()
    >>> Window.identity[1] == dearpygui.get_item_info(dpg_wndw)['type']
    True

    Depending on the information inferred from the function and module, mixin
    classes may be included in the new class' bases. The logic is smart enough
    to, for example, include `RootItem` as a mixin for items that cannot be
    parented. This may change the result of other class properties such as
    `.is_root_item`.
    >>> Window.is_root_item  # issubclass(Window, RootItem)
    True
    >>> Window.is_container  # issubclass(Window, ContainerItem)
    True
    >>> ChildWindow = type_from_callable(dearpygui.child_window)
    >>> ChildWindow.is_root_item, ChildWindow.is_container
    (False, True)
    >>> Button = type_from_callable(dearpygui.add_button)
    >>> Button.is_root_item, Button.is_container
    (False, False)

    Mixins may extend (or limit) the available interface for the new class.
    Since `Window` is a derived `RootItem`, methods that would manage the item's
    parent will now raise a `TypeError` instead of the ambiguous `SystemError`
    thrown by DearPyGui.

    The logic that includes mixin base classes is kept minimal, and can't
    account for every possibility. Typing information on the returned class is
    generalized and will be lost when subclassing (ex.
    `class Window(type_from_callable(dearpygui.window)): ...`). For better typing
    introspection and a more "accurate" class, it is best to statically define
    the class in its entirety using the mixin classes exposed in this module
    (ex. `class Window(RootItem, AppItemType): ...`).
    """

    try:
        cmd_name = command.__qualname__
    except:
        raise TypeError("`command` argument is not valid.")
    if not px_utils.is_item_cmd(command):
        raise TypeError(f"Invalid `command` argument {cmd_name!r}.")
    if cmd_name == "popup":
        raise ValueError("Invalid `command` argument `popup` (use `window`, `add_window`).")

    is_container = False
    if px_utils.is_ctxmgr_fn(command):  # is "container command" -- get the basic function
        _name1 = f"add_{cmd_name}"
        _name2 = f"draw_{cmd_name}"
        try:
            command = getattr(dearpygui, _name1, None) or getattr(dearpygui, _name2)
        except AttributeError:
            raise ValueError(
                f"Unable to get basic item command of context manager function {cmd_name!r}."
            ) from None
        is_container = True
    else:  # is basic function -- add container support if container command exists
        _name = cmd_name
        # chaining `.removeprefix(...)` could remove more than intended
        if cmd_name.startswith("draw_"):
            _name = cmd_name.removeprefix("draw_")
        elif cmd_name.startswith("add_"):
            _name = cmd_name.removeprefix("add_")
        try:
            getattr(dearpygui, _name)
        except AttributeError:
            pass
        else:
            is_container = True

    item_name = cmd_name.removeprefix("add_")
    # DPG constants are cases as "mvColorMap" -- correct casing issue
    if item_name.startswith("colormap"):
        item_name = item_name.replace("colormap", "color_map", 1)
    # A SyntaxError could potentially be thrown IF the class were to be statically created
    # i.e. `add_3d_slider` -> "3dSlider", `add_2d_histogram` -> "2dHistogram", etc. So the
    # 'mv' (Marvel) prefix is added.
    basename = f'mv{item_name.title().replace("_", "")}'
    if basename == "mvWindow":  # sole exception to the typical function naming convention
        basename = "mvWindowAppItem"
    try:
        # item.identity[0] == dearpygui.mvConstant
        # item.identity[1] == dearpygui.get_item_info(item)["type"]
        getattr(dearpygui, basename)
    except AttributeError:
        # refer to the "this shit is weird" map
        if item_name in _ITEM_TO_CONST:
            basename = _ITEM_TO_CONST[item_name]
        # item handler?
        elif all(s in item_name for s in ("item_", "_handler")):
            basename = basename.replace("Item", "", 1)
        # x4 input item?
        elif item_name[-1] == "x":
            basename = f"{basename[:-1]}Multi"
        # panik
        else:
            raise
    identity = getattr(dearpygui, basename), f"mvAppItemType::{basename}"

    cmd_sig    = inspect.signature(command).replace(return_annotation=None)
    cmd_params = cmd_sig.parameters
    item_bases = [AppItemType,]

    # can the item support a callback?
    if "callback" in cmd_params:
        # is the non-container item a handler?
        if cmd_name.endswith("_handler") and not is_container:
            item_bases.append(HandlerItem)
        else:
            item_bases.append(CallableItem)
    # can the item store a value?
    if any(s in cmd_name for s in ("_series", "theme_color", "theme_style")):
        item_bases.append(ValueArrayItem)
    elif ("default_value" in cmd_params or any(s in cmd_name for s in ("tab_bar",))):
        item_bases.append(ValueAbleItem)
    # can the item be sized?
    if "pos" in cmd_params:
        if all(p in cmd_params for p in ("width", "height", "pos")):
            item_bases.append(SizedItem)
        else:
            item_bases.append(PositionedItem)
    # can the item parent other items?
    if is_container:
        # is the item a registry?
        if any(cmd_name.endswith(s) for s in ("_registry", "theme")):
            item_bases.append(RegistryItem)
        # can the non-registry item be parented?
        elif "parent" not in cmd_params:
            item_bases.append(RootItem)
            if basename == "mvWindowAppItem":
                item_bases.append(WindowItem)
        elif basename == "mvChildWindow":
            item_bases.append(WindowItem)
        else:
            item_bases.append(ContainerItem)
    cls: Any = type(basename, tuple(item_bases[::-1]), {}, command=command, identity=identity)  # type: ignore
    cls.__doc__ = command.__doc__
    return cls




###########################################
########### SPECIAL MIXIN TYPES ###########
###########################################

# XXX These are unique mixins that can make the resulting class a bit weird,
# instances or do unusual things.

class _PatchedItem(AppItemType):  # "do not import" indicator for genfile.py script
    ...




class PixlatedItem(_PatchedItem, Generic[P]):
    """AppItemType mixin that extends higher-level information-related methods and
    properties to return `AppItemType` instances where an item identifier would be
    returned.
    """
    @property
    def parent(self) -> ContainerItem | None:
        p_item = self.information()["parent"]
        return ContainerItem(tag=p_item) if p_item else None

    def get_font(self) -> ContainerItem | None:
        font = super().get_font()
        return ContainerItem(tag=font) if font else None

    def get_handlers(self) -> RegistryItem | None:
        hreg = super().get_handlers()
        return RegistryItem(tag=hreg) if hreg else None

    def get_theme(self) -> RegistryItem | None:
        theme = super().get_theme()
        return RegistryItem(tag=theme) if theme else None

    def get_root_parent(self) -> RootItem:
        root = super().get_root_parent()
        return RootItem(tag=root)



def _init_wrapper(mthd: Callable[P, T], *_args: P.args, **_kwargs: P.kwargs) -> Callable[[], T]:
    @functools.wraps(mthd)
    def init(*args: P.args, **kwargs: P.kwargs) -> T:
        mthd(*(args or _args), **(_kwargs | kwargs))
        mthd.__self__.__init__ = mthd
    return init

class _NullInitItemMeta(AppItemMeta):
    def __call__(cls, *args, **kwargs):
        return cls.__new__(cls, *args, **kwargs)

class NullInitItem(_PatchedItem, Generic[P], metaclass=_NullInitItemMeta):
    """`AppItemType` mixin that disables auto initialization for new instances. The
    `.__init__` method must be called manually or through other means as defined by
    the user.

    When calling the `.__init__` method, it will automatically receive any arguments
    it would have received under normal circumstances. If keyword arguments are sent
    to the `.__init__` method, they will be merged into the keyword arguments used
    when the instance was created. If positional arguments are included, only those
    positional arguments will be used and NOT the positional arguments originally
    passed on instantiation (to `.__new__`).

    NOTE: Attempting to call instance methods before calling the `.__init__` method
    may result in an error because the DearPyGui item may not exist yet. Class-bound
    descriptors will function as normal.
    """
    def __new__(cls, *args: P.args, **kwargs: P.kwargs) -> Self:
        self = super().__new__(*args, **kwargs)
        self.__init__ = _init_wrapper(self.__init__, *args, **kwargs)
        return self




def _get_non_template_type(obj: type) -> type:
    for t in obj.mro():
        if not issubclass(t, _PatchedItem):
            return t

class _TemplateItemMeta(Generic[P], AppItemMeta):
    def __new__(mcls, name: str, bases: tuple, namespace: dict[str], *args: P.args, **kwargs: P.kwargs):
        kwargs["__slots__"] = ()
        cls = super().__new__(mcls, name, bases, namespace,)
        cls.__init__    = None
        cls.__setattr__ = None
        cls.__type      = _get_non_template_type(cls)
        cls.__args      = args
        cls.__kwargs    = kwargs
        return cls

    def __call__(cls, *args: P.args, **kwargs: P.kwargs) -> Self:
        return cls._type(*(args or cls._args), **(cls._kwargs | kwargs))

    def template_type(cls, *args: P.args, **kwargs: P.kwargs):
        return cls.__type.template_type(*args, **kwargs)

class TemplateItem(_PatchedItem, Generic[P], metaclass=_TemplateItemMeta):
    """An `AppItemType` mixin that turns the class into a superclass
    factory with pre-bound arguments of the user's choosing.
    """
    def __new__(cls, *args: P.args, **kwargs: P.kwargs) -> type[Self]:
        return cls




class _AutoParentItemMeta(AppItemMeta):
    def __new__(mcls, name, bases, namespace, auto_parent: DPGCommand = None, **kwargs):
        cls = super().__new__(mcls, name, bases, namespace, **kwargs)
        if auto_parent:=namespace.get("auto_parent", auto_parent):
            if cls.is_root_item:
                raise TypeError("cannot mix `AutoParentItem` with a root item type.")
            cls.auto_parent = staticmethod(auto_parent)
        return cls

class AutoParentItem(_PatchedItem, Generic[P], metaclass=_AutoParentItemMeta):
    """An AppItemType mixin that creates a parent item for itself if one
    is not available and the container stack is empty.

    This does not check for a *compatible* parent. It will only trigger as
    a last resort -- the container stack must be empty and `parent` cannot
    be included as an argument.
    """

    auto_parent: DPGCommand = staticmethod(lambda self: 0)

    def __init__(self, *args: P.args, **kwargs: P.kwargs) -> None:
        if not kwargs.get("parent", None) and not _dearpygui.top_container_stack():
            kwargs["parent"] = self.auto_parent()
        super().__init__(*args, **kwargs)


