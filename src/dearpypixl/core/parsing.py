"""Utilities for inspecting Dear PyGui's API."""
import re
import types
import typing
import functools
import threading
import annotationlib
import dataclasses
import importlib.metadata
from inspect import Parameter

from dearpygui import dearpygui

from . import codegen
from .protocols import Item, ItemCommand, ItemCallback

if typing.TYPE_CHECKING:
    from inspect import Parameter




# you can get this through `get_app_configuration()`, but that
# requires creating device context
DEARPYGUI_VERSION = tuple(int(d) for d in importlib.metadata.version('dearpygui').split("."))


# [ helpers ]

_TAG_ANNOTATIONS = (Item, int | str)


def _static_output[T: typing.Callable](fn: T, /) -> T:

    @functools.wraps(fn)
    def cached_result(*args, **kwargs):
        nonlocal result
        try:
            return result
        except NameError:
            result = fn(*args, **kwargs)
            return result

    result: typing.Any

    return cached_result  # type: ignore




# [ API Parsers ]

class _Wrapped[**P, T](typing.Protocol):
    __wrapped__: typing.Callable[P, T]
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> T: ...

def is_contextmanager(o: typing.Any, /) -> typing.TypeIs[_Wrapped]:
    """Return True if a function is wrapped by `contextlib.contextmanager`.

    Args:
        * o: The object to inspect.


    >>> from dearpygui import dearpygui
    >>> is_contextmanager(dearpygui.window)
    True
    >>> is_contextmanager(dearpygui.add_window)
    False
    >>> is_contextmanager(dearpygui.child_window)
    True
    >>> is_contextmanager(dearpygui.add_child_window)
    False
    >>> is_contextmanager(dearpygui.mutex)
    True
    """
    return (
        callable(o) and
        o.__globals__["__name__"] == "contextlib" and
        o.__module__ != "contextlib" and
        isinstance(getattr(o, "__wrapped__", None), types.FunctionType)
    )


def is_item_command(o: typing.Any, /) -> typing.TypeIs['ItemCommand']:
    """Return True if an object is a callable defined in DearPyGui that creates
    and yields/returns an item identifier.

    Only returns True for item commands located in the `dearpygui.dearpygui`,
    not `dearpygui._dearpygui`. Functions in the latter are considered "built-
    in" and have no signature, in which this function returns False.

    Args:
        * o: The object to inspect.


    >>> from dearpygui import dearpygui, _dearpygui
    ...
    >>> is_item_command(dearpygui.window)
    True
    >>> is_item_command(dearpygui.add_window)
    True
    >>> # parsed as a signature-less "built-in"
    >>> is_item_command(_dearpygui.add_window)
    False
    >>> # does not return or accept *tag*
    >>> is_item_command(dearpygui.configure_item)
    False
    >>> def randfunc(*args, tag: int | str = 0) -> int | str: ...
    >>> # not from `dearpygui.dearpygui`
    >>> is_item_command(randfunc)
    False
    """
    # this only works reliably when the function is in `dearpygui`
    # public module because those in the private `_dearpygui` module
    # don't have good signatures
    try:
        signature = codegen.signature(o)
    except:
        return False  # not callable or is "built-in"

    try:
        if dearpygui.__name__ not in o.__module__:
            return False
    except AttributeError:
        return False

    if signature.return_annotation not in _TAG_ANNOTATIONS:
        return False

    try:
        tag = signature.parameters["tag"]
    except KeyError:
        return False
    if tag.kind != Parameter.KEYWORD_ONLY:
        return False

    # we'll use this later
    if not hasattr(o, "__signature__"):
        o.__signature__ = signature
    return True



@dataclasses.dataclass(slots=True, frozen=True)
class ItemParameters:
    creation: dict[str, Parameter] = dataclasses.field(default_factory=dict)
    readable: dict[str, Parameter] = dataclasses.field(default_factory=dict)
    writable: dict[str, Parameter] = dataclasses.field(default_factory=dict)


@dataclasses.dataclass(slots=True)
class ItemTypeInfo:
    namespace = "mvAppItemType"

    type_name: str
    type_uuid: int
    function: ItemCommand
    function2: ItemCommand | None
    container: bool
    root_item: bool = False
    value_type: type | None = dataclasses.field(default=None, repr=False)
    parameters: ItemParameters = dataclasses.field(default_factory=ItemParameters, repr=False)
    parents: tuple[str, ...] | None = dataclasses.field(default=None, repr=False)
    children: tuple[str, ...] | None = dataclasses.field(default=None, repr=False)

    @property
    def type_qualname(self) -> str:
        return f"mvAppItemType::{self.type_name}"


