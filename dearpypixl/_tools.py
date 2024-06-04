import sys
import abc
import time
import enum
import types
import ctypes
import typing
import inspect
import itertools
import functools
import threading
from typing import overload, Any, Mapping, Iterable, Callable, Sequence, TypeVar, ParamSpec


P     = ParamSpec("P")
T     = TypeVar("T")
KT    = TypeVar("KT")
VT    = TypeVar("VT")
O     = TypeVar("O")


_SENTINEL = object()





# [Dynamic Code Generation]

def create_module(
    name : str,
    body : Mapping[str, Any] | Iterable[tuple[str, Any]] = (),
    attrs: Mapping[str, Any] | Iterable[tuple[str, Any]] = (),
) -> types.ModuleType:
    """Create a new module object.

    Args:
        - name: Name for the new module.

        - body: Used to update the module's contents/dictionary.

        - attrs: Used to update the module's attributes.
    """
    m = types.ModuleType(name, None)
    for k, v in tuple(attrs):
        setattr(m, k, v)
    m.__dict__.update(body)

    return m


@overload
def create_function(name: str, args: Sequence[str], body: Sequence[str], return_type: T = Any, module: str = '', *, globals: dict[str,  Any] | None = None, locals: Mapping[str,  Any] | Iterable[tuple[str,  Any]] = ()) -> Callable[..., T]: ...  # type: ignore
def create_function(name: str, args: Sequence[str], body: Sequence[str], return_type: T = Any, module: str = '', *, globals: dict[str,  Any] | None = None, locals: Mapping[str,  Any] | Iterable[tuple[str,  Any]] = (), __default_module=create_module('')) -> Callable[..., T]:
    """Compile a new function from source.

    Args:
        * name: Name for the new function.

        * args: A sequence containing argument signatures (as strings)
        for the new function. Each value in *args* should be limited to
        a single argument signature.

        * body: A sequence containing the source that will be executed when
        the when the new function is called. Each value in the sequence should
        be limited to one line of code.

        * return_type: Object to use as the function's return annotation.

        * module: Used to update the function's `__module__` attribute
        and to fetch the appropriate global mapping when *globals* is
        None.

        * globals: The global scope for the new function.

        * locals: The (non)local scope for the new function.


    When *globals* is None, this function will attempt to look up *module*
    in `sys.modules`, and will use the returned module's dictionary as
    *globals* if found. If the module could not be found or both *module*
    and *globals* are unspecified, *globals* defaults to the dictionary of
    a dedicated internal dummy module.

    Note that, when including *locals*, the created function's local scope
    will not be *locals*, but a new mapping created from its' contents.
    However, *globals* is used as-is.

    """
    assert not isinstance(body, str)
    body = '\n'.join(f'        {line}' for line in body)

    locals = dict(locals)
    locals["_return_type"] = return_type

    if globals is None:
        if module in sys.modules:
            globals = sys.modules[module].__dict__
        else:
            globals = __default_module.__dict__

    closure = (
        f"def __create_function__({', '.join(locals)}):\n"
        f"    def {name}({', '.join(args)}) -> _return_type:\n{body}\n"
        f"    return {name}"
    )

    scope = {}
    exec(closure, globals, scope)

    fn = scope["__create_function__"](**locals)
    fn.__module__   = module or __default_module.__name__
    fn.__qualname__ = fn.__name__ = name

    return fn


@typing.final
class _MarkerType(typing.Protocol):
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __delattr__(self, name: str) -> TypeError: ...
    def __setattr__(self, name: str, value: Any) -> TypeError: ...


