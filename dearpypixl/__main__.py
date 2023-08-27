import types
import inspect
from inspect import Parameter
from typing import Any, Mapping
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
    common.Property,
    common.Any,
    common.Color,
    common.Point,
))

interface_imports = mkstub.Imported(interface)
interface_imports.extend((
    o for o in mkstub.Exported.fetch(interface).values()
    if isinstance(o, type)
    and issubclass(o, interface.AppItemType)
))




def fetch_exports(module: types.ModuleType) -> Mapping[str, Any]:
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

        init_params = inspect.signature(tp.__init__).parameters
        icmd_params = init_params.copy()
        del icmd_params['self']

        init_p_src       = mkstub.to_source_parameters(init_params)
        configuration_rt = mkstub.object_annotation(
            inspect.signature(tp.configuration).return_annotation
        )
        pyi.extend((
            indent(f"def {tp.__init__.__name__}({init_p_src}) -> None: ..."),
            indent(f"@staticmethod"),
            indent(f"def command({mkstub.to_source_parameters(icmd_params)}) -> Item: ..."),
            indent(f"def configuration(self) -> {configuration_rt}: ...")
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
    for name, itp in fetch_exports(items).items():
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




def _to_source_itp_element(tp: type[interface.AppItemType]):
    return _to_source_itp_base(tp).split("def __init__")[0]

def _theme_element_pyi(fpath: str | Path, module: types.ModuleType):
    itp_imports = interface_imports.copy()
    itp_imports.extend((interface.ThemeColor, interface.ThemeStyle))

    pyi_imp = '\n'.join((
        str(typing_imports),
        str(itp_imports),
    ))
    pyi_src = "\n\n".join(
        _to_source_itp_element(itp)
        for itp in fetch_exports(module).values()
    )
    pyi = "".join((pyi_imp, "\n\n\n", pyi_src))
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