@_static_output
def itemtype_info() -> typing.Mapping[str, ItemTypeInfo]:
    """Parse Dear PyGui's API and return compiled item type definitions.

    The result of this function is only built once and is cached
    for future calls.
    """
    def set_item_types():
        nonlocal name_to_uuid
        dearpygui.create_context()
        name_to_uuid = dearpygui.get_item_types()
        dearpygui.destroy_context()

    name_to_uuid = typing.cast(dict[str, int], None)
    # This needs to be done in a separate thread so the GPU
    # context isn't created too early or burned for the user.
    thread = threading.Thread(target=set_item_types, daemon=True)
    thread.start()
    thread.join()

    name_to_info = {}
    func_to_name = {
        dearpygui.add_2d_histogram_series: "mv2dHistogramSeries",
        dearpygui.add_3d_slider          : "mvSlider3D",
        dearpygui.add_hline_series       : "mvHLineSeries",
        dearpygui.add_vline_series       : "mvVLineSeries",
        dearpygui.add_plot_annotation    : "mvAnnotation",
        dearpygui.add_text_point         : "mvLabelSeries",
        dearpygui.draw_image             : 'mvDrawImage',
        dearpygui.draw_text              : 'mvDrawText',
        dearpygui.draw_rectangle         : "mvDrawRect",
        dearpygui.add_subplots           : 'mvSubPlots',
        dearpygui.add_window             : "mvWindowAppItem",
    }
    object_cache = set()

    ADD_PREFIX  = 'add_'
    DRAW_PREFIX = 'draw_'

    for name, obj in dearpygui.__dict__.items():
        if name.startswith("_") or obj in object_cache:
            continue

        try:
            object_cache.add(obj)
        except TypeError:
            assert getattr(obj, "__hash__", None) is None
            continue

        if not (callable(obj) and is_item_command(obj)):
            continue

        # XXX: should be cached by `is_item_command()`
        signature = obj.__signature__  # type: ignore

        # find item commands and raw type name
        if is_contextmanager(obj):
            try:
                # if the context manager is an item command, a normal
                # function (the one we need) should also exist
                function = (
                    getattr(dearpygui, f"{ADD_PREFIX}{name}", None) or
                    getattr(dearpygui, f"{DRAW_PREFIX}{name}")
                )
                function2 = obj
                container = True
            except AttributeError:
                continue

            if function in object_cache:
                continue
            object_cache.add(function)

            _type_name = name
        else:
            if name.startswith(DRAW_PREFIX):
                _type_name = name.removeprefix(DRAW_PREFIX)
            elif name.startswith(ADD_PREFIX):
                _type_name = name.removeprefix(ADD_PREFIX)
            else:  # shouldn't get here
                assert not is_item_command(obj)
                continue

            function2 = getattr(dearpygui, _type_name, None)
            container = is_contextmanager(function2)
            if not container:
                function2 = None
            function = obj

        # determine the item type name
        if function in func_to_name:
            type_name = func_to_name[function]
            type_uuid = name_to_uuid[type_name]
        else:
            if _type_name.startswith("colormap"):
                _type_name = _type_name.replace("colormap", "color_map", 1)
            type_name = f'mv{_type_name.title().replace("_", "")}'
            try:
                type_uuid = name_to_uuid[type_name]
            except KeyError:
                # drawing item?
                if DRAW_PREFIX in function.__name__ and not type_name.startswith("mvDraw"):
                    type_name = f'mvDraw{type_name.removeprefix("mv")}'
                # handler item?
                elif "item_" in function.__name__ or "_handler" in function.__name__:
                    type_name = type_name.replace("Item", "", 1)
                # multi input item?
                elif function.__name__[-1] == "x":
                    type_name = f"{type_name[:-1]}Multi"
                else:
                    raise
                type_uuid = name_to_uuid[type_name]

        parameters = ItemParameters()
        parameters.creation.update((name, _update_parameter(param)) for name, param in signature.parameters.items())
        parameters.readable.update((param.name, param) for param in _filter_config_parameters(parameters.creation.values()))
        parameters.writable.update(parameters.readable)

        if type_name.endswith("Handler"):
            param = parameters.creation.get("key")
            if param is not None:
                param = codegen.parameter(param.name, param.KEYWORD_ONLY, param.default, param.annotation)
                parameters.readable["key"] = parameters.writable["key"] = param
            else:
                param = parameters.creation.get("button")
                if param is not None:
                    param = codegen.parameter(param.name, param.KEYWORD_ONLY, param.default, param.annotation)
                    parameters.readable["button"] = parameters.writable["button"] = param

        param = parameters.creation.get("pos")
        if param is not None:
            try:
                del parameters.readable["pos"]  # writable as configuration, but is considered a state
            except KeyError:
                pass

            if param.kind == param.KEYWORD_ONLY:
                # this is an empty list (mutable) by default
                parameters.creation["pos"] = codegen.parameter(param.name, param.kind, (), param.annotation)

        if type_name in ("mvThemeColor", "mvThemeStyle"):
            # `configure()`    : -`target`, -`category`
            # `configuration()`: +`target`, +`category`
            parameters.writable.pop('category', None)

            param = parameters.creation["target"]
            parameters.readable['target'] = codegen.parameter(
                param.name, param.KEYWORD_ONLY, param.default, param.annotation
            )

        name_to_info[type_name] = ItemTypeInfo(
            type_name=type_name,
            type_uuid=type_uuid,
            function=function,
            function2=function2,
            container=container,
            parameters=parameters,
        ) 

    return types.MappingProxyType({n:name_to_info[n] for n in sorted(name_to_info)})




