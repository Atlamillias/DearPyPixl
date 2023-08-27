"""Python junk drawer."""
# pyright:reportGeneralTypeIssues=information
import sys
import abc
import enum
import copy
import types
import array
import ctypes
import typing
import inspect
import builtins
import itertools
import functools
import threading
from .common import Callable, Any, Iterable, Mapping, Sequence, MutableSequence, MutableMapping


_T = typing.TypeVar("_T")
_O = typing.TypeVar("_O")
_F = typing.TypeVar("_F", bound=types.FunctionType)
_N = typing.TypeVar("_N", float, int)
_P = typing.ParamSpec("_P")

_SENTINEL = object()





SPECIAL_INTERNALS = (
    '__abstractmethods__',
    '__annotations__',
    '__base__',
    '__bases__',
    '__basicsize__',
    '__class__',
    '__class_getitem__',
    '__dict__',
    '__dictoffset__',
    '__doc__',
    '__flags__',
    '__init__',
    '__itemsize__',
    '__module__',
    '__mro__',
    '__name__',
    '__new__',
    '__qualname__',
    '__slots__',
    '__subclasses__',
    '__subclasshook__',
    '__text_signature__',
    '__weakref__',
    '__weakrefoffset__',
)
TYPING_INTERNALS = (
    '__parameters__',
    '__orig_bases__',
    '__orig_class__',
    '_is_protocol',
    '_is_runtime_protocol',
)
ABSTRACT_INTERNALS = (
    '__abstractmethod__',
    '__abstractmethods__',
    '_MutableMapping__marker',
)





def is_builtin(o: Any) -> bool:
    """Return `True` if an object is a built-in class or function.

    A 'built-in' object is any object available in the `builtins` module.
    This includes all primitive types (`str`, `list`, etc.) and functions
    such as `print` and `isinstance`.
    """
    try:
        return o.__module__ == type.__module__
    except:
        return False


def is_type_object(o: Any) -> bool:
    """Return `True` if an object is a class/type.

    A class/type object is any object that is, or is an instance of, the `type`
    built-in class.
    """
    return isinstance(o, type)


def is_inst_object(o: Any) -> bool:
    """Return `True` if an object is an instance object.

    An instance object is any object that is not, or is not an instance of, the
    `type` built-in class.
    """
    return not isinstance(o, type)


def is_instance(o: Any, tp: type[Any] | tuple[type[Any], ...], /) -> bool:
    """Return `True` if an object is an instance of a type, or is an instance
    of any of the included types. Returns `False` otherwise, or if the object
    is not an instance.

    Args:
        * o: The class/type or instance object to test.

        * tp: A single class/type, or a tuple of class/type objects.


    There is no functional difference between this function and the `isinstance`
    built-in.
    """
    # unlike `issubclass`, no TypeError is thrown due to the object's
    # classification
    return isinstance(o, tp)


def is_subclass(o: Any, tp: type[Any] | tuple[type[Any], ...], /) -> bool:
    """Return `True` if an object is (or is a subclass of) a type, or is (or is a
    subclass of) any of the included types. Returns `False` otherwise, or if the
    object is not a class.

    Args:
        * o: The class/type object to test.

        * tp: A single class/type, or a tuple of class/type objects.


    The only functional difference between this function and the `isinstance`
    built-in is that the `TypeError` is handled when *o* is not a class.
    """
    try:
        return issubclass(o, tp)
    except TypeError:
        if is_type_object(o):
            raise
        return False


def is_iterable(o: Any):
    """Return `True` if an object has an `.__iter__` method.

    An object is iterable if the result of `iter(object)` returns an iterator.
    All iterators, sequences, and containers are iterable.
    """
    return hasattr(o, "__iter__")


def is_iterator(o: Any):
    """Return `True` if an object is iterable and has a `.__next__` method.

    All iterators are iterable, but not all iterables are iterators. For
    example, `next([0, 1, 2])` results in an error, but `next(iter([0, 1, 2]))`
    does not.
    """
    try:
        o.__next__
        o.__iter__
    except:
        return False
    return True


