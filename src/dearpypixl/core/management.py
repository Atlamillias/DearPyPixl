""":meta private:"""
import typing
import os
import sys
import operator
import functools
import threading
from warnings import warn


__all__ = ()


_dearpygui_version = os.getenv("_DPX_DEARPYGUI_VERSION")
if _dearpygui_version is None:
    import importlib.metadata
    _dearpygui_version = os.environ["_DPX_DEARPYGUI_VERSION"] = importlib.metadata.version('dearpygui')

DEARPYGUI_VERSION = tuple(int(d) for d in _dearpygui_version.split(".")); del _dearpygui_version




_ENVIRONS = {}

ENVIRONS = type(int.__dict__)(_ENVIRONS)

@typing.overload
def register_environ[T: bool | int | str](env: str, doc: str, valtype: type[T], default: T) -> T: ...  # ty:ignore[invalid-overload]
def register_environ(env, doc=None, /, valtype=bool, default=None, *, __defaults_map={bool: False, int: 0, str: ''}):
    var = env.upper()
    if var in _ENVIRONS:
        raise ValueError(f"{env!r} already registered")

    _ENVIRONS[var] = doc

    res = os.getenv(env)

    if res is None:
        return default

    res = res.strip().lower()  # type: ignore

    if valtype is str:
        return res

    match res:
        case '' | "false" | '0' | "none" | "null":
            res = 0
        case '1' | "true":
            res = 1
        case _:
            try:
                res = int(res)
            except (TypeError, ValueError):
                warn(f"Unknown value {os.getenv(env)!r} for environment variable {env!r}.")
                return default

    if valtype is bool:
        return bool(res)

    return res




_DPX_NO_INIT = typing.cast(
    typing.Literal[False],
    register_environ(
        "_DPX_NO_INIT",
        "When set, DearPyPixl's basic libraries are not loaded on import (internal only).",
        bool,
        False
    )
)




_DPX_NO_WARNINGS = register_environ(
    "DPX_NO_WARNINGS",
    "When set, most warnings issued by DearPyPixl are disabled.",
    bool,
    False
)

if _DPX_NO_WARNINGS:

    def warn(
        message: str,
        category: type[Warning] | None = None,
        stacklevel: int = 1,
        source: typing.Any | None = None,
        *,
        skip_file_prefixes: tuple[str, ...] = ()
    ) -> None:
        return




_DPX_NO_PATCH = register_environ(
    "DPX_NO_PATCH",
    "When set, DearPyPixl will not apply DearPyGui patches (expect nearly all "
    "DearPyPixl code that that interacts with DearPyGui's global state to fail "
    "— would NOT recommend).",
    bool,
    False
)

type _Version = tuple[int, ...]

@typing.overload
def patch[F: typing.Callable](target, /, *, cond: bool | int = ..., lt: _Version = ..., le: _Version = ..., gt: _Version = ..., ge: _Version = ...) -> typing.Callable[[F], F]: ...
@typing.overload
def patch[F: typing.Callable](target, replacement: F, /, *, cond: bool = ..., lt: _Version = ..., le: _Version = ..., gt: _Version = ..., ge: _Version = ...) -> F: ...
def patch[F: typing.Callable](target, replacement=None, /, **kwargs) -> typing.Any:

    def capture_fn(replacement, /):
        if not hasattr(replacement, "_patched"):
            doc = replacement.__doc__

            replacement = functools.update_wrapper(replacement, target)

            if doc:  # restore original docstring
                replacement.__doc__ = doc

        if patch:
            module = sys.modules[target.__module__]
            setattr(module, target.__name__, replacement)

        setattr(replacement, "_patched", patch)

        return replacement

    patch = kwargs.pop("cond", not _DPX_NO_PATCH )
    if patch:
        while kwargs:
            comparer, version = kwargs.popitem()

            patch = getattr(operator, comparer)(DEARPYGUI_VERSION, version)
            if not patch:
                break

    if replacement is None:
        return capture_fn
    return capture_fn(replacement)




_DPX_NO_DEARPYGUI_AUTO_INIT = register_environ(
    "DPX_NO_DEARPYGUI_AUTO_INIT",
    "When set, prevents DearPyPixl from implicitly initializing "
    "DearPyGui via `create_context()` and `setup_dearpygui()` where "
    "applicable (e.g. creating the first item interface, creating "
    "the viewport, etc).",
    bool,
    False,
)

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

    _initialize_dearpygui = _unwrap_initializers = unwrap_initializers = noop  # ty:ignore[invalid-assignment]

    del _init_lock, _init_wrapped


def _initialize_dearpygui():
    from dearpygui import dearpygui

    if not _DPX_NO_DEARPYGUI_AUTO_INIT:
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



@typing.overload
def cast_signature[T: typing.Callable](wrapped: T, /) -> typing.Callable[[typing.Any], T]: ...
@typing.overload
def cast_signature[**P, T](wrapped: typing.Callable[P, typing.Any], return_type: T, /) -> typing.Callable[[typing.Any], typing.Callable[P, T]]: ...
def cast_signature(wrapped, return_type=None, /):
    def get_wrapper(wrapper, /):
        return wrapper
    return get_wrapper
