import typing
import inspect
import functools

from dearpygui import _dearpygui

from . import codegen
from . import parsing
from . import interface
from . import management
from . import uuidpool
from .protocols import Item, property, true

if typing.TYPE_CHECKING:
    from inspect import Signature, Parameter
    from dearpypixl.items import mvTheme, mvFont, mvItemHandlerRegistry
    from .itemtype import RootItem, ContainerItem, ContainerItemT




_ITEMTYPE_REGISTRY = interface.Interface.__itemtype_registry__




# [ `AppItemType` metaclass ]

class AppItemType(type):
    __slots__ = ()

    __itemtype_registry__: dict[str, type[typing.Any]] = _ITEMTYPE_REGISTRY
    __itemtype_identity__: tuple[int, str]

    @property
    def __itemtype_uuid__(self) -> int:
        return self.__itemtype_identity__[0]

    @property
    def __itemtype_name__(self) -> str:
        return self.__itemtype_identity__[1]

    __itemtype_info__: parsing.ItemTypeInfo | typing.Any = None

    @staticmethod
    def __itemtype_command__(*args, tag: Item = 0, **kwargs) -> Item:
        return 0

    @typing.overload
    def __eq__(self, other: typing.Any, /) -> bool: ...   # pyright: ignore[reportInconsistentOverload]
    def __eq__(self, other: typing.Any, /, *, __type_eq=type.__eq__, __isinstance=isinstance) -> bool:
        if __isinstance(other, __class__):
            try:
                return __type_eq(self, other)
            except TypeError:
                return False

        uuid, name = self.__itemtype_identity__

        if __isinstance(other, str):
            return name == other

        try:
            return uuid == other
        except TypeError:
            return False

    def __str__(self) -> str:
        return self.__itemtype_identity__[1]

    def __int__(self) -> int:
        return self.__itemtype_identity__[0]

    def __repr__(self) -> str:
        return f"<class {self.__name__!r}>"

    @classmethod
    def create(cls, /, *args, **kwargs) -> AppItem:
        raise NotImplementedError




# [ `AppItem` class ]

_LOCALS_ITEMTYPE_FUNC = {
    "__itemtype_registry__": interface.Interface.__itemtype_registry__,
    "set_item_config": _dearpygui.configure_item,
    "get_item_config": _dearpygui.get_item_configuration,
    "get_item_state": _dearpygui.get_item_state,
    "get_item_info": _dearpygui.get_item_info,
    "set_item_theme": _dearpygui.bind_item_theme,
    "set_item_font": _dearpygui.bind_item_font,
    "set_item_handlers": _dearpygui.bind_item_handler_registry,
    "acquire_lock": _dearpygui.lock_mutex,
    "release_lock": _dearpygui.unlock_mutex,
    "int": int,
    "null": None,
}


@typing.overload
def item_config_property(del_value: None = None, doc: str | None = None) -> property[typing.Any, typing.Any]: ...
@typing.overload
def item_config_property(del_value: typing.Any, doc: str | None = None) -> property[typing.Any, typing.Any, typing.Literal[True]]: ...
def item_config_property(del_value: typing.Any = None, doc: str | None = None) -> property[typing.Any, typing.Any, typing.Any]:
    def factory(name):
        if del_value is not None:
            fdel_body = f"set_item_config(self, {name}={del_value!r})"
        else:
            fdel_body = None

        prop = codegen.create_property(
            f"return get_item_config(self)['{name}']",
            f"set_item_config(self, {name}=value)",
            fdel_body,
            doc=doc,
            module=__name__,
            locals=_LOCALS_ITEMTYPE_FUNC,
        )
        prop.fget.__module__ = prop.fset.__module__ = __name__

        return prop

    return codegen.DescriptorDelegate(factory)  # type: ignore


def item_info_property(item_type: str, doc: str | None = None) -> property[typing.Any, typing.Any, typing.Any]:
    if not item_type.startswith("mvAppItemType::"):
        item_type = f"mvAppItemType::{item_type}"

    def factory(name, item_type=item_type):
        prop = codegen.create_property(
            (
                f"item = get_item_info(self)['{name}']",
                f"if item is null:",
                f"  return null",
                f"return int.__new__(__itemtype_registry__['{item_type}'], item)",
            ),
            (
                f"if value is null:",
                f"  value = 0",
                f"set_item_{name}(self, value)",
            ),
            (
                f"set_item_{name}(self, 0)",
            ),
            doc=doc,
            module=__name__,
            locals=_LOCALS_ITEMTYPE_FUNC,
        )
        prop.fget.__module__ = prop.fset.__module__ = prop.fdel.__module__ = __name__

        return prop

    return codegen.DescriptorDelegate(factory)  # type: ignore