@dataclasses.dataclass(slots=True, frozen=True)
class ThemeElementInfo:
    type_name: typing.Literal['mvThemeColor', 'mvThemeStyle']
    elem_name: str
    func_name: str
    target: int
    category: int


@_static_output
def theme_element_info() -> typing.Mapping[str, ThemeElementInfo]:
    const_pfxs = (
        "mvThemeCol",
        "mvPlotCol",
        "mvNodeCol",
        "mvNodesCol",
        "mvStyleVar",
        "mvPlotStyleVar",
        "mvNodeStyleVar",
        "mvNodesStyleVar",
    )

    CORE = dearpygui.mvThemeCat_Core
    PLOT = dearpygui.mvThemeCat_Plots
    NODE = dearpygui.mvThemeCat_Nodes
    const_to_elem: dict[int, dict[str, ThemeElementInfo]] = {
        CORE: {},
        PLOT: {},
        NODE: {},
    }

    RE_CAPS = re.compile(r'([A-Z])')

    for constant, target in dearpygui.__dict__.items():
        pfx, *elem_name = constant.split("_", maxsplit=1)
        if pfx not in const_pfxs:
            continue
        elem_name = elem_name[0] \
            .replace("_", "") \
            .replace("Background", "Bg") \
            .replace("bg", "Bg")
        func_name = '_'.join(re.sub(RE_CAPS, r' \1', elem_name).split()).lower()

        kind = 'mvThemeColor' if pfx.endswith("Col") else 'mvThemeStyle'

        if pfx.startswith('mvPlot'):
            category = PLOT
            if not elem_name.startswith('Plot'):
                elem_name = f'Plot{elem_name}'
                func_name = f'plot_{func_name}'
        elif pfx.startswith('mvNode'):
            category = NODE
            if not elem_name.startswith('Node'):
                elem_name = f'Node{elem_name}'
                func_name = f'node_{func_name}'
        else:
            category = CORE

        element = ThemeElementInfo(
            type_name=kind,
            func_name=func_name,
            elem_name=elem_name,
            target=target,
            category=category,
        )
        const_to_elem[category][constant] = element

    for cat in (CORE, PLOT, NODE):
        const_to_elem[cat] = dict(
            sorted(const_to_elem[cat].items(), key=lambda x: x[1].elem_name)  # type: ignore
        )

    return types.MappingProxyType(
        const_to_elem[CORE] | const_to_elem[PLOT] | const_to_elem[NODE]
    )


@_static_output
def theme_color_info() -> typing.Mapping[str, ThemeElementInfo]:
    return types.MappingProxyType({
        k:v for k,v in theme_element_info().items()
        if v.type_name == "mvThemeColor"
    })


@_static_output
def theme_style_info() -> typing.Mapping[str, ThemeElementInfo]:
    return types.MappingProxyType({
        k:v for k,v in theme_element_info().items()
        if v.type_name == "mvThemeStyle"
    })




