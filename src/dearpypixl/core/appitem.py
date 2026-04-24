import typing

from dearpygui import _dearpygui

from . import interface
from . import management


__all__ = (
    "AppItemType",
    "AppItem",
    "ChildItem",
    "ContainerItem",
    "SupportsValueArray",
    "_HandlerItem",
    "_ElementItem",
    "_ElementInfo",
)




_MISSING = object()

_ITEM_REGISTRY = interface.Interface.__item_registry__


class AppItemType(type):
    __slots__ = ()

    __item_registry__ = _ITEM_REGISTRY

    __item_type__ = None
    __item_slot__ = 1
    __item_command__ = ''
    __item_parents__ = ()
    __item_children__ = ()

    def __new__(cls, name, bases, namespace, /, *, __type_new=type.__new__, command=None, slot=1):
        self = __type_new(cls, name, bases, namespace)

        if command:
            self.__item_type__ = self
            self.__item_slot__ = slot
            self.__item_command__ = command
            self.__hash__ = AppItem.__hash__  # type: ignore

            registry = __class__.__item_registry__
            registry[f"mvAppItemType::{name}"] = registry[getattr(_dearpygui, name)] = self

        return self

    def __int__(self, /, *, __cache=_dearpygui.__dict__):
        try:
            return __cache[self.__item_type__.__name__]  # ty:ignore[unresolved-attribute]
        except AttributeError, KeyError:
            return __cache["mvAll"]

    __index__ = __int__

    def __str__(self, /, *, __missing=_MISSING):
        try:
            return f"mvAppItemType::{self.__item_type__.__name__}"  # ty:ignore[unresolved-attribute]
        except AttributeError:
            return f"<class {self.__name__!r}>"

    __hash__ = type.__hash__

    def __eq__(self, other, /, *, __type=type, __type_eq=type.__eq__, __isinstance=isinstance) -> bool:
        if self is other:
            return True

        cls = self.__item_type__
        if cls is not None:
            return str(self) == other or int(self) == other

        return False

    def __repr__(self) -> str:
        return f"<class {self.__name__!r}>"