class AppItem[U = typing.Any, V = typing.Any, P: typing.Any = typing.Any](
    interface.Interface, int, metaclass=AppItemType
):
    __slots__ = ()

    __itemtype_identity__: typing.ClassVar[tuple[int, str]] = (0, '')
    __itemtype_command__ = AppItemType.__itemtype_command__

    @property
    def __itemtype_uuid__(self) -> int:
        type_uuid = self.__itemtype_identity__[0]
        if type_uuid < 1:
            type_name = self.__itemtype_name__
            type_uuid = parsing.itemtype_info()[type_name].type_uuid
        return type_uuid

    @property
    def __itemtype_name__(self) -> str:
        return (
            self.__itemtype_identity__[1] or
            _dearpygui.get_item_info(self)["type"]
        )

    @typing.overload
    @staticmethod
    def _interface[T: "AppItem[typing.Any, typing.Any, typing.Any]"](type: type[T], tag: Item, /) -> T: ...  # pyright: ignore[reportInconsistentOverload, reportSelfClsParameterName]
    @staticmethod
    @management.initializer
    @staticmethod
    def _interface(type, tag, /, *, __int_new=int.__new__):
        return __int_new(type, tag)

    @typing.overload
    def __new__(cls, /, tag: int | str) -> typing.Self: ... # pyright: ignore[reportInconsistentOverload]
    @management.initializer
    def __new__(
        cls,
        /,
        tag: int | str,
        __isinstance=isinstance,
        __wrap_item=int.__new__,
        __int=int,
        __alloc=uuidpool.alloc,
        __set_item_alias=_dearpygui.add_alias,
        __get_item_uuid=_dearpygui.get_alias_id,
    ) -> typing.Self:
        if __isinstance(tag, __int):
            return __wrap_item(cls, tag or __alloc())

        alias = tag
        uuid  = __get_item_uuid(tag)
        if not uuid:
            __set_item_alias(alias, uuid)

        return __wrap_item(cls, uuid)

    def __repr__(self) -> str:
        uuid  = self.real
        alias = _dearpygui.get_item_alias(uuid)
        value = _dearpygui.get_value(uuid)

        if self.__class__ is __class__:
            type = _dearpygui.get_item_info(self)["type"]
            return f"{__class__.__name__}({type=}, {uuid=}, {alias=}, {value=})"

        return f"{self.__class__.__name__}({uuid=}, {alias=}, {value=})"

    def __int__(self) -> int:
        return self.real

    def __str__(self) -> str:
        return _dearpygui.get_item_alias(self) or ""

    @property
    def tag(self) -> Item:
        """[get] the associated item's unique integer or string
        identifier (integer by default)."""
        return self.real

    @property
    def uuid(self) -> int:
        """[get] the associated item's unique integer identifier."""
        return self.real

    @property
    def alias(self) -> str | None:
        """[get, set, del] the associated item's unique string identifier."""
        return _dearpygui.get_item_alias(self)
    @alias.setter
    def alias(self, value: str | None, /) -> None:
        if value is None:
            alias = _dearpygui.get_item_alias(self)
            if alias is not None:
                _dearpygui.remove_alias(alias)
        else:
            _dearpygui.set_item_alias(self, value)
    @alias.deleter
    def alias(self) -> None:
        _dearpygui.remove_alias(_dearpygui.get_item_alias(self))

    @property
    def value(self) -> V:
        """[get, set] the associated item's or interface's value."""
        return _dearpygui.get_value(self)
    @value.setter
    def value(self, value: V, /) -> None:
        _dearpygui.set_value(self, value)

    @classmethod
    def create(cls, /, *args, **kwargs) -> typing.Self:
        """Dedicated constructor method for Dear PyPixl interface
        objects. At minimum, calling this method creates a new item
        and interface. The interface is returned.

        For built-in itemtype classes, calling this method is
        roughly equivelent to
        `return cls(tag=cls.__itemtype_command__(*args, **kwargs))`.

        For stateful derived classes, this method should be overridden
        in place of `__new__()` and/or `__init__()`. Calling it should
        construct and initialize a new interface similarly to a typical
        `__init__()` implementation.

        When overriding this method, it is not necessary to delegate
        calls to the default implementation (e.g.
        `super().create(*args, **kwargs)`). In fact, doing so should
        be **avoided** when possible.
        """
        raise NotImplementedError

    def destroy(self, /) -> None:
        """Dedicated destructor method for Dear PyPixl interface
        objects. At minimum, calling this method sets the interface in
        an unusable state and deletes the associated item (if any).
        Subsequent calls do nothing.

        The default implementation is equivelent to trying
        `dearpygui.delete_item(self)` and discarding any resulting
        `SystemError`.

        For stateful derived classes, this method should be overridden
        to clean up any Python object or Dear PyGui item created as a
        result of calling :py:meth:`create()`.
        """
        try:
            _dearpygui.delete_item(self, children_only=False, slot=-1)
        except SystemError:
            pass
        return

    @typing.overload
    def delete(self, /) -> None: ...
    @typing.overload
    def delete(self, /, *, children_only: bool, slot: typing.Literal[-1, 0, 1, 2, 3] = -1) -> None: ...
    def delete(self, /, *, children_only: bool = False, slot: int = -1) -> None:
        """Destroy the item associated with the interface.
        The interface's state is otherwise unchanged.

        Similar to `dearpygui.delete_item(self, **kwargs)`.
        """
        if not children_only:
            return _dearpygui.delete_item(self, children_only=False, slot=-1)
        try:
            _dearpygui.delete_item(self, children_only=children_only, slot=slot)
        except SystemError:
            if children_only not in (0, 1, True, False):
                raise TypeError(f"`children_only` must be a boolean") from None
            if slot not in (-1, 0, 1, 2, 3):
                raise ValueError(f"`slot` must be 0, 1, 2, 3, or -1 (all child slots)") from None
            raise

    label: property[str | None, str | None] = item_config_property()
    use_internal_label: property[str | None, str | None] = item_config_property()
    user_data: property[U | typing.Any, U | typing.Any] = item_config_property()

    @typing.overload
    def configure(self, *, label: str | None = ..., user_data: typing.Any = ..., use_internal_label: bool = ..., **kwargs) -> None: ...  # pyright: ignore[reportInconsistentOverload]
    def configure(self, **kwargs):
        """Update the item associated with the interface.

        Similar to `dearpygui.configure_item(self, **kwargs)`.
        """
        _dearpygui.configure_item(self, **kwargs)

    def configuration(self, /) -> dict[typing.Literal["label", "use_internal_label", "user_data"] | str, typing.Any] | typing.Any:
        """Return the associated item's settings.

        Similar to `dearpygui.get_item_configuration(self)`.
        """
        return _dearpygui.get_item_configuration(self)

    @staticmethod
    def _get_root_parent(
        tag: Item,
        /, *,
        __get_info=_dearpygui.get_item_info,
        __acquire_lock=_dearpygui.lock_mutex,
        __release_lock=_dearpygui.unlock_mutex,
    ) -> tuple[Item | None, str]:
        item_uuid = tag
        type_name = ''

        __acquire_lock()
        try:
            while True:
                info =__get_info(item_uuid)

                parent = info["parent"]
                if parent is None:
                    break

                item_uuid = parent
                type_name = info["type"]
        finally:
            __release_lock()

        if item_uuid == tag:
            return None, type_name

        return item_uuid, type_name

    @property
    def root_parent(self) -> RootItem | None:
        """[get] the item's top-level parent."""
        item_uuid, type_name = self._get_root_parent(self)
        if item_uuid is None:
            return None

        item_type = __class__.__itemtype_registry__[type_name]
        return __class__._interface(item_type, item_uuid)

    @staticmethod
    def _get_parents(
        tag: Item,
        /, *,
        __get_info=_dearpygui.get_item_info,
        __acquire_lock=_dearpygui.lock_mutex,
        __release_lock=_dearpygui.unlock_mutex,
    ) -> list[ContainerItem]:
        parents = []
        insert_parent = parents.insert

        interface = __class__._interface
        registry = __class__.__itemtype_registry__

        item_uuid = tag

        __acquire_lock()
        try:
            while True:
                info =__get_info(item_uuid)

                parent = info["parent"]
                if parent is None:
                    break

                item_uuid = parent
                type_name = info["type"]
                insert_parent(0, interface(registry[type_name], item_uuid))
        finally:
            __release_lock()

        return parents

    @property
    def parents(self) -> typing.Sequence["ContainerItem" | P | typing.Any]:
        """[get] the list of parent items from the item's root. The
        first and last item(s) in the list will be this item's root
        and direct parents, respectively.
        """
        return self._get_parents(self)

    @property
    def parent(self) -> P:
        """[get] the item's direct parent."""
        item = _dearpygui.get_item_info(self)["parent"]
        if item is None:
            return None  # pyright: ignore[reportReturnType]

        type_name = _dearpygui.get_item_info(item)["type"]
        item_type = __class__.__itemtype_registry__[type_name]

        return __class__._interface(item_type, item)

    theme: property[mvTheme | None, Item | None, true] = item_info_property(
        "mvTheme",
        "[get, set, del] the item's theme. Colors and styles in the theme "
        "are propegated to the item's children.\n\nNote that `del item.theme` "
        "is equivelent to `item.theme = None`."
    )
    font: property[mvFont | None, Item | None, true] = item_info_property(
        "mvFont",
        "[get, set, del] the item's font. Fonts are propegated to the item's "
        "children.\n\nNote that `del item.font` is equivelent to `item.font = None`."
    )
    handlers: property[mvItemHandlerRegistry | None, Item | None, true] = item_info_property(
        "mvItemHandlerRegistry",
        "[get, set, del] the item's event handler registry.\n\nNote that "
        "`del item.font` is equivelent to `item.font = None`."
    )

    def information(self, /) -> interface.ItemInfoDict:
        """Return various information of the associated item.

        Similar to `dearpygui.get_item_info(self)`.
        """
        return _dearpygui.get_item_info(self)  # pyright: ignore[reportReturnType]

    @typing.overload
    def children(self, /, slot: typing.Literal[-1] = ...) -> dict[typing.Literal[0, 1, 2, 3], list[Item]]: ...
    @typing.overload
    def children(self, /, slot: typing.Literal[0, 1, 2, 3]) -> list["AppItem"]: ...
    def children(self, /, slot=-1):
        """Return the associated item's children.

        Similar to `dearpygui.get_item_children(self, *args, **kwargs)`.
        """
        items = _dearpygui.get_item_info(self)["children"]
        if slot == -1:
            return items

        interface = __class__._interface
        return [interface(__class__, i) for i in items[slot]]

    def state(self, /) -> typing.Any | interface.ItemStateDict:
        """Return the associated item's state(s).

        Similar to `dearpygui.get_item_state(self)`.
        """
        return _dearpygui.get_item_state(self)  # pyright: ignore[reportReturnType]

    def focus(self, /) -> None:
        """Set focus to the associated item. Does nothing if the
        item cannot be rendered.

        Similar to `dearpygui.focus_item(self)`.
        """
        _dearpygui.focus_item(self)

    @staticmethod
    def _get_child_slot_target(type_name: str, /) -> typing.Literal[0, 1, 2, 3]:
        type_name = type_name.removeprefix("mvAppItemType::")
        match type_name:
            case (
                "mvFileExtension" |
                "mvFontRangeHint" |
                "mvNodeLink" |
                "mvAnnotation" |
                "mvDragLine" |
                "mvDragPoint" |
                "mvLegend" |
                "mvTableColumn"
            ):
                return 0
            case "mvAppItemType::mvDragPayload":
                return 3
            case _ if type_name.startswith("mvDraw"):
                return 2
            case _:
                return 1

    def child_slot_target(self) -> typing.Literal[0, 1, 2, 3] | None:
        """Return the index of the child slot the associated item
        is in."""
        item_info = _dearpygui.get_item_info(self)

        if item_info["parent"] is None:
            return None

        return __class__._get_child_slot_target(item_info["type"])