def is_container(o: Any, *, protocol_only: bool = False):
    """Return `True` if an object is a container.

    Containers are iterables capable of storing various objects. They are
    required to implement the `.__contains__` method.
    """
    return hasattr(o, "__contains__")


def is_sequence(o: Any):
    """Return `True` if an object is a sequence.

    Sequences are subscriptable containers storing ordered values and feature
    position-based lookups -- typically using integers or integer-like keys as
    subscript -- called indexes. They are required to implement the `.__len__` and
    `.__getitem__` methods, where `.__getitem__` differs to the subscript's
    `.__index__` method for lookups.

    Mappings and sequences share the same protocol. A sequence's `.__getitem__`
    method will raise 'IndexError' when the subscript is out-of-range, where
    a mapping's `.__getitem__` method will raise `KeyError`.
    """
    try:
        o[len(o) + 1]
    except IndexError:
        return True
    except:
        pass
    return False


def is_mapping(o: Any):
    """Return `True` if an object is a mapping.

    Mappings are subscriptable containers storing associated key-value pairs
    and support arbitrary key lookups, allowing any hashable object to be used as
    a key. They are required to implement the `.__len__` and `.__getitem__` methods,
    where `.__getitem__` differs to the subscript's `.__hash__` method for lookups.

    Mappings and sequences share the same protocol.
    """
    try:
        o.__len__
        o[_SENTINEL]
    except KeyError:
        return True
    except:
        pass
    return False



def dunders(tp: type[Any], *, excludes: Sequence[str] = (), excl_inherited: bool = False) -> list[str]:
    """Return the names of an object's dunder methods.

    Args:
        * o: The object of inquiry.

        * excludes: Names of members to exclude.

        * excl_inherited: If `True`, only fetch members from the type's
        `__dict__`.
    """
    startsw = str.startswith
    endsw   = str.endswith
    # `.startswith("__")` is *usually* enough, since most that also
    # don't end with "__" are name-mangled. But just in case...
    return sorted(set(
        n
        for n in (tp.__dict__ if excl_inherited else dir(tp))
        if startsw(n, "__") and endsw(n, "__") and n not in excludes
    ))


def flatten(tp: type[_T], *iterables: Iterable[Any]) -> _T:
    """Return a flattened collection object from iterables."""
    return tp(itertools.chain(*iterables))


def flatten_as_set(*iterables: Iterable[Any]) -> set[Any]:
    """Return a flattened set from several iterables."""
    return flatten(set, *iterables)


def flatten_as_list(*iterables: Iterable[Any]) -> list[Any]:
    """Return a flattened list from several iterables."""
    return flatten(list, *iterables)


def flatten_as_tuple(*iterables: Iterable[Any]) -> tuple[Any]:
    """Return a flattened tuple from several iterables."""
    return flatten(tuple, *iterables)


def flatten_as_arr(tp_code: str, *iterables: Iterable[Iterable[_T]]) -> array.array | MutableSequence[_T]:
    """Return a flattened Python array from several iterables."""
    return array.array(tp_code, itertools.chain(*iterables))


def hasattrs(o: Any, *names: str) -> bool:
    """Return True if an object has attribute(s) of all given names."""
    return all(hasattr(o, name) for name in names)


def namespace_path(o: type | types.FunctionType) -> tuple[str, str]:
    assert hasattr(sys.modules[o.__module__], o.__name__)
    return o.__module__, o.__name__