# type parameters are used only to ensure it produces generic subclasses
class AppItem[U = typing.Any, V = typing.Any, P = typing.Any, C = typing.Any](interface.Interface, int, metaclass=AppItemType):
    __slots__ = ()

    __class_getitem__ = classmethod(type(list[int]))

    @management.initializer
    def __new__(
        cls, /, tag=0, *,
        __isinstance=isinstance,
        __int_new=int.__new__,
        __int=int,
        __alloc=_dearpygui.generate_uuid,
        __set_item_alias=_dearpygui.add_alias,
        __get_item_uuid=_dearpygui.get_alias_id,
    ):
        if __isinstance(tag, __int):
            return __int_new(cls, tag or __alloc())

        alias = tag
        uuid  = __get_item_uuid(tag)  # ty:ignore[invalid-argument-type]
        if not uuid:
            uuid = __alloc()
            __set_item_alias(alias, uuid)  # ty:ignore[invalid-argument-type]

        return __int_new(cls, uuid)

    def __repr__(self, /):
        uuid = self.real
        try:
            alias = _dearpygui.get_item_alias(uuid)
        except SystemError:
            alias = ''
        try:
            label = _dearpygui.get_item_configuration(self)["label"]
        except SystemError:
            label = ''

        class_name = self.__class__.__name__

        if self.__class__.__item_type__ is None:
            try:
                type = _dearpygui.get_item_info(self)["type"]
            except SystemError:
                type = ''
            return f"{class_name}({type=}, {uuid=}, {alias=}, {label=})"

        return f"{class_name}({uuid=}, {alias=}, {label=})"

    def __int__(self, /):
        return self.real

    __hash__ = __int__

    def __eq__(self, other, /, *, __func=_dearpygui.get_item_alias):
        return (
            (self.real == other) or
            (alias == other if (alias:=__func(self.real)) else False)
        )

    @classmethod
    def create(cls, /, *args, **kwargs):
        raise NotImplementedError

    def destroy(self, /) -> None:
        try:
            _dearpygui.delete_item(self, children_only=False, slot=-1)
        except SystemError:
            pass
        return

    def delete(self, /, *, children_only: bool = False, slot: int = -1):
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

    def exists(self, /, *, __func=_dearpygui.does_item_exist):
        try:
            return __func(self)
        except SystemError:
            return False

    @property
    def tag(self):
        return self.real

    @property
    def uuid(self):
        return self.real

    @property
    def alias(self):
        return _dearpygui.get_item_alias(self)
    @alias.setter
    def alias(self, value, /):
        if value is None:
            alias = _dearpygui.get_item_alias(self)
            if alias is not None:
                _dearpygui.remove_alias(alias)
        else:
            _dearpygui.set_item_alias(self, value)
    @alias.deleter
    def alias(self):
        _dearpygui.remove_alias(_dearpygui.get_item_alias(self))

    @property
    def value(self, /, *, __func=_dearpygui.get_value):
        return __func(self)
    @value.setter
    def value(self, value, /, *, __func=_dearpygui.set_value):
        __func(self, value)

    # configuration

    @property
    def label(self, /, *, __func=_dearpygui.get_item_configuration):
        return __func(self)["label"]
    @label.setter
    def label(self, value, /, __func=_dearpygui.configure_item):
        __func(self, label=value)
    @label.deleter
    def label(self, /, __func=_dearpygui.configure_item):
        __func(self, label=None)

    @property
    def use_internal_label(self, /, *, __func=_dearpygui.get_item_configuration):
        return __func(self)["use_internal_label"]
    @use_internal_label.setter
    def use_internal_label(self, value, /, __func=_dearpygui.configure_item):
        __func(self, use_internal_label=value)

    @property
    def user_data(self, /, *, __func=_dearpygui.get_item_configuration):
        return __func(self)["user_data"]
    @user_data.setter
    def user_data(self, value, /, __func=_dearpygui.configure_item):
        __func(self, user_data=value)
    @user_data.deleter
    def user_data(self, /, __func=_dearpygui.configure_item):
        __func(self, user_data=None)

    def configure(self, **kwargs):
        _dearpygui.configure_item(self, **kwargs)

    def configuration(self, /):
        return _dearpygui.get_item_configuration(self)

    # information

    @staticmethod
    def _create_bound_info_property(type_key: int | str, field_key: str, setter, /) -> property:

        def fget(self, /, __type_key=type_key, __field_key=field_key, __func=_dearpygui.get_item_info, __int_new=int.__new__, __registry=_ITEM_REGISTRY):
            item = __func(self)[__field_key]
            if not item:
                return None
            return __int_new(__registry[__type_key], item)

        def fset(self, value, /, __func=setter):
            __func(self, value or 0)

        def fdel(self, /, __func=setter):
            __func(self, 0)

        fget.__name__ = fset.__name__ = fdel.__name__ = field_key

        return property(fget, fset, fdel)

    theme = _create_bound_info_property("mvTheme", "theme", _dearpygui.bind_item_theme)
    font = _create_bound_info_property("mvFont", "font", _dearpygui.bind_item_font)
    handlers = _create_bound_info_property("mvItemHandlerRegistry", "handlers", _dearpygui.bind_item_handler_registry)

    del _create_bound_info_property

    @property
    def parent(self, /, *, __func=_dearpygui.get_item_info, __int_new=int.__new__, __registry=_ITEM_REGISTRY):
        item = __func(self)["parent"]
        if item is None:
            return None

        type_name = __func(item)["type"]

        try:
            item_type = __registry[type_name]
        except KeyError:
            item_type = ContainerItem

        return __int_new(item_type, item)

    @property
    def parents(self, /, *, __func=_dearpygui.get_item_info, __int_new=int.__new__, __registry=_ITEM_REGISTRY):
        parents = []

        item_uuid = self

        while True:
            info =__func(item_uuid)

            parent = info["parent"]
            if parent is None:
                break

            item_uuid = parent
            type_name = info["type"]

            try:
                item_type = __registry[type_name]
            except KeyError:
                item_type = ContainerItem

            parents.append(__int_new(item_type, item_uuid))

        parents.reverse()

        return parents

    @property
    def root_parent(self, /, *, __func=_dearpygui.get_item_info, __int_new=int.__new__, __registry=_ITEM_REGISTRY):
        item_uuid = self
        type_name = ''

        while True:
            info =__func(item_uuid)

            parent = info["parent"]
            if parent is None:
                break

            item_uuid = parent
            type_name = info["type"]

        if item_uuid == self.real:
            return None

        try:
            item_type = __registry[type_name]
        except KeyError:
            item_type = ContainerItem

        return __int_new(item_type, item_uuid)

    def information(self, /, *, __func=_dearpygui.get_item_info):
        return __func(self)

    # state

    @property
    def pos(self, /, *, __func=_dearpygui.get_item_state):
        return __func(self)["pos"]

    def state(self, /, *, __func=_dearpygui.get_item_state):
        return __func(self)

    # other methods

    def children(self, /, slot=-1, *, __func=_dearpygui.get_item_info, __int_new=int.__new__):
        items = __func(self)["children"]
        if slot == -1:
            return items

        item_type = ChildItem
        return [__int_new(item_type, item_uuid) for item_uuid in items[slot]]

    def focus(self, /, *, __func=_dearpygui.focus_item):
        __func(self)


