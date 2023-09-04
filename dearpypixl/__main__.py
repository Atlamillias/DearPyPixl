import types
import inspect
from inspect import Parameter
from typing import Any, Mapping, get_overloads
from pathlib import Path
from ._dearpypixl import common, interface, mkstub
from ._dearpypixl.mkstub import indent


try:
    DPX_PATH = Path(__file__).parent.resolve()
except AttributeError:
    DPX_PATH = Path().resolve()

typing_imports = mkstub.Imported(common, False)
typing_imports.extend((
    common.Item,
    common.ItemAlias,
    common.ItemUUID,
    common.ItemCommand,
    common.Array,
    common.Literal,
    common.Sequence,
    common.Callable,
    common.Unpack,
    common.Property,
    common.Any,
    common.Color,
    common.Point,
    common.overload,
))

interface_imports = mkstub.Imported(interface)
interface_imports.extend((
    o for o in mkstub.Exported.fetch(interface).values()
    if isinstance(o, type)
    and issubclass(o, interface.AppItemType)
))




def fetch_exports(module: types.ModuleType):
    return mkstub.Exported.fetch(module)


def write_stub(filename: Path | str, source: str) -> None:
    #mkstub.validate_source(source)
    with open(DPX_PATH / filename, 'w') as typestub:
        typestub.write(source)




def _to_source_itp_base(tp: type[interface.AppItemType]) -> str:
    pyi = [mkstub.to_source_classdef(tp)]

    with indent:
        for name, anno in getattr(tp, 'configure').__annotations__.items():
            value = getattr(tp, name, Parameter.empty)
            if value is Parameter.empty or not hasattr(value, '__get__'):
                continue
            anno = mkstub.object_annotation(anno)
            pyi.append(
                indent(f"{name}: {common.Property.__qualname__}[{anno}] = ...")
            )

        init_overloads = get_overloads(tp.__init__)
        if init_overloads:
            for fn in init_overloads:
                init_params = inspect.signature(fn).parameters
                init_p_src  = mkstub.to_source_parameters(init_params)
                pyi.extend((
                    indent(f'@overload'),
                    indent(f"def __init__({mkstub.to_source_parameters(init_params)}) -> None: ..."),
                ))

        else:
            init_params = inspect.signature(tp.__init__).parameters
            init_p_src  = mkstub.to_source_parameters(init_params)
            icmd_params = init_params.copy()
            del icmd_params['self']

            pyi.extend((
                indent(f"def __init__({init_p_src}) -> None: ..."),
                indent(f"@staticmethod"),
                indent(f"def command({mkstub.to_source_parameters(icmd_params)}) -> Item: ..."),
            ))

        configure_params = inspect.signature(tp.configure).parameters
        configuration_rt = mkstub.object_annotation(
            inspect.signature(tp.configuration).return_annotation
        )
        pyi.extend((
            indent(f"def configure({mkstub.to_source_parameters(configure_params)}) -> None: ..."),
            indent(f"def configuration(self) -> {configuration_rt}: ..."),
        ))
    return '\n'.join(pyi)


def items_pyi(fpath: str | Path):
    from . import items

    itp_imports = interface_imports.copy()
    itp_imports.append(interface.mvAll, export=True)
    itp_imports.extend((
        o for o in fetch_exports(interface).values()
        if not (isinstance(o, type) and issubclass(o, interface.AppItemType))
    ), export=True)

    pyi_imp = '\n'.join((
        str(typing_imports),
        str(itp_imports),
        '\n\n\n\n'
    ))

    pyi_src1 = []
    pyi_src2 = []
    exports = fetch_exports(items)
    # TODO: use new '__aliased__' member in exports
    for name, itp in exports.items():
        if name == itp.__qualname__:
            pyi_src1.append(_to_source_itp_base(itp))
        else:
            pyi_src2.append(f"{name} = {itp.__qualname__}")
    pyi_src2.sort()

    pyi = ''.join((
        pyi_imp,
        '\n\n\n'.join(pyi_src1),
        "\n\n\n\n",
        '\n'.join(pyi_src2),
    ))
    write_stub(fpath, pyi)


def _theme_element_pyi(fpath: str | Path, module: types.ModuleType):
    from . import items

    item_imports = mkstub.Imported(items)
    item_imports.extend((
        items.mvThemeColor,
        'ThemeColor',
        items.mvThemeStyle,
        'ThemeStyle',
    ), export=True)

    pyi_imp = '\n'.join((
        str(typing_imports),
        str(interface_imports),
        str(item_imports),
    ))

    exports = fetch_exports(module)
    aliases = exports.aliased
    pyi_src1 = "\n\n\n".join(
        mkstub.to_source_function(itp)
        for itp in exports.values()
    )
    pyi_src2 = '\n'.join(
        f"{name} = {obj.__name__}" for name, obj in aliases.items()
    )
    pyi = "".join((pyi_imp, "\n\n\n", pyi_src1, '\n\n\n', pyi_src2))
    write_stub(fpath, pyi)


def color_pyi(fpath: str | Path):
    from . import color
    _theme_element_pyi(fpath, color)


def style_pyi(fpath: str | Path):
    from . import style
    _theme_element_pyi(fpath, style)




items_pyi("items.pyi")
color_pyi("color.pyi")
style_pyi("style.pyi")