# [ `build()` function ]

def _update_method_metadata[T: typing.Callable](cls: type, name: str, method: T, signature: Signature | None = None) -> T:
    method.__name__ = name
    method.__qualname__ = f"{cls.__qualname__}.{name}"
    method.__module__ = cls.__module__
    if signature is not None:
        method.__signature__ = signature  # type: ignore
    return method


def _build_create_method(cls: type[AppItem | typing.Any], parameters: typing.Mapping[str, Parameter]) -> typing.Any:
    params = [codegen.CLASS_PARAMETER, *parameters.values()]
    if 'kwargs' not in parameters:
        params.append(codegen.KWDS_PARAMETER)

    signature = inspect.Signature(
        params,
        return_annotation=typing.Self,
        __validate_parameters__=False
    )

    call_args = ', '.join(
        p.name if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD) else f"{p.name}={p.name}"
        for p in parameters.values()
    ).removesuffix(', kwargs=kwargs')

    method = codegen.create_function(
        "create",
        codegen.source_signature_from_parameters(params),
        f"return cls(tag=cls.__itemtype_command__({call_args}))",
        return_type=typing.Self,
    )
    _update_method_metadata(cls, "create", method, signature)

    return classmethod(method)


def _build_command_method(cls: typing.Any, parameters: typing.Mapping[str, Parameter]) -> typing.Any:
    command = getattr(_dearpygui, cls.__itemtype_info__.function.__name__)

    params = [*parameters.values()]
    if 'kwargs' not in parameters:
        params.append(codegen.KWDS_PARAMETER)

    signature = inspect.Signature(
        params,
        return_annotation=Item,
        __validate_parameters__=False
    )

    call_args = ', '.join(
        p.name if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD) else f"{p.name}={p.name}"
        for p in parameters.values()
    ).removesuffix(', kwargs=kwargs')

    method = codegen.create_function(
        "func",
        codegen.source_signature_from_parameters(params),
        f"return dearpygui_command({call_args})",
        return_type=Item,
        locals={"dearpygui_command": command}
    )
    _update_method_metadata(cls, command.__name__, method, signature)

    return staticmethod(method)