class ChildItem[U = typing.Any, V = typing.Any, P = typing.Any, C = typing.Any](AppItem):
    __slots__ = ()

    __item_type__ = _MISSING

    __hash__ = AppItem.__hash__

    def move(self, *, parent=0, before=0, __func=_dearpygui.move_item):
        __func(self, parent=parent, before=before)

    def move_up(self, /, *, __func=_dearpygui.move_item_up):
        __func(self)

    def move_down(self, /, *, __func=_dearpygui.move_item_down):
        __func(self)

    def unstage(self, /, *, __func=_dearpygui.unstage):
        __func(self)


class ContainerItem[U = typing.Any, V = typing.Any, P = typing.Any, C = typing.Any](AppItem):
    __slots__ = ()

    __item_type__ = _MISSING

    __hash__ = AppItem.__hash__

    def __enter__(self, /, *, __func=_dearpygui.push_container_stack):
        __func(self)
        return self

    def __exit__(self, exc_type = None, exc_value = None, traceback = None, /, *, __func=_dearpygui.pop_container_stack):
        __func()

    __item_index_slot__ = 1
    __item_index_type__ = ChildItem

    def __getitem__(self, index, /, *, __func=_dearpygui.get_item_info, __new=int.__new__, __list=list):
        children = __func(self)["children"][self.__item_index_slot__][index]

        if children.__class__ is __list:
            item_type = self.__item_index_type__
            return [__new(item_type, child) for child in children]

        return __new(self.__item_index_type__, children)

    def __delitem__(self, index, /, *, __func=_dearpygui.delete_item, __list=list):
        children = _dearpygui.get_item_info(self)["children"][self.__item_index_slot__][index]

        if children.__class__ is __list:
            for child in children:
                __func(child, children_only=False, slot=-1)
        else:
            __func(children, children_only=False, slot=-1)

    def index(self, item, /, slot = None):
        if isinstance(item, str):
            tag = _dearpygui.get_alias_id(item)
        else:
            tag = item

        child_slots = _dearpygui.get_item_info(self)["children"]

        if slot is not None:
            if -5 < slot < 4:
                slot %= 4
            else:
                raise IndexError("slot index out of range")

            try:
                return child_slots[slot].index(tag)
            except ValueError:
                raise ValueError(f"item {item!r} not in child slot {slot!r}") from None

        slot0, slot1, slot2, slot3 = child_slots.values()
        if tag in slot1:
            return slot1.index(tag)
        if tag in slot0:
            return slot0.index(tag)
        if tag in slot2:
            return slot2.index(tag)
        if tag in slot3:
            return slot3.index(tag)

        raise ValueError(f"item {item!r} is not a child of {self!r}")

    def insert(self, index, item, /, slot=None, *, __get_info=_dearpygui.get_item_info, __move_item=_dearpygui.move_item) -> None:
        if slot is not None:
            if -5 < slot < 4:
                slot_index = slot % 4
            else:
                raise IndexError("slot index out of range")
        else:
            slot_index = __get_info(item)["target"]

        child_slot = __get_info(self)["children"][slot_index]
        __move_item(item, parent=self, before=child_slot[index])

    def reorder(self, /, slot=None, new_order=None, *, __func=_dearpygui.reorder_items):
        if slot is None:  # `new_order` is a keyword argument
            slot = self.__item_index_slot__
        elif new_order is None:  # `new_order` the (sole) positional argument
            new_order = slot
            slot = self.__item_index_slot__
        elif -5 < slot < 4:
            slot %= 4
        else:
            raise IndexError("slot index out of range")

        assert new_order is not None
        __func(self, slot, new_order)


