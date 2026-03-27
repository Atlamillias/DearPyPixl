""":meta private:"""
import sys
import types
import typing


__all__ = ()



type _SourceStrings = typing.Sequence[str]



_MISSING = object()


_DEFAULT_MODULE = types.ModuleType(f"<module>")
_DEFAULT_MODULE.__dict__.update(globals())

_DEFAULT_LOCALS = {}

def create_function(
    name: str,
    args: _SourceStrings,
    body: _SourceStrings,
    module: str = '',
    *,
    return_type: typing.Any = _MISSING,
    globals: dict[str, typing.Any] | None = None,
    locals: dict[str, typing.Any] | None = None,
) -> typing.Callable:
    if isinstance(args, str):
        args = args.split(",")
    if isinstance(body, str):
        body = (body,)

    body = '\n'.join(f'        {line}' for line in body)

    if return_type is not _MISSING:
        if locals is None:
            locals = _DEFAULT_LOCALS

        locals = dict(locals)
        locals["_return_type"] = return_type

        ret_src = " -> _return_type"
    else:
        if locals is None:
            locals = _DEFAULT_LOCALS

        ret_src = ''

    if globals is None:
        if module in sys.modules:
            globals = sys.modules[module].__dict__
        else:
            globals = _DEFAULT_MODULE.__dict__

    closure = (
        f"def __create_function__({', '.join(locals)}):\n"
        f"    def {name}({','.join(args)}){ret_src}:\n{body}\n"
        f"    return {name}"
    )

    scope = {}
    exec(closure, globals, scope)

    fn = scope["__create_function__"](**locals)
    fn.__module__   = module or _DEFAULT_MODULE.__name__
    fn.__qualname__ = fn.__name__ = name

    return fn


FGET_SOURCE_ARGS = FDEL_SOURCE_ARGS = ("self",)
FSET_SOURCE_ARGS = ("self", "value",)


def create_property(
    fget_body: _SourceStrings,
    fset_body: _SourceStrings | None = None,
    fdel_body: _SourceStrings | None = None,
    doc: str | None = None,
    *,
    module: str = '',
    globals: dict[str, typing.Any] | None = None,
    locals: dict[str, typing.Any] | None = None,
) -> property:
    fget = create_function(
        "getter", FGET_SOURCE_ARGS, fget_body, module, globals=globals, locals=locals
    )

    if fset_body is not None:
        fset = create_function(
            "setter", FSET_SOURCE_ARGS, fset_body, module, globals=globals, locals=locals
        )
    else:
        fset = None

    if fdel_body is not None:
        fdel = create_function(
            "deleter", FDEL_SOURCE_ARGS, fdel_body, module, globals=globals, locals=locals
        )
    else:
        fdel = None

    return property(fget, fset, fdel, doc)  # type: ignore


class DescriptorDelegate:
    __slots__ = ("factory",)

    def __init__(self, factory: typing.Callable[[str], typing.Any], /):
        self.factory = factory

    def __get__(self, instance=None, cls=None):
        return self

    def __set_name__(self, cls, name):
        prop = self.factory(name)
        setattr(cls, name, prop)