_CFG_PROPERTY_LOCALS = {
    "get_item_config": _dearpygui.get_item_configuration,
    "set_item_config": _dearpygui.configure_item,
    "get_item_state" : _dearpygui.get_item_state,
}

@functools.cache  # we're going to make a LOT of these
def _get_config_property(name, annotation, readonly, /) -> property:
    fget = codegen.create_function(
        name,
        codegen.FGET_SOURCE_ARGS,
        f"return get_item_config(self)['{name}']",
        return_type=annotation,
        module=__name__,
        locals=_CFG_PROPERTY_LOCALS
    )

    if readonly:
        fset = None
    else:
        fset = codegen.create_function(
            name,
            codegen.FSET_SOURCE_ARGS,
            f"set_item_config(self, {name}=value)",
            return_type=None,
            module=__name__,
            locals=_CFG_PROPERTY_LOCALS
        )
        fset.__annotations__[name] = annotation

    return property(fget, fset)


def _create_config_property(cls, parameter: Parameter, /, *, readonly: bool = False):
    name = parameter.name
    anno = parameter.annotation

    p = _get_config_property(name, anno, readonly)

    if readonly:
        cls.__annotations__[name] = property[anno, typing.Never]
    else:
        cls.__annotations__[name] = property[anno, anno]

    return p