class CompositeItem:
    __slots__ = ()

    components = ()

    if __debug__:
        def __init_subclass__(cls, **kwargs) -> None:
            bases = __class__.__bases__
            if __class__ not in bases:
                return super().__init_subclass__(**kwargs)

            index = bases.index(__class__)

            for tp in bases[:index]:
                if isinstance(tp, AppItemType):
                    management.warn(
                        f"{cls.__name__!r} — solid base class `CompositeItem` should be listed prior "
                        "to all other `AppItem` bases",
                        stacklevel=2,
                    )

            if not isinstance(cls, AppItemType):
                management.warn(
                    f"{cls.__name__!r} — resulting subclass using solid base class `CompositeItem` "
                    "should be a subclass of `AppItem`"
                )

            super().__init_subclass__(**kwargs)

    @property
    def user_data(self):
        return self.__dict__.get("user_data", None)
    @user_data.setter
    def user_data(self, value, /):
        self.__dict__["user_data"] = value
    @user_data.deleter
    def user_data(self, /):
        self.__dict__["user_data"] = None

    @classmethod
    def create(cls, /, user_data=None, **kwargs):
        return super().create(user_data={"user_data": user_data}, **kwargs)  # ty:ignore[unresolved-attribute]

    def __init__(self: typing.Any, /, tag=0):
        user_data = _dearpygui.get_item_configuration(self)["user_data"]
        try:
            self.__dict__ = user_data
        except TypeError:
            self.__dict__["user_data"] = user_data
            _dearpygui.configure_item(self, user_data=self.__dict__)

    def __repr__(self: typing.Any, /):
        # uses the concrete class name, whereas `AppItem.__repr__()` always
        # uses the item type's name
        uuid = self.real
        try:
            alias = _dearpygui.get_item_alias(uuid)
        except SystemError:
            alias = ''
        try:
            label = _dearpygui.get_item_configuration(self)["label"]
        except SystemError:
            label = ''

        return f"{self.__class__.__name__}({uuid=}, {alias=}, {label=})"

    def destroy(self, /, *, __func=_dearpygui.delete_item):
        for item in self.components:
            destructor = getattr(item, "destroy", None)
            if callable(destructor):
                destructor()
            else:
                try:
                    __func(item, children_only=False, slot=-1)
                except SystemError:
                    pass

        try:
            self.__dict__.clear()
        except AttributeError:
            pass

        super().destroy()  # type: ignore

    def configure(self: typing.Any, /, user_data=_MISSING, __missing=_MISSING, **kwargs):
        super().configure(**kwargs)
        if user_data is not __missing:
            self.user_data = user_data

    def configuration(self: typing.Any, /):
        config = super().configuration()
        config["user_data"] = self.user_data
        return config


class SupportsValueArray[T]:
    __slots__ = ()

    def get_value(self: typing.Any) -> list[T]:
        return _dearpygui.get_value(self) or []

    def set_value(self: typing.Any, value, /) -> None:
        _dearpygui.set_value(self, value)

    def __len__(self, /) -> int:
        value = self.get_value()
        return 0 if not value else len(value)

    def __iter__(self, /) -> typing.Iterator[T]:
        return iter(self.get_value())

    def __reversed__(self, /) -> typing.Iterator[T]:
        yield from reversed(self.get_value())

    def __contains__(self, value: T, /) -> bool:
        return value in self.get_value()

    def __getitem__(self, index, /):
        return self.get_value()[index]

    def __setitem__(self, index, value, /) -> None:
        item_value = self.get_value()
        item_value[index] = value
        self.set_value(item_value)


class _ElementInfo:
    __slots__ = ("type", "name", "fullname", "category", "target")

    def __astuple(self, /):
        return (self.type, self.name, self.fullname, self.category, self.target)

    def __init__(self, type, function, constant, category, target, /):
        self.type = type
        self.name = function
        self.fullname = constant
        self.category = category
        self.target = target

    def __repr__(self, /):
        type = self.type
        name = self.name
        fullname = self.fullname
        category = self.category
        target = self.target
        return f"_ElementInfo({type=}, {name=}, {fullname=}, {category=}, {target=})"

    def __hash__(self, /):
        return hash(self.__astuple())

    def __add__(self, x, /):
        return self.__astuple() + x

    __iadd__ = __add__

    def __radd__(self, other, /):
        return other + self.__astuple()

    def __iter__(self, /):
        yield self.type
        yield self.name
        yield self.fullname
        yield self.category
        yield self.target

    def __getitem__(self, index, /):
        match index:
            case 0 | -5: return self.type
            case 1 | -4: return self.name
            case 2 | -3: return self.fullname
            case 3 | -2: return self.category
            case 4 | -1: return self.target

        return self.__astuple()[index]

    def index(self, /, *args):
        return self.__astuple().index(*args)