def create_function(name: str, args: Sequence[str], body: Sequence[str], return_type: _T = Any, *, globals: dict | None = None, locals: dict | None = None) -> Callable[..., _T]:
    """Dynamically define and return a new function.

    Args:
        * name: Formal name for the new function.

        * args: A sequence containing argument signatures (as strings) for the new
        function. Each value in *args* should be limited to a single argument
        signature.

        * body: A sequence containing the source code (as strings) that will execute
        when the new function is called. Each value in *body* should be limited to
        one line of executable source code.

        * return_tp: The type/annotation indicating the new function's return type.

        * globals: The global scope that will be available to the new function.

        * locals: The local scope that will be available to the new function.
    """
    locals = locals if locals is not None else {}
    locals["_return"] = return_type

    body    = '\n'.join(f"        {line}" for line in body)
    closure = (
        f"def __create_function__({', '.join(locals)}):\n"
        f"    def {name}({', '.join(args)}) -> _return:\n{body}\n"
        f"    return {name}"
    )

    scope = {}
    exec(closure, globals, scope)

    fn = scope["__create_function__"](**locals)
    fn.__qualname__ = name
    return fn


def copy_function(
    fn      : _F,
    /,
    name    : str                   | None = None,
    code    : types.CodeType        | None = None,
    globals : dict[str, Any]        | None = None,
    defaults: tuple[Any]            | None = None,
    closure : tuple[types.CellType] | None = None,
) -> _F:
    """Return a copy of a function.

    NOTE: This function may not work with non-standard Python
    implementations.

    A deepcopy operation is performed objects code objects and closures
    before creating the function. Existing references are used for all
    other objects.
    """
    new = types.FunctionType(
        name=fn.__name__ if name is None else name,
        globals=fn.__globals__ if globals is None else globals,
        argdefs=fn.__defaults__ if defaults is None else defaults,
        # Most users won't mess with these objects. The deepcopy op is
        # for those that will.
        code=copy.deepcopy(fn.__code__ if code is None else code),
        closure=copy.deepcopy(fn.__closure__ if closure is None else closure),
    )
    new.__dict__.update(fn.__dict__)
    return new


def cfunction(pfunction: 'ctypes._NamedFuncPointer', argtypes: tuple[Any, ...] = (), restype: Any = None):
    """Cast a foreign C function pointer as the decorated function.

    *argtypes* and *restypes* will be assigned to *pfunction*.
    """
    def func_prototype(fn_signature: Callable[_P, _T]) -> Callable[_P, _T]:
        pfunction.argtypes = argtypes
        pfunction.restype  = restype
        functools.update_wrapper(pfunction, fn_signature, updated='')
        return pfunction  # type: ignore
    return func_prototype



@typing.final
class _MarkerType(typing.Protocol):
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __delattr__(self, name: str) -> TypeError: ...
    def __setattr__(self, name: str, value: Any) -> TypeError: ...


def create_marker_type(name: str, *, body: Mapping[str, Any] | Sequence[tuple[str, Any]] = ()) -> type[_MarkerType]:
    """Dynamically create and return a new marker type as if it were defined
    in the module this function is called from.

    Markers cannot be instantiated or subclassed, and are read-only by default.

    Args:
        * name: Class name of the marker.

        * body: A mapping to use as the namespace/dict of the marker's
        metaclass.


    This function creates both the marker class as well as the marker's metaclass.
    By default, the metaclass implements the `__repr__`, `__eq__`, `__hash__`,
    `__setattr__`, and `__delattr__` methods. User implementations included in
    *body* will be used instead, if present.

    Note that the metaclass also implements `__new__` and `__call__`. User
    implementations of these methods will be used when creating the marker class
    if available. However, they are deleted from the metaclass' dict before
    returning the marker class.
    """
    body = dict(body)
    if '__module__' in body:
        module = sys.modules[body['__module__']]
    else:
        module = inspect.getmodule(inspect.stack()[1][0])
        assert module.__name__  # type:ignore

    namespace = {
        '__module__': module.__name__,  # type:ignore
        '__repr__': create_function(
            '__repr__',
            ('cls',),
            (f'return "<class \'{name}\'>"',),
            globals=module.__dict__
        ),
        '__eq__': create_function(
            '__eq__',
            ('cls', 'other'),
            (f'return other is cls',),
            globals=module.__dict__
        ),
        '__hash__': create_function(
            '__hash__',
            ('cls',),
            (f'return {hash(object())}',),
            globals=module.__dict__,
        ),
        '__setattr__': create_function(
            '__setattr__',
            ('cls', 'name = None', 'value = None'),
            (f"raise TypeError(\"cannot set attributes on read-only class {name!r}.\")",),
            globals=module.__dict__,
        ),
        '__delattr__': create_function(
            '__delattr__',
            ('cls', 'name = None'),
            (f"raise TypeError(\"cannot delete attributes on read-only class {name!r}.\")",),
            globals=module.__dict__,
        ),
    }
    namespace.update(body)
    cls: Any = type(f'{name.title()}Type', (type,), namespace)(
        name, (), {'__module__': module.__name__}   # type:ignore
    )
    type(cls).__call__ = create_function(
        '__call__',
        ('*args', '**kwargs'),
        (f"raise TypeError(\"{name!r} class cannot be instantiated.\")",),
        globals=module.__dict__,
    )
    type(cls).__new__ = create_function(
        '__new__',
        ('*args', '**kwargs'),
        (f"raise TypeError(\"one or more bases cannot be subclassed.\")",),
        globals=module.__dict__,
    )
    return typing.final(cls)


