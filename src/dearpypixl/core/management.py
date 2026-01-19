import sys
import typing
import types
import functools
import threading

if typing.TYPE_CHECKING:
    from .protocols import Mappable




@typing.overload
def patched[F: typing.Callable](target, /) -> typing.Callable[[F], F]: ...
@typing.overload
def patched[F: typing.Callable](target, replacement: F, /) -> F: ...
def patched[F: typing.Callable](target, replacement=None, /) -> typing.Any:
    def capture_fn(replacement, /):
        replacement = functools.update_wrapper(replacement, target)
        setattr(replacement, "_patched", True)

        module = sys.modules[target.__module__]
        setattr(module, target.__name__, replacement)

        return replacement

    if replacement is None:
        return capture_fn  # type: ignore
    return capture_fn(replacement)




_init_lock = threading.RLock()
_init_wrapped = []


def _unwrap_initializers():
    global initializer, _initialize_dearpygui, _unwrap_initializers, _init_lock, _init_wrapped

    for func in _init_wrapped:
        module = sys.modules[func.__module__]
        owner_name = func.__qualname__ \
            .removesuffix(func.__name__) \
            .rstrip(".") \
            .removeprefix(func.__module__)

        if not owner_name:
            owner = module
        else:
            owner = getattr(module, owner_name)

        setattr(owner, func.__name__, func)

    def initializer(func):
        return func

    def noop():
        pass

    _initialize_dearpygui = _unwrap_initializers = unwrap_initializers = noop

    del _init_lock, _init_wrapped


def _initialize_dearpygui():
    from dearpygui import dearpygui

    dearpygui.create_context()
    try:
        # HACK: the default impl of this function causes a segfault
        # on error and does NOT raise (patched in `application.py`)
        dearpygui.setup_dearpygui()
    except SystemError:
        pass

    _unwrap_initializers()


def initializer[T: typing.Callable](func: T) -> T:  # pyright: ignore[reportRedeclaration]

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            lock = _init_lock
        except NameError:
            return func(*args, **kwargs)

        with lock:
            _initialize_dearpygui()

        return func(*args, **kwargs)

    _init_wrapped.append(func)

    return wrapper   # type: ignore


def unwrap_initializers():
    try:
        lock = _init_lock
    except NameError:
        return _unwrap_initializers()

    with lock:
        _unwrap_initializers()
