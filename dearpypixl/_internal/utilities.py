"""DearPyPixl's junk drawer."""
from __future__ import annotations
import functools
import itertools
import inspect
import types
import logging
import collections
from typing import Callable, Sequence, Literal, TYPE_CHECKING, TypeVar, Iterable, Any
from typing_extensions import Self
from inspect import signature, _VAR_POSITIONAL, _KEYWORD_ONLY
from dearpygui._dearpygui import get_item_info, does_item_exist
from . import registry
from .constants import APP_UUID
from .comtypes import Null

if TYPE_CHECKING:
    from .item import ItemType




_ST = TypeVar("_ST", set, list, collections.deque)

class _AutoSlotsType(type):
    def __new__(mcls, name, bases, namespace, **kwargs):
        if not "__slots__" in namespace:
            namespace["__slots__"] = ()
        return type.__new__(mcls, name, bases, namespace, **kwargs)

def _updseq_method_wrapper(method, base_cls):
    @functools.wraps(method)
    def updater_sequence_mthd(self, *args, **kwargs):
        cls = type(self)
        result = method(self, *args, **kwargs)
        if isinstance(result, base_cls) and not isinstance(result, cls):
            result = cls(result, callback=self.callback)
        self.callback()
        return result
    return updater_sequence_mthd

def _new_updater_seq_type(base: type[_ST], targets: Sequence[str], exec_body: dict = ()) -> type[_ST]:
    def init(self, iterable: Iterable = (), callback: Callable[[], Any] = None):
        super(_UpdaterSequence, self).__init__(iterable)
        self.callback = callback if callback else getattr(iterable, "callback", None)
        if not self.callback:
            raise ValueError("`callback` cannot be None.")

    def prepare_namespace(namespace: dict):
        dunders = {"__slots__": ("callback",), "__init__": init}
        methods = {t:_updseq_method_wrapper(getattr(base, t), base) for t in targets}
        namespace |= dict(exec_body) | methods | dunders

    _UpdaterSequence: type[_ST] = types.new_class(
        "_UpdaterSequence",
        (base,),
        {"metaclass":_AutoSlotsType},
        prepare_namespace,
    )
    return _UpdaterSequence

_LIST_METHODS = (
    "__add__",
    "__iadd__",
    "__mul__",
    "__rmul__",
    "__imul__",
    "__setitem__",
    "__delitem__",
    "append",
    "extend",
    "insert",
    "remove",
    "pop",
)
_SET_METHODS  = (
    "__and__",
    "__iand__",
    "__or__",
    "__ior__",
    "__sub__",
    "__isub__",
    "__xor__",
    "__ixor__",
    "add",
    "copy",
    "difference",
    "difference_update",
    "discard",
    "intersection",
    "intersection_update",
    "remove",
    "symmetric_difference",
    "symmetric_difference_update",
    "union",
    "update",
)


class UpdaterList(_new_updater_seq_type(list, _LIST_METHODS)):
    """A list that runs a callback when its content changes."""
    __init__: Callable[[Self, Iterable | None, Callable[[], Any] | None], None]


class UpdaterSet(_new_updater_seq_type(set, _SET_METHODS)):
    """A set that runs a callback when its content changes."""
    __init__: Callable[[Self, Iterable | None, Callable[[], Any] | None], None]