def frozen_namespace(cls: type[_T]) -> type[_T]:
    contents = tuple(m for m in dir(cls) if not m.startswith('_'))
    return create_marker_type(  # type: ignore
        cls.__qualname__,
        body={
            "__module__": cls.__module__,
            '__annotations__': cls.__annotations__,
            "__iter__": create_function(
                '__iter__',
                ('self',),
                ('return iter({' + ', '.join(f"'{m}': self.{m}" for m in contents) + '}.items())',),
                globals=sys.modules[cls.__module__].__dict__,
            ),
            **{m: getattr(cls, m) for m in contents}
        }
    )




def resolve_annotation(annotation: Any, globals: Mapping[str, Any], trim: bool = True, *, use_typing: bool = True):
    """Evaluate a type hint within a global scope.

    Args:
        * annotation: A `str` instance or class object to evaluate.

        * globals: The namespace to use for the evaluation.

        * trim: If `True`, the root type of the annotation will be returned.
        When `False`, the entire evaluated annotation is returned.

        * use_typing: If `True`, the `typing` module will be used before
        *globals* when evaluating parts of the annotation.


    If the annotation is not a string, it is returned as-is without
    modification.
    """
    # None is the only object usable as a type hint that is not a class
    # or "special form". PEP-0484 states that using None as an annotation
    # is equivelent to `type(None)`. This function always evals None as
    # just None, since `NoneType` is not available without importing `types`
    # or a pre-existing alias to `NoneType`.
    if is_instance(annotation, str):
        annotation = typing.ForwardRef(annotation, is_argument=False, is_class=True)
        annotation = typing._eval_type(
            annotation,
            globals,
            typing.__dict__ if use_typing else None
        )
    if annotation is type(None):
        return annotation
    return typing._strip_annotations(annotation) if trim else annotation


def unresolve_annotation(annotation: Any, globals: Mapping[str, Any]):
    """Return a annotation as if it were read as Python source code.

    Args:
        * annotation: A `str` instance or class object to evaluate.


    If the annotation is already a string, it is returned as-is without
    modification.

    Depending on the Python version used, the returned annotation may not be
    proper source code. This is because older versions of Python may lack
    "quality of life" typing changes. For example, `dict` annotations in
    Python 3.6 require using `typing.Dict`.

    When (un)resolving the annotation, `Union` and `Optional` annotations are
    not formatted using the union (`|`) operator.

    The `exec` and/or `resolve_annotations` can reverse this process given
    the proper globals and locals.
    """
    if not is_instance(annotation, str):
        param = inspect.Parameter(
            "_",
            inspect.Parameter.POSITIONAL_ONLY,
            annotation=annotation
        )
        annotation = str(param).split("_: ", maxsplit=1)[-1]

    if not globals:
        globals = {}

    if '__name__' in globals and globals['__name__'] in annotation:
        annotation = annotation.replace(f"{globals['__name__']}.", '')
    elif not (annotation in globals or annotation in builtins.__dict__):
        anno = ''
        for part in reversed(annotation.split(".")):
            if part in globals:
                annotation = part if not anno else f'{part}.{anno}'
                break
            anno = part if not anno else f'{part}.{anno}'
        else:
            raise RuntimeError(
                f'could not find annotation reference in globals.'
            )
    return annotation




