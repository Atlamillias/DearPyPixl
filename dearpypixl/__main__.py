import sys
# only run when dearpypixl is ran as a module
if __name__ != '__main__':
    sys.exit()

from typing import Any, Sequence, Self
import textwrap
import ast
import types
import pathlib
import inspect
import warnings
import dearpygui as dearpygui_pkg
import dearpygui.dearpygui as dearpygui
import dearpypixl
from dearpypixl import px_typing, px_items, px_utils, px_theme



PKG_DIR = pathlib.Path(__file__).parent

########################################
######## SOURCE CODE FORMATTING ########
########################################

def _get_obj_name(obj: Any) -> str:
    if isinstance(obj, str):
        return obj
    try:
        is_cls = issubclass(obj, (object, type))
    except:
        is_cls = False
    if is_cls:
        return obj.__qualname__.split(".")[-1]  # typing.<obj>
    try:
        has_name = obj.__name__
    except AttributeError:
        has_name = False
    if has_name:
        return obj.__name__
    return str(obj)

def _fmt_docstring(s: str) -> str:
    if not s:
        return ""
    s = s.strip("'\"").strip()
    return f'"""{s}"""\n\n'

def _fmt_imports(sequence: Sequence[str]) -> str:
    return '\n'.join(s.strip() for s in sequence) + "\n\n\n"

def _fmt_alldundr(s: str):
    if not s:
        return ""
    return s.strip() + "\n\n\n\n\n"


def mfc_rel_import_str(src_ns: types.ModuleType, *imports: Any, wrap_at: int = 5) -> str:
    preface = f"from {src_ns.__name__.replace(dearpypixl.__name__, '')}"
    inames  = [_get_obj_name(iobj) for iobj in imports]

    if len(imports) >= wrap_at:
        names = ',\n    '.join(inames)
        pstface = f"import (\n    {names}\n)"
    else:
        pstface = f"import {', '.join(inames)}"
    return f"{preface} {pstface}\n"


def mfc_alldundr(*exports: Any, wrap_at: int = 5) -> str:
    enames = [repr(_get_obj_name(eobj)) for eobj in exports]
    if len(exports) >= wrap_at:
        names = ',\n    '.join(enames)
        return f"__all__ = [\n    {names}\n]\n"
    return f"__all__ = [{', '.join(enames)}]\n"




########################################
######### GENERATOR BASE CLASS #########
########################################

def _get_itpmixins():
    basetp = px_items.AppItemType
    excltp = px_items.PatchedItem
    mixins = {}
    for attr in dir(px_items):
        obj = getattr(px_items, attr)
        is_itemtype = False
        try:
            is_itemtype = issubclass(obj, basetp)
        except:
            continue
        is_excluded = issubclass(obj, excltp)
        if is_itemtype and not is_excluded:
            mixins[obj.__qualname__] = obj
    return mixins


def _mfc_itemtypes(*, verbose: bool = True, ignore_errors: bool = True):
    from dearpypixl.px_items import itp_from_callable, AppItemType
    from dearpypixl.px_utils import is_item_cmd, is_ctxmgr_fn

    itemtypes: dict[str, type[AppItemType]] = {}
    for attr in dir(dearpygui):
        obj = getattr(dearpygui, attr)
        if not is_item_cmd(obj) or is_ctxmgr_fn(obj):
            continue
        try:
            itemtype = itp_from_callable(obj)
        except Exception as err:
            if not ignore_errors:
                raise
            if verbose:
                warnings.warn(f"Failed to construct itemtype from DearPyGui callable {obj.__name__!r}: {err.args[0]}")
            continue
        itemtypes[itemtype.__qualname__] = itemtype
    return dict(sorted(itemtypes.items()))


