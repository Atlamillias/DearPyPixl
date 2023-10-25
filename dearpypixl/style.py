import inspect
from . import _typing, _parsing, _tools, _mkstub
from ._typing import overload, Item, Color, Any, Array
from .items import mvThemeColor, ThemeColor, mvThemeStyle, ThemeStyle


def _init_module():
    overloads = _typing.get_overloads(_add_theme_element)

    p_kwargs = inspect.Parameter('kwargs', inspect.Parameter.VAR_KEYWORD)

    for ovld in overloads:
        try:
            ovld_sig = ovld.__signature__
        except AttributeError:
            ovld_sig = inspect.signature(ovld)
        try:
            kwargs_sig = _ITP_BASE.configure.__signature__
        except AttributeError:
            kwargs_sig = _ITP_BASE.configure.__signature__ = inspect.signature(
                _ITP_BASE.configure
        )

        ovld_args = {
            n:p for n, p in ovld_sig.parameters.items()
            if p.kind is p.POSITIONAL_ONLY
        }
        ovld_kwds = {
            n:p for n, p in kwargs_sig.parameters.items()
            if n not in ovld_args
            and p.kind in (p.POSITIONAL_OR_KEYWORD, p.KEYWORD_ONLY)}
        ovld_kwds['kwargs'] = p_kwargs
        ovld_kwds.pop('self', None)
        ovld_kwds.pop('cls', None)
        ovld.__signature__ = ovld_sig.replace(
            parameters=list((ovld_args | ovld_kwds).values())
        )

    exported = _mkstub.Exported(__name__)

    ns = {}
    for elem_def in _parsing.style_definitions().values():
        fn = _tools.create_function(
            elem_def.name2, _DFN_ARGS,
            _DFN_BODY,
            _ITP_BASE,
            globals=globals(),
            locals={
                'itp'      : _ITP_BASE,
                'category' : int(elem_def.category),
                'target'   : elem_def.target,
            }
        )
        fn.__module__ = __name__

        # HACK: force register existing overloads
        for ovld in overloads:
            ovld.__name__     = fn.__name__
            ovld.__qualname__ = fn.__qualname__
            overload(ovld)

        exported[fn.__name__] = fn
        exported.aliased[elem_def.name1] = fn
        ns[elem_def.name2] = ns[elem_def.name1] = fn

    globals().update(ns)




_ITP_BASE = mvThemeStyle
_DFN_ARGS = ('value: Any = 1', 'y: Any = -1', '/', '**kwargs')
_DFN_BODY = (
    "if isinstance(value, (int, float)):",
    "    x = value",
    "else:",
    "    x, y = value",
    "kwargs.update(",
    "    target=target,",
    "    x=x,",
    "    y=y,",
    "    category=category,",
    ")",
    "return itp(**kwargs)",
)


@overload
def _add_theme_element(value: Array[float, float] = ..., /, **kwargs) -> _ITP_BASE: ...
@overload
def _add_theme_element(x: float = ..., y: float = ..., /, **kwargs) -> _ITP_BASE: ...
def _add_theme_element(value: Any = 1, y: Any = -1, /, **kwargs) -> _ITP_BASE: ...

_init_module()