def _get_typing_internals():
    import typing, collections.abc

    target_modules = (typing.__name__, collections.abc.__name__,)

    dunders = set()
    type_members = set(itertools.chain(object.__dict__.keys(), type.__dict__.keys()))  # type: ignore
    for obj in typing.__dict__.values():
        try:
            if obj.__module__ not in target_modules:
                continue
        except AttributeError:
            continue

        members = dir(obj)
        dunders.update(
            m for m in members
            if m not in type_members
            and m.startswith("_")
            and not m.endswith("__")
        )
    return tuple(sorted(dunders))





def protocol_members(cls):
    """Return a protocol's structural members.

    "Structural" members include the protocol's `__dict__` keys and class-level
    annotations.

    Special attribute names such as those of significant importance to the
    Python interpreter, typing (module), or are considered Python "implementation
    detail"s are excluded.
    """
    targets = set()
    internals = (SPECIAL_INTERNALS, TYPING_INTERNALS, ABSTRACT_INTERNALS)
    for base in cls.__mro__[:-1]:
        if base.__name__ in ('Protocol', 'Generic'):
            continue

        for member in itertools.chain(base.__dict__, getattr(base, '__annotations__', {})):
            if (
                not member.startswith('_abc_')
                and all(member not in c for c in internals)
            ):
                targets.add(member)
    return targets



def cache_once(fn: Callable[_P, _T], /) -> Callable[_P, _T]:
    """Similar to `functools.cached_property` but for functions. Returns the
    same result regardless of the arguments passed to the decorated function.
    """
    @functools.wraps(fn)
    def cached_result(*args: _P.args, **kwargs: _P.kwargs) -> _T:
        nonlocal cache
        try:
            return cache
        except NameError:
            cache = fn(*args, **kwargs)
            return cache
    cache: _T
    return cached_result


@functools.lru_cache(128)
def parameters(c: Callable) -> tuple[inspect.Parameter]:
    """Return the parameters of the given callable. The result
    is cached for future calls.

    Args:
        * c: Callable for the query.
    """
    return tuple(inspect.signature(c).parameters.values())










class _property(typing.Generic[_T], abc.ABC):
    __slots__ = ('__wrapped__',)

    def __init__(self, fget: Callable[..., _T]):
        self.__wrapped__ = fget

    def __set_name__(self, cls: type[Any], name: str):
        set_name = getattr(self.__wrapped__, "__set_name__", None)
        if set_name:
            set_name(cls, name)

    @abc.abstractmethod
    def __get__(self, instance: Any, cls: type | None = None) -> _T | typing.Self: ...


class classproperty(_property, typing.Generic[_T]):
    """A descriptor for emulating class-bound virtual attributes. Can
    optionally be used as a decorator.

    The functionality of this descriptor is similar to a `classmethod` and
    `property` descriptor chain in Python 3.9 which, as of 3.11, has been
    deprecated.

    Note that, due to Python's lookup behavior, the mutability of the
    property can be misleading; it is read-only when an assignment is made
    on an instance, but not on the class. This weird behavior is one of the
    reasons for the feature's deprecation.
    """
    __slots__ = ()

    def __get__(self, instance: Any, cls: type[Any]) -> _T:
        return self.__wrapped__(cls)


class staticproperty(_property, typing.Generic[_T]):
    """A descriptor for emulating unbound virtual attributes. Can optionally
    be used as a decorator.

    The functionality of this descriptor is similar to a `staticmethod` and
    `property` descriptor chain in Python 3.9 which, as of 3.11, has been
    deprecated.

    Note that, due to Python's lookup behavior, the mutability of the
    property can be misleading; it is read-only when an assignment is made
    on an instance, but not on the class. This weird behavior is one of the
    reasons for the feature's deprecation.
    """
    __slots__ = ()

    def __get__(self, instance: Any, cls: type[Any]) -> _T:
        return self.__wrapped__()