class GeneratePy:
    ITEMTYPES = _mfc_itemtypes()
    ITPMIXINS = _get_itpmixins()

    file_generators: list[type[Self]] = []

    def __init_subclass__(cls) -> None:
        if "filepath" in cls.__dict__:
            GeneratePy.file_generators.append(cls)

    @classmethod
    def dump(cls, *,  dst: str = None, verbose: bool = True, ignore_errors: bool = True) -> None:
        # `GeneratePy.dump()` -> all files, `GenPySubclass.dump()` -> one file
        file_generators = cls.file_generators if cls is GeneratePy else (cls,)

        for fg_tp in file_generators:
            fg  = fg_tp()
            src = ''.join([
                _fmt_docstring(fg.docstring),
                _fmt_imports(fg.imports),
                _fmt_alldundr(fg.alldndr),
                fg.content,
            ])
            fpath = pathlib.Path(dst or fg.filepath)
            try:
                ast.parse(src, fpath)
            except SyntaxError as err:
                if not ignore_errors:
                    raise
                if verbose:
                    warnings.warn(f"Generated file is not a valid Python source file {fpath.name!r}: {err.args[0]}")
            else:
                if verbose:
                    print(f"Generated {fpath.name!r} is valid.")
            with open(fpath, "w") as file:
                try:
                    file.write(src)
                except Exception as err:
                    if not ignore_errors:
                        raise
                    if verbose:
                        warnings.warn(f"Could not update source file {fpath.name!r}: {err.args[0]}")
                else:
                    print(f"{fpath.name!r} successfully updated.")

    filepath: str  # pseudo-abstract; every usable class should define this again
    # should populate these attributes on instantiation if not set on the class
    docstring : str           = ""
    imports   : Sequence[str] = ()
    alldndr   : str           = ""
    content   : str           = ""




########################################
######### GENERATOR SUBCLASSES #########
########################################

def _param_to_annotation_str(parameter) -> str:
    # Do not use p.annotation since Parameter().__str__() is really good about
    # formatting already -- specifically the crap in the `typing` module.
    raw_anno_str = str(parameter).split(":", maxsplit=1)[-1].split("=")[0].strip()
    quotes = "'", '"'
    # type alias, like 'ItemId'
    if raw_anno_str[0] in quotes and raw_anno_str[-1] in quotes:
        raw_anno_str = raw_anno_str[1:-1]
    # `List` and "Tuple" are not replaced w/builtins when the class' annotations
    # are "updated" at runtime because it doesn't matter at runtime and isn't worth
    # the trouble. Trivial to do as a string, though.
    raw_anno_str = raw_anno_str.replace("List", "list").replace("Tuple", "tuple")
    return raw_anno_str.split(".")[-1]


def _fmt_cls_docstring(s: str, line_width: int = 92) -> str:
    replacements = (
        ("\t", ""),
        ("Union[int, str]"                      , "int | str"       ),
        ("Union[List[int], Tuple[int, ...]]"    , f"Sequence[int]"  ),
        ("Union[List[float], Tuple[float, ...]]", f"Sequence[float]"),
        ("Union[List[str], Tuple[str, ...]]"    , f"Sequence[str]"  ),
        ("."  , ". "),  # add spaces between sentences, extra whitespace is handled later
    )
    for pair in replacements:
        s = s.replace(*pair)
    rdocstring = s.splitlines()

    _args_idx = rdocstring.index("Args:")
    _rtn_idx  = rdocstring.index("Returns:")

    doc_header = textwrap.fill(
        " ".join(_ln.strip() for ln in rdocstring[:_args_idx] if ln for _ln in ln.split()),
        line_width,
        subsequent_indent="    "
    )
    doc_params = "\n    Args:" + "".join(
        textwrap.fill(f"* {ln}", line_width, initial_indent="\n\n        ",subsequent_indent="        ")
        for ln in [' '.join(ln.strip().split()) for ln in rdocstring[_args_idx+1:_rtn_idx]
                   if ln and "(deprecated)" not in ln]
    )[1:]
    # the return should always be `int | str`
    doc_return = "\n    Returns:\n        *Self*"

    docstring = '\n'.join((doc_header, doc_params, doc_return))
    return docstring


def _mfc_cls_anno_src(parameters) -> str:
    parameters   = px_utils.writable_cfg_from_params(parameters)
    max_char_len = max((len(pname) for pname in parameters))
    return "\n    ".join(
        [f'{p.name.ljust(max_char_len, " ")}: {_param_to_annotation_str(p)}'
         for p in parameters.values()]
    )  + "\n"


def _mfc_mthd_sig_src(parameters) -> str:
    param_strs  = []
    vpos_delimd = False
    vkwd_delimd = False
    for param in parameters.values():
        p_name = param.name
        p_anno = _param_to_annotation_str(param)
        p_dval = f" = {param.default}" if param.default is not param.empty else ""
        # kwd-only syntax PRECEDES
        if not vkwd_delimd and param.kind == param.KEYWORD_ONLY:
            vkwd_delimd = True
            param_strs.append("*")

        if param.kind == param.VAR_KEYWORD:
            param_str = f"**{p_name}"
        elif param.kind == param.VAR_POSITIONAL:
            param_str = f"*{p_name}{': {}'.format(p_anno) if p_anno else ''}"
        else:
            param_str = f"{p_name}{': {}'.format(p_anno) if p_anno else ''}{' = ...' if p_dval else ''}"
        param_strs.append(param_str)

        # pos-only syntax FOLLOWS
        if not vpos_delimd and param.kind == param.POSITIONAL_ONLY:
            vpos_delimd = True
            param_strs.append("/")
    return ', '.join(param_strs)