@dataclasses.dataclass(slots=True, frozen=True)
class ConstantInfo:
    name  : str
    target: int
    prefix: str
    suffix: str


@_static_output
def constant_info() -> typing.Mapping[str, ConstantInfo]:
    definitions = {}

    prefixes = {
        "mvKey": "Key",
        "mvXAxis": "Axis",
        "mvYAxis": "Axis",
        "mvPlot_Location": "PlotLocation",
        "mvNodeMiniMap_Location": "NodeMiniMapLocation",
        "mvTable_Sizing": "TablePolicy",
        "mvFormat_Float": "ColorFormat",
        "mvThemeCat": "ThemeCategory",
        "mvReserved": "ReservedUUID",
        "mvNode_PinShape": "NodePinShape",
        "mvNode_Attr": "NodeAttr",
        "mvPlotColormap": "PlotColorMap"
    }
    suffixes = {
        "uint8": "UINT_8",
        "RdBu": "RdBu",
        "BrBG": "BrBG",
        "PiYG": "PiYG",
    }
    prefix_noformat = {"GraphicsBackend",}
    suffix_noformat = {"NORTHWEST", "NORTHEAST", "SOUTHWEST", "SOUTHEAST"}
    suffix_tolower  = {"Us", "Ms", "S"}

    re_capwords = re.compile(
        r"[A-Z][a-z][a-z]+|^(?:L|R)(?=[A-Z][a-z])|[A-Z]*\d+|[A-Z][A-Z][A-Z]+"
    )

    const_exclusions = set(theme_element_info())
    for name, value in dearpygui.__dict__.items():
        if (
            name in const_exclusions or
            not (name.startswith('mv') and '_' in name)
        ):
            continue

        assert isinstance(value, int)

        startswith = name.startswith
        for raw_pfx, new_pfx in prefixes.items():
            if startswith(raw_pfx):
                prefix = new_pfx
                suffix = name.removeprefix(raw_pfx).lstrip('_')
                break
        else:
            prefix, suffix = name.removeprefix('mv').split('_', 1)

        if suffix in suffixes:
            suffix = suffixes[suffix]
        elif suffix.isdigit():
            suffix = f"DIGIT_{suffix}"
        elif suffix.startswith("NumPad"):
            suffix = suffix.replace("NumPad", "NUMPAD_").upper()
        elif suffix in suffix_tolower:
            suffix = suffix.lower()
        else:
            if not (prefix in prefix_noformat or suffix.upper() in suffix_noformat):
                matches = re_capwords.findall(suffix)
                if matches:
                    suffix = '_'.join(matches)

            suffix = suffix.upper()

        definitions[name] = ConstantInfo(
            name=name, target=value, prefix=prefix, suffix=suffix
        )

    return types.MappingProxyType(definitions)



# [ Signature Parsing, Formatting ]

_CONFIG_PARAM_EXCLUSIONS = (
    "tag", "id", "parent", "before", "default_value", "delay_search"
)

def _filter_config_parameters(parameters: typing.Iterable[Parameter], /):
    for param in parameters:
        name = param.name
        if (
            not ("default" in name or name in _CONFIG_PARAM_EXCLUSIONS) and
            param.kind == param.KEYWORD_ONLY
        ):
            yield param




_ANNOTATION_OVERRIDES = {
    "label": str | None,
    "tag": Item,
    "parent": Item,
    "before": Item,
    "callback": ItemCallback | None,
    "zoom_rate": float
}
_ANNOTATION_OVERRIDES2 = {
    typing.Callable: ItemCallback | None,
}


_RE_PYSEQ1 = re.compile(r"list\[(?P<inner>.+)\]\s*\|\s*tuple\[(?P=inner), ...\]")
_RE_PYSEQ2 = re.compile(r"tuple\[(?P<inner>.+), ...\]\s*\|\s*list\[(?P=inner)\]")

def _update_annotation(name, anno, /):
    anno_ = _ANNOTATION_OVERRIDES.get(name)
    if anno_ is not None:
        return anno_

    anno_ = _ANNOTATION_OVERRIDES2.get(anno)
    if anno_ is not None:
        return anno_

    type_repr_ = annotationlib.type_repr(anno)
    type_repr  = type_repr_ \
        .replace("typing.Tuple", "tuple") \
        .replace("typing.List", "list") \
        .replace("typing.Dict", "dict")

    if type_repr != type_repr_:
        while True:
            for pattern in (_RE_PYSEQ1, _RE_PYSEQ2):
                m = pattern.match(type_repr)
                if m is not None:
                    type_repr = f"Sequence[{m.group('inner')}]"
                    break
            else:
                break

        anno = eval(type_repr, globals=typing.__dict__)

    return anno