_POS_ANNOTATION = property[list[int], typing.Sequence[int], typing.Literal[True]]

@property
def _POS_PROPERTY(self: typing.Any, /) -> list[int]:
    return _dearpygui.get_item_state(self)["pos"]
@_POS_PROPERTY.setter
def _POS_PROPERTY(self: typing.Any, value: typing.Sequence[int], /) -> None:
    _dearpygui.configure_item(self, pos=value)
@_POS_PROPERTY.deleter
def _POS_PROPERTY(self: typing.Any, /) -> None:
    _dearpygui.configure_item(self, pos=())




def _build[T: type[AppItem[typing.Any, typing.Any, typing.Any]]](
    cls: T,
    /,
    type_info: parsing.ItemTypeInfo,
    *,
    getattr=getattr,
    setattr=setattr,
    hasattr=hasattr,
) -> T:
    cls.__itemtype_info__ = type_info
    cls.__itemtype_identity__ = (type_info.type_uuid, type_info.type_qualname)

    cls.__itemtype_command__ = _build_command_method(cls, type_info.parameters.creation)
    cls.create = _build_create_method(cls, type_info.parameters.creation)
    #cls.configure = _build_configure_method(cls, type_info.parameters.writable)
    #cls.configuration = _build_configuration_method(cls, type_info.parameters.readable)

    parameters = type_info.parameters.writable
    if "pos" in parameters and not hasattr(cls, "pos"):
        setattr(cls, "pos", _POS_PROPERTY)
        cls.__annotations__["pos"] = _POS_ANNOTATION

    for name, param in parameters.items():
        if not hasattr(cls, name):
            prop = _create_config_property(cls, param)
            setattr(cls, name, prop)
            prop.__set_name__(cls, name)  # pyright: ignore[reportAttributeAccessIssue]

    for name, param in type_info.parameters.readable.items():
        if not hasattr(cls, name):
            prop = _create_config_property(cls, param, readonly=True)
            setattr(cls, name, prop)
            prop.__set_name__(cls, name)  # pyright: ignore[reportAttributeAccessIssue]

    return cls

def build[T: type[AppItem[typing.Any, typing.Any, typing.Any]]](cls: T) -> T:
    return _build(cls, type_info=parsing.itemtype_info()[cls.__name__])