class AppItemsModule(GeneratePy):
    filepath  = PKG_DIR / "_appitems.py"
    docstring = "Base interface implementations for DearPyGui items."
    imports   = (
        mfc_rel_import_str(dearpygui_pkg, dearpygui_pkg),
        mfc_rel_import_str(px_typing, *(
            "ItemId",
            px_typing.Array,
            px_typing.DPGCallback,
            px_typing.Callable,
            px_typing.Sequence,
            px_typing.Any,
            px_typing.typing_overload,
            )
        ),
        mfc_rel_import_str(px_items, *GeneratePy.ITPMIXINS),
    )

    def __init__(self) -> None:
        super().__init__()
        self.alldndr = mfc_alldundr(*self.ITEMTYPES)
        src = []  # makes debugging easier compared to concat. strings

        for itp_name, itp in self.ITEMTYPES.items():
            # class definition
            basenames_src = ', '.join([b.__qualname__ for b in itp.__bases__])
            # class annotations
            init_parameters = inspect.signature(itp).parameters
            cls_annotations = _mfc_cls_anno_src(init_parameters)
            # method signatures
            init_signature_src = _mfc_mthd_sig_src(init_parameters)
            configure_sig_src  = _mfc_mthd_sig_src(px_utils.writable_cfg_from_params(init_parameters))

            class_src = (
                f'class {itp_name}({basenames_src}):\n'
                f'    """{_fmt_cls_docstring(itp.command.__doc__) or ""}\n'
                f'    """\n'
                f'    command  = {dearpygui_pkg.__name__}.{itp.command.__name__}\n'
                f'    identity = {dearpygui_pkg.__name__}.{itp_name}, {itp.identity[1]!r}\n'
                f'    \n'
                f'    {cls_annotations}'
                f'    \n'
                f'    @{px_typing.typing_overload.__name__}\n'
                f'    def __init__(self, {init_signature_src}, **kwargs) -> None: ...\n'
                f'    @{px_typing.typing_overload.__name__}\n'
                f'    def configure(self, {configure_sig_src}, **kwargs) -> None: ...\n'
                f'\n\n'
            )
            # END
            src.append("".join(class_src))
        self.content = ''.join(src)




class TColorModule(GeneratePy):
    filepath  = PKG_DIR / "_tcoloritems.py"
    docstring = "Interfaces for specific DearPyGui theme color items."
    imports   = (
        mfc_rel_import_str(dearpygui_pkg, dearpygui_pkg),
        mfc_rel_import_str(px_theme, "*"),
    )

    def __init__(self) -> None:
        super().__init__()
        theme_itps = self._mfc_theme_itps()
        self.alldndr = mfc_alldundr(*theme_itps)
        src = []
        for itp_name, itp in theme_itps.items():
            # class definition
            basenames_src = ', '.join([b.__qualname__ for b in itp.__bases__])
            class_src = (
                f'class {itp_name}({basenames_src}):\n'
                f'    target = {_get_obj_name(dearpygui_pkg)}.{itp.constant}\n'
                f'\n\n'
            )
            # END
            src.append("".join(class_src))
        self.content = ''.join(src)

    def _mfc_theme_itps(self):
        itemtypes = {}
        for attr in dir(dearpygui):
            if not any(attr.startswith(pfx) for pfx in self.tconst_pfxs):
                continue
            theme_itp = px_theme.itp_from_tconst(attr)
            itemtypes[theme_itp.__qualname__] = theme_itp
        return dict(sorted(itemtypes.items()))

    tconst_pfxs = tuple(pfx for pfx in px_theme._CONSTPFX_TO_BASES if "Col_" in pfx)


class TStyleModule(TColorModule):
    filepath  = PKG_DIR / "_tstyleitems.py"
    docstring = "Interfaces for specific DearPyGui theme style items."

    tconst_pfxs = tuple(pfx for pfx in px_theme._CONSTPFX_TO_BASES if "StyleVar_" in pfx)





GeneratePy.dump(ignore_errors=False)
