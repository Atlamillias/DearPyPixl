import typing
import re
import inspect
import annotationlib

from dearpypixl.core import codegen
from dearpypixl.core import parsing
from dearpypixl.core import protocols
from dearpypixl.core import appitem
from dearpypixl.core import itemtype
from dearpypixl import items




_EVAL_GLOBALS = (
    typing.__dict__ | parsing.__dict__ | protocols.__dict__ | appitem.__dict__ |
    itemtype.__dict__ | items.__dict__
)
_EVAL_GLOBALS = {k:v for k,v in _EVAL_GLOBALS.items() if not k.startswith("_")}


_replace_lookups = re.compile(
    r"(?P<head>(?:[A-Za-z_][A-Za-z_0-9]*\.)+?)(?P<object>[A-Za-z_][A-Za-z_0-9]*)(?P<tail>[\[\],:\s]|$)"
).sub
_replace_typereprs = re.compile(r"(?:'|\")?<class\s'(?P<typename>.+?)'>(?:'|\")?").sub

def _clean_repr(s: str) -> str:
    value = s.replace("NoneType", "None").replace("Ellipsis", "...")
    value = _replace_lookups(r"\g<object>\g<tail>", value)
    value = _replace_typereprs(r"\g<typename>", value)
    return value


def get_typealias_repr(alias):
    try:
        alias_args = alias.__args__
    except AttributeError:
        pass
    else:
        if alias_args:
            args = []
            for arg in alias_args:
                if isinstance(arg, annotationlib.ForwardRef):
                    arg = arg.evaluate(globals=_EVAL_GLOBALS)
                args.append(arg)

            alias = alias.__origin__[*args]

    return _clean_repr(str(alias))


def get_typevar_repr(owner, typevar: typing.TypeVar):
    if typevar.evaluate_bound is not None:
        bound = annotationlib.call_evaluate_function(
            typevar.evaluate_bound, annotationlib.Format.VALUE, owner=owner,
        )
        if bound.__name__ not in _EVAL_GLOBALS and isinstance(bound, typing.TypeAliasType):
            bound = bound.__value__

        anno = f": {annotationlib.type_repr(bound)}"
    else:
        anno = ""

    if typevar.evaluate_default is not None:
        default = annotationlib.call_evaluate_function(
            typevar.evaluate_default, annotationlib.Format.VALUE, owner=owner
        )
        if default.__name__ not in _EVAL_GLOBALS and isinstance(default, typing.TypeAliasType):
            default = default.__value__

        value = f" = {annotationlib.type_repr(default)}"
    else:
        value = ""

    return f"{typevar.__name__}{anno}{value}"


def get_func_repr(func, name: str = '', /):
    deco_repr = ""
    func_repr = ""

    method = func

    func = getattr(method, "__func__", None)

    if func is None:  # unbound method
        func = method

        signature = inspect.signature(func)

        if len(signature.parameters) > 0:
            param = next(iter(signature.parameters.values()))
            if (
                param.name != "self" or
                param.kind not in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD)
            ):
                deco_repr = "@staticmethod\n"
    else:
        signature = inspect.signature(func)
        deco_repr = ("@classmethod\n")

    if not name:
        name = func.__name__

    type_params = getattr(func, "__type_params__", ())
    if type_params:
        param_repr = ''
        for var in type_params:
            param_repr += f"{get_typevar_repr(func, var)},"
        param_repr = param_repr.rstrip(",")
        param_repr = f"[{param_repr}]"
    else:
        param_repr = ""

    func_repr = _clean_repr(f"def {name}{param_repr}{signature}: ...")

    return f"{deco_repr}{func_repr}"


def get_typedef_repr(cls: type, /) -> str:
    buffer = [f"class {cls.__name__}"]

    type_vars = getattr(cls, "__parameters__", None)
    if type_vars:
        buffer.append("[")
        for var in type_vars:
            buffer.append(get_typevar_repr(cls, var))
            buffer.append(", ")
        buffer[-1] = ']'

    type_bases = [
        class_ for class_ in getattr(cls, "__orig_bases__", cls.__bases__)
        if getattr(class_, "__origin__", class_) not in (object, typing.Generic)
    ]
    if type_bases:
        buffer.append("(")

        for obj in type_bases:
            class_ = getattr(obj, "__origin__", None)
            if class_ is not None:
                buffer.append(get_typealias_repr(obj))
            else:
                class_ = obj
                buffer.append(class_.__name__)
            buffer.append(", ")

        buffer[-1] = ')'

    buffer.append(":")

    return _clean_repr("".join(buffer))


def get_property_repr(name: str, prop, /) -> str:
    fget = prop.fget
    if fget is not None:
        getT = get_typealias_repr(inspect.signature(fget).return_annotation)
    else:
        getT = "Never"

    fset = prop.fset
    if fset is not None:
        # TODO: get the hint for `value` and fallback to `getT`
        setT = getT
    else:
        setT = "Never"

    fdel = prop.fdel
    if fdel is not None:
        delT = "Literal[True]"
    else:
        delT = "Literal[False]"

    return f"{name}: Property[{getT}, {setT}, {delT}]"


def write_file(path, source: typing.Iterable[str]):
    with open(path, "w") as file:
        file.write("\n".join(source))




_SOURCE_TEMPLATE = [
    "from typing import *",
    f"from {protocols.__name__} import *",
    f"from {appitem.__name__} import *",
    f"from {itemtype.__name__} import *",
]