class simpleproperty(_property, typing.Generic[_T]):
    """A data descriptor for emulating read-only virtual attributes. Can
    optionally be used as a decorator.
        >>> class MyClass:
        ...     foo = simpleproperty()
        ...


    The behavior of `foo = simpleproperty()` within a class body is roughly
    outlined in the below example using a `property` descriptor:
        >>> class MyClass:
        ...     @property
        ...     def foo(self):
        ...         return self._foo
        ...
        ...     @foo.setter
        ...     def foo(self, value):
        ...         if hasattr(self, '_foo'):
        ...             raise AttributeError
        ...         self._foo = value

    When accessed, the descriptor returns the value of a similarly-
    named private member on the instance -- That is, a member whose name
    matches the name the descriptor is assigned to, but prefixed with a
    single underscore. Writes to the "public" member are allowed, but
    only if the "private" member is missing. It is otherwise read-only,
    and any attempt to write to the public member are met with
    `AttributeError`:
        >>> my_instance = MyClass()
        >>> my_instance.foo = 'bar'  # WRITABLE
        >>> my_instance.foo
        'bar'
        >>> my_instance.foo = 'BAR'  # READ-ONLY
        Traceback (most recent call last):
            ...
        AttributeError: 'MyClass' object attribute 'foo' is read-only.

    The default setter implementation may not work for all cases, as it
    is usually desirable to transform the value before setting it. The
    descriptor's constructor accepts a custom setter as the first argument,
    allowing it to be used as a decorator:
        >>> class MyClass:
        ...     @simpleproperty
        ...     def foo(self, value):
        ...         self._foo = str(value).lower()
        ...
        >>> my_instance = MyClass()
        >>> my_instance.foo = 'BAR'
        >>> my_instance.foo
        'bar'

    Unlike the outlined `property` simplification above, the logic that
    determines when to perform the set is actually decoupled from the setter
    itself. The descriptor determines *when* to invoke the setter, and the
    setter determines *how* to set the value. That is, if the descriptor
    determines the public member is read-only (i.e. `my_instance._foo` exists),
    it won't call the setter.

    When accessing the public member, the "getter" used by the descriptor
    first checks the instance dictionary for the private member. If it is not
    found, the result of calling `getattr(instance, '_member')` is returned.

    The "getter" used by the descriptor is static; it cannot be configured nor
    can a new one be set. If your use-case extends beyond the capacity of this
    simple descriptor, it is best to use a `property` instead.

    When setting `simpleproperty` descriptors on an existing class, you must
    manually call the `.__set_name__` method to fully initialize the descriptor
    (Python does this automatically DURING class creation). Otherwise,
    `RuntimeError` may be thrown when attempting to access the target member.

    The descriptor works for slotted classes. However, the class must define,
    inherit, or slot the "private" target member.
    """
    __slots__ = ('name',)

    def __init__(self, fset: Callable[[Any, Any], _T] | None = None):
        self.__wrapped__ = fset
        self.name = ''

    def __set_name__(self, cls: type, name: str):
        super().__set_name__(cls, name)
        name = f"_{name}"
        if '__slots__' in cls.__dict__:
            slots = set(itertools.chain(getattr(b, '__slots__', ()) for b in cls.mro()))
            if name not in slots and getattr(cls, name, _SENTINEL) is _SENTINEL:
                raise ValueError(
                    f"slotted class {cls.__qualname__!r} does not include, inherit, "
                    f"or define non-public member {name!r}."
                )
        self.name = name

    def __get__(self, instance: Any, cls: type | None = None) -> _T:
        try:
            return instance.__dict__[self.name]
        except AttributeError:
            if instance is None:
                return self  # type: ignore
            elif not self.name:
                raise RuntimeError(
                    f'{type(self).__qualname__!r} descriptor not fully initialized '
                    f'-- did you forget to call `__set_name__`?'
                )
            return getattr(instance, self.name)
        except KeyError:
            if self.name:
                raise AttributeError(
                    f'{type(instance).__qualname__!r} object has no attribute '
                    f'{self.name[1:]!r}.'
                ) from None
            raise

    def __set__(self, instance: Any, value: Any) -> None:
        if hasattr(instance, self.name):
            raise AttributeError(
                f'{type(instance).__qualname__!r} object attribute {self.name[1:]!r} is read-only.'
            )
        if self.__wrapped__ is None:
            setattr(instance, self.name, value)
        else:
            self.__wrapped__(instance, value)

    def __copy__(self) -> typing.Self:
        copy = type(self)(self.__wrapped__)
        copy.name = self.name
        return copy

    def setter(self, fset: Callable[[Any, Any], Any] | None) -> typing.Self:
        copy = self.__copy__()
        copy.__wrapped__ = fset
        return copy