class TypeGuard:
    """Creates a callable validator object for checking argument(s) against certain
    criteria.
    """

    def __init__(self, types: tuple[type | object, ...] = None, callback: Callable = None, type_err_msg: str = None, value_err_msg: str = None):
        """Args:
            * types (type | object, ...], optional): A tuple of types that will be passed
            as the second argument of `isinstance`; raises TypeError if <argument> are not
            instances of <types>. Defaults to None (no error).
            * callback (Callable, optional): Raises ValueError if the result of
            `callback(argument)` is falsey. Defaults to None (no error).
        """
        self._types    = types or (object,)
        self._callback = callback or (lambda x: True)

        if not type_err_msg:
            if not types or len(self._types) == 1:
                type_err_msg = f"Value must be an instance of {self._types[0].__qualname__!r} (got {{}})."
            else:
                _qualnames = []
                for t in self._types:
                    try:
                        _qualnames.append(t.__qualname__)
                    except AttributeError:
                        _qualnames.append(t)
                type_err_msg = f"Value must be an instance of {', '.join(name for name in _qualnames[:-1])!r} or {_qualnames[-1]!r} (got {{}})."
        if not value_err_msg:
            value_err_msg = f"Result of `{self._callback.__qualname__}(<argument>)` is falsey (got type {{cls}} value {{value}})."

        self._type_err_msg = type_err_msg
        self._val_err_msg  = value_err_msg

    def __call__(self, argument: Sequence[object] | object):  # NOTE: won't work for mapping values
        """Raise TypeError if the argument (or any argument in a sequence of arguments) is
        not an instance of <types>, or ValueError if `callback(argument)` does not return True.

        Args:
            * argument (Sequence[object] | object): The object to check. If the object is
            a sequence, all objects within that sequence are checked (the sequence itself
            will not be checked).

        """
        types    = self._types
        callback = self._callback
        if not isinstance(argument, Sequence):
            argument = (argument,)
        for arg in argument:
            if not isinstance(arg, types):
                err_msg = self._type_err_msg.format(repr(arg))
                raise TypeError(err_msg)
            if not callback(arg):
                err_msg = self._val_err_msg.format(cls=repr(type(arg).__qualname__), value=repr(arg))
                raise ValueError(err_msg)

    def wraps(self, func: Callable = None, target_idx: int = 0):
        """(Decorator) Validate an argument of <func> before it is called.

        Args:
            * func (callable): Any callable object.
            * target_idx (int, optional): Used to index <func>'s sequence of
            arguments. The result will be validated.
        """
        @functools.wraps(func)
        def wrapper(func: Callable):
            def callable_object(*args):
                self(args[target_idx])
                return func(*args)
            return callable_object
        if func:
            return wrapper(func)
        return wrapper


class classproperty(property):
    """Descriptor/decorator for binding class-level read-only properties.
    Functionaly similar to chaining classmethod -> property decorators
    in Python 3.9 (which is deprecated in Python 3.11).
    """
    # pyright "special-cases" the property builtin so wrapped
    # methods masquerade as attributes instead, which is what
    # I want. Pretend classproperty doesn't subclass property :-)
    __slots__ = ("__wrapped__",)

    def __init__(self, fn):
        self.__wrapped__ = fn

    def __set_name__(self, cls, name):
        if set_name:=getattr(self.__wrapped__, "__set_name__", None):
            set_name(cls, name)

    def __get__(self, instance, cls):
        return self.__wrapped__(cls)


class generate_itemtype_uuid:
    """Return a unique integer value. Used for assigning a numeric identifier to
    ItemType classes with no representation in DearPyGui (i.e. custom types).
    Functionally similar to DearPyGui's `generate_uuid` function.
    """
    # To avoid conflicting w/dearpygui's existing item type enum values, these
    # will always be negative.
    __count = itertools.count(-1, -1)

    def __new__(cls) -> int:
        return next(cls.__count)


####################################################################################
################################# Helper Functions #################################
####################################################################################

def get_positional_args_count(obj: Callable) -> int:
    """Return the number of positional arguments for a given object.
    """
    # Emulating how DearPyGui doesn't require callbacks having 3 positional
    # arguments. Only pass sender/app_data/user_data if there's "room" to
    # do so.
    pos_arg_cnt = 0
    for param in signature(obj).parameters.values():
        if param.kind == _VAR_POSITIONAL:
            pos_arg_cnt = 3
        elif param.kind != _KEYWORD_ONLY:
            pos_arg_cnt += 1

        if pos_arg_cnt >= 3:
            pos_arg_cnt = 3
            break
    return pos_arg_cnt


def forward_method(attr: str):
    """Calls of the wrapped (bound) method will be forwarded to the method of the same name
    found on `self.<attr>`. The wrapped method will not be called and former result will be
    returned.

    This:
    >>> @forward_method("list_obj")
    ... def append(self, obj):
    ...     ...

    Becomes this:
    >>> def append(self, obj):
    ...     return self.list_obj.append(obj)

    """
    def process_method(mthd):
        @functools.wraps(mthd)
        def forwarded_method(self, *args, **kwargs):
            return getattr(getattr(self, attr), mthd_name)(*args, **kwargs)
        mthd_name = mthd.__name__
        return forwarded_method
    return process_method



def prep_callback(item: 'ItemType', _callback: Callable | None):
    """DearPyGui callback wrapper.
    """
    @functools.wraps(_callback)
    def callable_object(_=None, app_data=None, user_data=None, **kwargs):
        args = (item, app_data, user_data)[0:pos_arg_cnt]
        _callback(*args, **kwargs)

    # Wrapping, firstly, to ensure that the Item instance of `sender` is
    # returned instead of the identifier. And second; nuitka compilation
    # doesn't like DPG callbacks unless they are wrapped (lambda, etc.) for
    # some reason.
    if callable(_callback):
        wrapper = callable_object
        pos_arg_cnt = get_positional_args_count(_callback)
    elif _callback is None:
        wrapper = None
    else:
        raise ValueError(f"`callback` is not callable (got {type(_callback)!r}.")
    return wrapper