class _ElementItem[U = typing.Any, P = typing.Any](SupportsValueArray, ChildItem):
    __slots__ = ()

    __item_type__ = _MISSING

    __hash__ = AppItem.__hash__

    @property
    def category(self, /) -> int:
        return _dearpygui.get_item_configuration(self)["category"]

    @property
    def target(self, /) -> int:
        return _dearpygui.get_item_configuration(self)["target"]

    def identify(self, /) -> '_ElementInfo':
        """Return a `_ElementInfo` object -- a tuple-like object with information
        regarding this theme element's identity.

        The returned `_ElementInfo` object has five read-only attributes:
        - `type`: The element's concrete class in Dear PyPixl (:py:class:`mvThemeColor`
        or :py:class:`mvThemeStyle`).
        - `name`: The name of the theme element. Matches the name of a function in
        the :py:module:`dearpypixl.color` or :py:module:`dearpypixl.style` namespaces.
        - `fullname`: The name of the theme element. Matches the name of a constant in
        the `dearpygui.dearpygui` and `dearpypixl` namespaces.
        - `category`: The value returned via `get_item_configuration(element)["category"]`.
        - `target`: The value returned via `get_item_configuration(element)["target"]`.
        """
        try:
            registry = __class__._ELEMENT_REGISTRY
            name_map = __class__._ELEMENT_NAME_MAP
        except AttributeError:
            import re

            registry = {}
            name_map = {}

            pattern = re.compile(r"[A-Z][a-z0-9]*")
            buffer  = []

            for symbol, value in _dearpygui.__dict__.items():
                prefix, _, suffix = symbol.partition('_')
                match prefix:
                    case "mvThemeCol":
                        type_name = "mvAppItemType::mvThemeColor"
                        prefix    = ''
                        category  = _dearpygui.mvThemeCat_Core
                    case "mvPlotCol":
                        type_name = "mvAppItemType::mvThemeColor"
                        prefix    = 'plot'
                        category  = _dearpygui.mvThemeCat_Plots
                    case "mvNodeCol" | "mvNodesCol":
                        type_name = "mvAppItemType::mvThemeColor"
                        prefix    = 'node'
                        category  = _dearpygui.mvThemeCat_Nodes
                    case "mvStyleVar":
                        type_name = "mvAppItemType::mvThemeStyle"
                        prefix    = ''
                        category  = _dearpygui.mvThemeCat_Core
                    case "mvPlotStyleVar":
                        type_name = "mvAppItemType::mvThemeStyle"
                        prefix    = 'plot'
                        category  = _dearpygui.mvThemeCat_Plots
                    case "mvNodeStyleVar" | "mvNodesStyleVar":
                        type_name = "mvAppItemType::mvThemeStyle"
                        prefix    = 'node'
                        category  = _dearpygui.mvThemeCat_Nodes
                    case _:
                        continue

                if prefix:
                    buffer.append(prefix)

                for substring in suffix.split("_"):
                    for word in pattern.findall(substring):
                        word = word.lower()
                        if word == prefix:
                            continue
                        buffer.append(word)

                name = '_'.join(buffer).replace("background", "bg").replace("foreground", "fg")

                registry[(type_name, category, value)] = symbol
                name_map[symbol] = name
                buffer.clear()

            __class__._ELEMENT_REGISTRY = registry
            __class__._ELEMENT_NAME_MAP = name_map

        info   = _dearpygui.get_item_info(self)
        config = _dearpygui.get_item_configuration(self)

        e_type     = info["type"]
        e_category = config["category"]
        e_target   = config["target"]
        try:
            e_fullname = registry[(e_type, e_category, e_target)]
        except KeyError:
            raise TypeError(f"{self!r} is not a theme color or style")
        e_name = name_map[e_fullname]
        e_type = __class__.__item_registry__[e_type]

        return _ElementInfo(e_type, e_name, e_fullname, e_category, e_target)


class _HandlerItem[U = typing.Any, P = typing.Any](ChildItem):
    __slots__  = ()

    __item_type__ = _MISSING

    __hash__ = AppItem.__hash__

    @property
    def callback(self, /, *, __func=_dearpygui.get_item_configuration):
        return __func(self)["callback"]
    @callback.setter
    def callback(self, value, /, *, __func=_dearpygui.configure_item) -> None:
        __func(self, callback=value)
    @callback.deleter
    def callback(self, /, *, __func=_dearpygui.configure_item):
        __func(self, callback=None)

    @property
    def show(self, /, *, __func=_dearpygui.get_item_configuration) -> bool:
        return __func(self)["show"]
    @show.setter
    def show(self, value, /, *, __func=_dearpygui.configure_item) -> None:
        __func(self, show=value)