class Locker(typing.Generic[_T]):
    """A mutex-like object that encapsulates a value that is to be managed
    only between select callables.
    """
    __slots__ = (
        'value',
        '__lock',
    )

    def __init__(self, default_value: _T):
        self.value  = default_value
        self.__lock = Lock()

    def __enter__(self):
        self.__lock.acquire()

    def __exit__(self, *args):
        self.__lock.release()

    def aquire(self):
        self.__lock.acquire()

    def release(self):
        self.__lock.release()

    def bind(self, fn: Callable[typing.Concatenate[typing.Self, _P], _O]) -> Callable[_P, _O]:
        """Return a callable as a method bound to this object. Can be used
        as a decorator."""
        return typing.cast(Callable[_P, _O], types.MethodType(fn, self))

    __call__ = bind




# reentrant locks work better with debuggers
# XXX: BEWARE -- this may mask deadlocks in release builds!
Lock = threading.Lock if not sys.gettrace() else threading.RLock


class Py_TPFLAG(enum.IntFlag):
    HAVE_FINALIZE            = 1 <<  0
    STATIC_BUILTIN           = 1 <<  1   # undocumented
    MANAGED_WEAKREF          = 1 <<  3
    MANAGED_DICT             = 1 <<  4
    SEQUENCE                 = 1 <<  5
    MAPPING                  = 1 <<  6
    DISALLOW_INSTANTIATION   = 1 <<  7
    IMMUTABLETYPE            = 1 <<  8
    HEAPTYPE                 = 1 <<  9
    BASETYPE                 = 1 << 10
    HAVE_VECTORCALL          = 1 << 11
    READY                    = 1 << 12
    READYING                 = 1 << 13
    HAVE_GC                  = 1 << 14
    HAVE_STACKLESS_EXTENSION = 1 << 15
    METHOD_DESCRIPTOR        = 1 << 17
    HAVE_VERSION_TAG         = 1 << 18
    VALID_VERSION_TAG        = 1 << 19
    IS_ABSTRACT              = 1 << 20
    MATCH_SELF               = 1 << 22  # undocumented
    ITEMS_AT_END             = 1 << 23
    LONG_SUBCLASS            = 1 << 24
    LIST_SUBCLASS            = 1 << 25
    TUPLE_SUBCLASS           = 1 << 26
    BYTES_SUBCLASS           = 1 << 27
    UNICODE_SUBCLASS         = 1 << 28
    DICT_SUBCLASS            = 1 << 29
    BASE_EXC_SUBCLASS        = 1 << 30
    TYPE_SUBCLASS            = 1 << 31

    @classmethod
    def get_tp_flags(cls, tp: type) -> tuple['Py_TPFLAG', ...]:
        return tuple(f for f in cls.__members__.values() if tp.__flags__ & f)


# used to cork c-extension memory leaks
@cfunction(ctypes.pythonapi.Py_DecRef, (ctypes.py_object,))
def Py_DECREF(_object: Any) -> None:
    """Reduce the reference count of a Python object by one.

    An object may be deconstructed (garbage collected) when its
    reference count reaches zero.
    """