def set_cached_attribute(item, name, value) -> None:
    """Convenience function for setting the cached value of an attribute.
    """
    item.__itemdict__[name] = value


def itemized_return(obj: Callable = None, *, default=None):
    """A decorator for any callable that returns an item identifier. The callable
    will now return the Item instance for that identifier from the registry, or None
    if no Item instance is found.
    """
    @functools.wraps(obj)
    def get_item(*args, **kwargs):
        return registry.get_item(obj(*args, **kwargs), default)
    return get_item


def auto_itemtype_init(itemtype_init):
    """A decorator for `__init__`, redefining it. It will invoke `super().__init__`,
    sending it any included keyword arguments.
    """
    @functools.wraps(itemtype_init)
    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
    return __init__


def is_itemtype_public_api(itemtype: type[ItemType]):
    metadata = itemtype.__dearpypixl__
    if metadata.internal_only is not True \
    and not any(metadata.identity == v for v in (None, Null)) \
    and not inspect.isabstract(itemtype):
        return True
    return False


def is_unbound_item(item: int | str | ItemType) -> bool:
    """Return True if item identifier exists and is not bound to an ItemType instance in
    the DearPyPixl registry.
    """
    item_uuid = int(item)
    if does_item_exist(item_uuid) and item_uuid not in registry._items:
        return True
    return False

def is_class_descriptor(obj):
    return isinstance(obj, (classmethod, classproperty))


def getmembers_static(obj, predicate: Callable[[object], bool] = None):
    """Python 3.11 implementation of `inspect.getmembers_static`."""
    # copypasta of Python 3.11's inspect._getmembers/inspect.getmembers_static.
    # <https://github.com/python/cpython/blob/6ec57e7c5af6816178d34233a4da12eb0c21c9d9/Lib/inspect.py#L550>
    results = []
    processed = set()
    names = dir(obj)
    if inspect.isclass(obj):
        mro = (obj,) + inspect.getmro(obj)
        try:
            for base in obj.__bases__:
                for k, v in base.__dict__.items():
                    if isinstance(v, types.DynamicClassAttribute):
                        names.append(k)
        except AttributeError:
            pass
    else:
        mro = ()
    getter = inspect.getattr_static
    for key in names:
        try:
            value = getter(obj, key)
            if key in processed:
                raise AttributeError
        except AttributeError:
            for base in mro:
                if key in base.__dict__:
                    value = base.__dict__[key]
                    break
            else:
                continue
        if not predicate or predicate(value):
            results.append((key, value))
        processed.add(key)
    results.sort(key=lambda pair: pair[0])
    return results

try:
    from inspect import getmembers_static  # python 3.11
except ImportError:
    pass


def get_class_members(obj):
    return getmembers_static(obj, is_class_descriptor)


def get_reflected_linkeditem(item: ItemType, target: Literal["theme", "font"]):
    linkeditem = getattr(item, target, Null)
    item_uuid  = int(item)
    if linkeditem is Null:  # Null = unsupported
        return None
    if linkeditem:
        return linkeditem
    # At this point, it's confirmed the itemtype supports the target but is
    # set to None.
    applvl_linkeditem = getattr(registry.get_item(APP_UUID), target)
    if item_uuid == APP_UUID:
        return applvl_linkeditem
    # Check the parent(s) and find the "nearest" linked item.
    current_item_uuid = item_uuid
    linkeditem_uuid   = None
    while current_item_uuid and not linkeditem_uuid:
        item_info = get_item_info(current_item_uuid)
        linkeditem_uuid   = item_info[target]
        current_item_uuid = item_info["parent"]

    if not linkeditem_uuid:
        return applvl_linkeditem  # no target was found, ran out of parents.
    return registry.get_item(linkeditem_uuid)


def log(level: str, target: ItemType, message: str, reason: str = "", *, exc_info=None, extra=None, stack_info=False, stacklevel=1):
    level = logging._nameToLevel[level.upper()]
    if reason:
        reason = f" ({reason})"
    msg = f" [{target}] {message}{reason}"
    return logging.log(level, msg, exc_info=exc_info, stack_info=stack_info, stacklevel=stacklevel)