def create_marker_type(name: str, module: str, *, body: Mapping[str, Any] | Sequence[tuple[str, Any]] = ()) -> type[_MarkerType]:
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
    module = sys.modules[module]  # type: ignore

    namespace = {
        '__module__': module.__name__,  # type: ignore
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
    type(cls).__new__ = create_function(  # type: ignore
        '__new__',
        ('*args', '**kwargs'),
        (f"raise TypeError(\"one or more bases cannot be subclassed.\")",),
        globals=module.__dict__,
    )
    return typing.final(cls)


def frozen_namespace(cls: type[T]) -> type[T]:
    contents = tuple(m for m in dir(cls) if not m.startswith('_'))
    return create_marker_type(  # type: ignore
        cls.__qualname__,
        cls.__module__,
        body={
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



# [Inspection Tools]

class PyTypeFlag(enum.IntFlag):
    """Python type bit masks (`type.__flags__`, `PyTypeObject.tp_flags`).

    A type's flag bit mask is created when the object is defined --
    changing it from Python does nothing helpful.
    """
    STATIC_BUILTIN           = (1 << 1)  # (undocumented, internal)
    MANAGED_WEAKREF          = (1 << 3)
    MANAGED_DICT             = (1 << 4)
    PREHEADER                = (MANAGED_WEAKREF | MANAGED_DICT)
    SEQUENCE                 = (1 << 5)
    MAPPING                  = (1 << 6)
    DISALLOW_INSTANTIATION   = (1 << 7)  # `tp_new == NULL`
    IMMUTABLETYPE            = (1 << 8)
    HEAPTYPE                 = (1 << 9)
    BASETYPE                 = (1 << 10)  # allows subclassing
    HAVE_VECTORCALL          = (1 << 11)
    READY                    = (1 << 12)  # fully constructed type
    READYING                 = (1 << 13)  # type is under construction
    HAVE_GC                  = (1 << 14)  # allow garbage collection
    HAVE_STACKLESS_EXTENSION = (3 << 15)  # Stackless Python
    METHOD_DESCRIPTOR        = (1 << 17)  # behaves like unbound methods
    VALID_VERSION_TAG        = (1 << 19)  # has up-to-date type attribute cache
    ABSTRACT                 = (1 << 20)  # `ABCMeta.__new__`
    MATCH_SELF               = (1 << 22)  # "builtin" class pattern-matting behavior (undocumented, internal)
    ITEMS_AT_END             = (1 << 23)  # items at tail end of instance memory
    LONG_SUBCLASS            = (1 << 24)  # |- used for `Py<type>_Check`, `isinstance`, `issubclass`
    LIST_SUBCLASS            = (1 << 25)  # |
    TUPLE_SUBCLASS           = (1 << 26)  # |
    BYTES_SUBCLASS           = (1 << 27)  # |
    UNICODE_SUBCLASS         = (1 << 28)  # |
    DICT_SUBCLASS            = (1 << 29)  # |
    BASE_EXC_SUBCLASS        = (1 << 30)  # |
    TYPE_SUBCLASS            = (1 << 31)  # |


def has_feature(cls: type[Any], flag: int | PyTypeFlag):
    """Python implementation of CPython's `PyType_HasFeature` macro."""
    return bool(cls.__flags__ & flag)


def managed_dict_type(o: Any) -> bool:
    """Check if an instance, or future instances of a class, support
    the dynamic assignment of new members/variables.

    Args:
        - o: Class or instance object to inspect.


    If *o* is an instance object, this function returns True if it has
    a `__dict__` attribute. For class objects; return True if instances
    of that class are expected to have a `__dict__` attribute, instead.

    This function will return False on "slotted" classes if any of its'
    non-builtin bases did not declare `__slots__` at the time of their
    creation.
    """
    if not isinstance(o, type):
        o = type(o)
    return has_feature(o, PyTypeFlag.MANAGED_DICT)


def is_cclass(o: Any):
    """Return True if an object is a class implemented in C."""
    return isinstance(o, type) and not has_feature(o, PyTypeFlag.HEAPTYPE)


def is_cfunction(o: Any) -> bool:
    """Return True if an object is a function implemented in C. This
    includes built-in functions like `len` and `isinstance`, as well
    as those exported in C-extensions.
    """
    return isinstance(o, types.BuiltinFunctionType)


@overload
def is_builtin(o: Any) -> bool: ...  # type: ignore
def is_builtin(o: Any, *, __module=type.__module__) -> bool:
    """Return True if an object is a built-in function or class.

    Unlike `inspect.isbuiltin`, the result of this function is not
    falsified by C-extension objects, and can also identify built-in
    classes.

    Args:
        - o: Object to test.
    """
    try:
        return o.__module__ == __module
    except:
        return False


@overload
def is_mapping(o: Any) -> bool: ...  # type: ignore
def is_mapping(o: Any, *, __key=object()):
    """Return True if an object implements the basic behavior of a
    mapping.

    Useful to validate an object based on protocol rather than type;
    objects need not be derived from `Mapping` to be considered a
    mapping or mapping-like.

    Args:
        - o: Object to test.


    This function returns True if `KeyError` is raised when attempting
    to "key" the object with one it does not contain. The object
    must also implement or inherit the `__len__`, `__iter__`, and
    `__contains__` methods.

    Note that this function only tests/inspects behavior methods,
    and may return True even if an object does implement high-level
    `Mapping` methods such as `.get`.
    """
    # Could also throw it a non-hashable and check for `TypeError`, but
    # it feels more ambiguous than `KeyError` in this context.
    try:
        o[__key]
    except KeyError: pass
    except:
        return False
    return (
        hasattr(o, '__len__')
        and
        hasattr(o, '__contains__')
        and
        hasattr(o, '__iter__')
    )


def is_sequence(o: Any) -> bool:
    """Return True if an object implements the basic behavior of a
    sequence.

    Useful to validate an object based on protocol rather than type;
    objects need not be derived from `Sequence` to be considered a
    sequence or sequence-like.

    Args:
        - o: Object to test.


    This function returns True if `IndexError` is raised when attempting
    to "key" the object with an index outside of its' range. The object
    must also implement or inherit the `__len__`, `__iter__`, and
    `__contains__` methods.

    Note that this function only tests/inspects behavior methods,
    and may return True even if an object does implement high-level
    `Sequence` methods such as `.count` and `.index`.
    """
    try:
        o[len(o)]
    except IndexError: pass
    except:
        return False
    return hasattr(o, '__contains__') and hasattr(o, '__iter__')


def compare_versions(lo: str, comp: typing.Literal['<', '<=', '==', '!=', '>=', '>'], ro: str) -> bool:
    """Simple software version comparison tool.

    Does not follow PEP standards.

    Args:
        * lo: Left operand version string.

        * comp: Rich comparison symbol(s).

        * ro: Right operand version string.
    """
    l_vers = tuple(int(v.strip()) for v in lo.split('.') if v.isdigit())
    r_vers = tuple(int(v.strip()) for v in ro.split('.') if v.isdigit())
    return eval(f'{l_vers} {comp} {r_vers}')




# [ Descriptors ]

class _property(typing.Generic[T], abc.ABC):
    __slots__ = ('__wrapped__',)

    def __init__(self, fget: Callable[..., T]):
        self.__wrapped__ = fget

    def __set_name__(self, cls: type[Any], name: str):
        set_name = getattr(self.__wrapped__, "__set_name__", None)
        if set_name:
            set_name(cls, name)

    @abc.abstractmethod
    def __get__(self, instance: Any, cls: type | None = None) -> T | typing.Self: ...


class classproperty(_property, typing.Generic[T]):
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

    def __get__(self, instance: Any, cls: type[Any]) -> T:
        return self.__wrapped__(cls)


class staticproperty(_property, typing.Generic[T]):
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

    def __get__(self, instance: Any, cls: type[Any]) -> T:
        return self.__wrapped__()


class simpleproperty(_property, typing.Generic[T]):
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

    def __init__(self, fset: Callable[[Any, Any], T] | None = None):
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

    def __get__(self, instance: Any, cls: type | None = None) -> T:
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




# [ Misc ]

Lock = threading.Lock if not sys.gettrace() else threading.RLock


class Locker(typing.Generic[T]):
    """A mutex-like object that encapsulates a value that is to be managed
    only between select callables.
    """
    __slots__ = (
        'value',
        '__lock',
    )

    def __init__(self, default_value: T):
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

    def bind(self, fn: Callable[typing.Concatenate[typing.Self, P], O]) -> Callable[P, O]:
        """Return a callable as a method bound to this object. Can be used
        as a decorator."""
        return typing.cast(Callable[P, O], types.MethodType(fn, self))

    __call__ = bind


def cfunction(pfunction: 'ctypes._NamedFuncPointer', argtypes: tuple[Any, ...] = (), restype: Any = None):
    """Cast a foreign C function pointer as the decorated function.

    *argtypes* and *restypes* will be assigned to *pfunction*.
    """
    def func_prototype(fn_signature: Callable[P, T]) -> Callable[P, T]:
        pfunction.argtypes = argtypes
        pfunction.restype  = restype
        functools.update_wrapper(pfunction, fn_signature, updated='')
        return pfunction  # type: ignore
    return func_prototype


# used to cork c-extension memory leaks
@cfunction(ctypes.pythonapi.Py_DecRef, (ctypes.py_object,))
def Py_DECREF(_object: Any) -> None:
    """Reduce the reference count of a Python object by one.

    An object may be deconstructed (garbage collected) when its
    reference count reaches zero.
    """


def timed(fn: Callable[P, T]) -> Callable[P, T]:
    """Decorator that times the execution of a function."""
    @functools.wraps(fn)
    def wrap(*args: P.args, **kwds: P.kwargs) -> T:
        ts = timer()
        result = fn(*args, **kwds)
        te = timer()
        sig = ', '.join((
            *(repr(v) for v in args),
            *(f"{k}={v!r}" for k,v in kwds.items()),
        ))
        print(f'`{fn.__name__}({sig}) -> ...` took {te-ts} second(s)')
        return result
    timer = time.time
    return wrap


def cache_once(fn: Callable[P, T], /) -> Callable[P, T]:
    """Similar to `functools.cached_property` but for functions. Returns the
    same result regardless of the arguments passed to the decorated function.
    """
    @functools.wraps(fn)
    def cached_result(*args: P.args, **kwargs: P.kwargs) -> T:
        nonlocal cache
        try:
            return cache
        except NameError:
            cache = fn(*args, **kwargs)
            return cache
    cache: T
    return cached_result


@functools.lru_cache(128)
def parameters(c: Callable) -> tuple[inspect.Parameter, ...]:
    """Return the parameters of the given callable. The result
    is cached for future calls.

    Args:
        * c: Callable for the query.
    """
    return tuple(inspect.signature(c).parameters.values())