def _update_parameter(parameter: Parameter, /) -> Parameter:
    if parameter.kind == parameter.VAR_KEYWORD or parameter.kind == parameter.VAR_POSITIONAL:
        return parameter

    anno = parameter.annotation
    if anno is not parameter.empty:
        anno = _update_annotation(parameter.name, anno)
        if anno != parameter.annotation:
            parameter = codegen.parameter(parameter.name, parameter.kind, parameter.default, anno)

    if parameter.default is not parameter.empty and isinstance(parameter.default, list):
        parameter = codegen.parameter(
            parameter.name, parameter.kind, tuple(parameter.default), parameter.annotation
        )

    return parameter


def parse_annotations(obj, /) -> dict[str, typing.Any]:
    annotations = annotationlib.get_annotations(obj, format=annotationlib.Format.VALUE)
    return {name:_update_annotation(name, anno) for name, anno in annotations.items()}




_DOCS_OVERRIDES = {
    "*": {
        'before': (
            "Existing child item of the current/target parent in the same child slot this item is stored in. "
            "This item will be positioned immediately before the child. A value of `None` or 0 appends the item at the "
            "end of the child slot."
        ),
        'callback': (
            "Callable to invoke following a specific event tied to this item. This can be any callable object with a "
            "`__code__` attribute. The callable **may** accept up to three positional arguments: the integer ID of the "
            "\"sending\" item (usually this item), data or value associated with the event, and the `user_data` of the "
            "sending item."
        ),
        'enabled': (
            "Sets the item's operational state. `True` and `False` enables or disables the item, respectively. Note that "
            "theme components affecting the item may change based off this status. This setting does not affect the item's "
            "visibility state."
        ),
        'filter_key': (
            'The text value of the item that will be used when applying filters.'
        ),
        'height': (
            "Vertical size of the item in pixels. Setting this value may override auto-scaling options for some items, but "
            "can be reversed by setting this value back to 0. For some items, a value of -1 can be used to make it fill as "
            "much of the visible space as possible."
        ),
        "width": (
            "Horizontal size of the item in pixels. Setting this value may override auto-scaling options for some items, but "
            "can be reversed by setting this value back to 0. For some items, a value of -1 can be used to make it fill as "
            "much of the visible space as possible."
        ),
        'indent': (
            "Additional horizontal padding added to the left of the widget. Multiplicative with the `mvStyleVar_IndentSpacing` "
            "theme style element. "
        ),
        'label': (
            "An informal name for the item. Items that are rendered may display this value. "
            "Note that any text following the substring `\"##\"` will not be rendered. "
        ),
        'parent': (
            "The item that will parent this one. If unspecified, the item atop the container stack will be used as its parent. "
        ),
        'show': (
            "For items that can be rendered, `True` and `False` will show and hide it, respectively. For other items "
            "such as handlers and registries, this setting functions similarly to `enabled`. "
        ),
        'source': (
            "The item whose value will be used as the source for this item's value. Updates automatically when the source's "
            "value changes."
        ),
        'tag': (
            "Used as the item's unique integer ID or alias. When unspecified, a unique integer ID is automatically generated "
            "for the item. "
        ),
        'track_offset': (
            "A numeric value between 0 and 1 that affects item tracking while scrolling when *tracked* is `True`. Common values "
            "are 0.0 (top), 0.5 (center, default), and 1.0 (bottom)."
        ),
        'tracked': (
            "Enables or disables (`True` and `False`, respectively) the item's ability to be tracked while scrolling."
        ),
        'use_internal_label': (
            "If `True`, `'##<item_uuid>'` is appended to the item's *label*."
        ),
        'user_data': (
            "Can be any value. "
        ),
    },
}


def parse_docstring(obj, /) -> dict[str, str]:
    text = obj.__doc__
    if text is None:
        return {}

    text = text.partition("Args:\n")[2].partition("Returns:")[0].partition("Yields:")[0]

    texts = {}
    for ln in text.split("\n"):
        name, _, doc = ln.partition(":")

        doc = doc.strip()
        if not doc:
            continue

        name = name.partition('(')[0].strip()
        if not name:
            continue

        texts[name] = doc

    return texts