def get_items_stub() -> list[str]:
    source = _SOURCE_TEMPLATE.copy()
    source.append(f"from {parsing.__name__} import {parsing.ThemeElementInfo.__name__}")
    source.append("")
    source.append("__all__")
    all_index = len(source) - 1
    source.append("\n")

    __all__ = []

    for name, item_type in items.__dict__.items():
        if not (isinstance(item_type, appitem.AppItemType) and item_type.__name__.startswith("mv")):
            continue

        type_name = item_type.__name__

        if name != type_name:
            source.append(f"{name} = {type_name}\n\n")
            __all__.append(f'"{name}",\n')
            continue

        if item_type.__name__ == "mvDragPayload" or item_type.__name__ == "mvTooltip":
            typedef_repr = f"{get_typedef_repr(item_type)}  # type: ignore"
        else:
            typedef_repr = get_typedef_repr(item_type)

        source.append(typedef_repr)


        buffer = ["__slots__ = ()"]

        # annotations & properties

        members_processed = set()

        for name, anno in annotationlib.get_annotations(item_type, format=annotationlib.Format.VALUE).items():
            buffer.append(f"{name}: {get_typealias_repr(anno)}")
            members_processed.add(f'"{name}",')

        methods = {}
        for name, member in item_type.__dict__.items():
            if name in members_processed or name.startswith("_"):
                continue

            if isinstance(member, property):
                get_property_repr(name, member)

            elif callable(member):
                methods[name] = member

        # methods

        buffer.extend(get_func_repr(item_type.__itemtype_command__, "__itemtype_command__").splitlines())
        methods.pop(item_type.__itemtype_command__.__name__, None)

        buffer.extend(get_func_repr(item_type.create).splitlines())
        methods.pop(item_type.create.__name__, None)

        item_info = item_type.__itemtype_info__

        parameters = [codegen.SELF_PARAMETER]
        parameters.extend(item_info.parameters.writable.values())
        signature = inspect.Signature(parameters, return_annotation=None)
        buffer.append(_clean_repr(f"def configure{signature}: ...  # type: ignore[override]"))
        methods.pop("configure", None)

        dictkeys_repr = ", ".join(f'"{p}"' for p in item_info.parameters.readable)
        buffer.append(_clean_repr(f"def configuration(self) -> dict[Literal[{dictkeys_repr}], Any]: ..."))
        methods.pop("configuration", None)

        for name, method in methods.items():
            overloads = list(typing.get_overloads(method))
            if len(overloads) == 1:
                method = overloads[0]
                overloads = ()

            if overloads:
                for method in typing.get_overloads(method):
                    buffer.append("@overload")
                    buffer.extend(get_func_repr(method, name).splitlines())
            else:
                buffer.extend(get_func_repr(method, name).splitlines())
        methods.clear()

        source.extend(f"    {s}" for s in buffer)
        source.append('')
        buffer.clear()

        # functions

        content = buffer

        signature = inspect.signature(item_type.create).replace(
            return_annotation=inspect.Signature.empty
        )
        for function in (item_info.function2, item_info.function):
            if function is None:
                continue

            s = f"def {function.__name__}[U: Any]{signature} -> {item_type.__name__}[U]: ..."
            s = _clean_repr(s).replace("user_data: Any", "user_data: U")
            source.append(s)

            content.append(function.__name__)

        source.append("\n")

        # __all__

        content.insert(0, type_name)
        __all__.append(f'{(", ".join(repr(s) for s in content))},')
        content.clear()

    __all__ = ("__all__ = (\n    " + "\n    ".join(__all__).rstrip(", ") + "\n)\n").splitlines()
    source = [*source[:all_index], *__all__, *source[all_index+1:]]

    return source


def _get_elements_stub(module, element_info: typing.Mapping[str, parsing.ThemeElementInfo]) -> list[str]:
    source = _SOURCE_TEMPLATE.copy()
    source.append(f"from {items.__name__} import mvTheme as mvTheme")
    source.append(f"from {items.__name__} import mvThemeComponent as mvThemeComponent")
    source.append(f"from {items.__name__} import mvThemeColor as mvThemeColor")
    source.append(f"from {items.__name__} import mvThemeStyle as mvThemeStyle")
    source.append("")
    source.append("__all__")
    all_index = len(source) - 1
    source.append("\n")

    __all__ = []

    for name, info in element_info.items():
        func_name = info.func_name
        for overload in typing.get_overloads(getattr(module, func_name)):
            source.append("@overload")
            source.extend(get_func_repr(overload, func_name).splitlines())

        __all__.append(f'"{func_name}",')
        source.append('')

    __all__ = ("__all__ = (\n    " + "\n    ".join(__all__).rstrip(", ") + "\n)\n").splitlines()
    source = [*source[:all_index], *__all__, *source[all_index+1:]]

    return source

def get_colors_stub() -> list[str]:
    return _get_elements_stub(color, parsing.theme_color_info())

def get_styles_stub() -> list[str]:
    return _get_elements_stub(style, parsing.theme_style_info())




if __name__ == "__main__":
    from pathlib import Path

    from dearpypixl import color
    from dearpypixl import style

    for module, func in zip((items, color, style), (get_items_stub, get_colors_stub, get_styles_stub)):
        stub = func()
        write_file(Path(module.__file__).with_suffix(".pyi"), stub)
