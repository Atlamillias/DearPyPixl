"""Utilities for inspecting Dear PyGui's API."""
import re
import types
import array
import typing
import inspect
import textwrap
import threading
import dataclasses
from inspect import Parameter
from dearpygui import dearpygui
from . import constants, _typing, _tools
from ._typing import (
    Any,
    Item,
    Callable,
    ItemCommand,
    Sequence,
    Mapping,
    Literal,
)




# [ API Parsers ]

def is_contextmanager(o: Any, /) -> bool:
    """Return True if a function is wrapped by `contextlib.contextmanager`.

    Args:
        * o: The object to inspect.


    >>> from dearpygui import dearpygui
    ...
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
    # Works 99% of the time. In theory, it could return false-positives.
    is_ctx_manager = all((
        callable(o),
        o.__globals__["__name__"] == "contextlib",
        o.__module__ != "contextlib",
        isinstance(getattr(o, "__wrapped__", None), types.FunctionType),
    ))
    return is_ctx_manager or False


def is_item_command(o: Any, /) -> bool:
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
    # This only works reliably when the function is in `dearpygui`
    # public module because those in the private `_dearpygui` module
    # can't be accurately inspected (no signature).
    try:
        signature = inspect.signature(o)
    except:
        return False  # not callable or is "built-in"

    try:
        if dearpygui.__name__ not in o.__module__:
            return False
    except AttributeError:
        return False

    if signature.return_annotation != int | str:
        return False

    if all(kwd not in signature.parameters for kwd in ("tag", "id")):
        return False
    # weeds out false positives
    elif signature.parameters['tag'].kind != Parameter.KEYWORD_ONLY:
        return False

    # minor optimization for future calls to `signature` (there will be)
    if not hasattr(o, "__signature__"):
        o.__signature__ = signature
    return True








@dataclasses.dataclass(slots=True, frozen=True)
class ItemDefinition:
    name          : str
    enum          : int
    command1      : ItemCommand
    command2      : ItemCommand | None
    init_params   : Mapping[str, Parameter] = dataclasses.field(repr=False)
    rconfig_params: Mapping[str, Parameter] = dataclasses.field(repr=False)
    wconfig_params: Mapping[str, Parameter] = dataclasses.field(repr=False)

    is_container: bool = dataclasses.field(init=False, repr=False)

    def __post_init__(self):
        _setattr = object.__setattr__.__get__(self)
        _setattr('is_container', bool(self.command2))


@_tools.cache_once
def item_definitions() -> Mapping[str, ItemDefinition]:
    """Parse Dear PyGui's API and return compiled item type definitions.

    The result of this function is only built once and is cached
    for future calls.
    """
    def set_item_types():
        nonlocal name_to_enum
        dearpygui.create_context()
        name_to_enum = dearpygui.get_item_types()
        dearpygui.destroy_context()

    name_to_enum = None
    # This needs to be done in a separate thread so the GPU
    # context isn't created too early or burned for the user.
    _t = threading.Thread(target=set_item_types, daemon=True)
    _t.start()
    _t.join()

    name_to_enum      = _typing.cast(dict[str, int], name_to_enum)
    name_to_def       = {}
    commands_to_names = {
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
    command_cache = set()
    cpfx_add  = 'add_'
    cpfx_draw = 'draw_'
    for name, obj in dearpygui.__dict__.items():
        if (
            not callable(obj)
            or not is_item_command(obj)
            or "popup" in name
            or obj in command_cache
        ):
            continue

        # find item commands and raw type name
        if is_contextmanager(obj):
            tp_cmd1  = (
                getattr(dearpygui, f"{cpfx_add}{name}", None) or
                getattr(dearpygui, f"{cpfx_draw}{name}")
            )
            tp_cmd2  = obj
            _tp_name = name
        else:
            tp_cmd1  = obj
            _tp_name = name
            # chaining `.removeprefix(...)` could remove more than intended
            if _tp_name.startswith(cpfx_draw):
                _tp_name = _tp_name.removeprefix(cpfx_draw)
            elif _tp_name.startswith(cpfx_add):
                _tp_name = _tp_name.removeprefix(cpfx_add)
            tp_cmd2 = getattr(dearpygui, _tp_name, None)

        command_cache.add(tp_cmd1)
        if tp_cmd2 is not None:
            command_cache.add(tp_cmd2)

        # build final itemtype name
        if tp_cmd1 in commands_to_names:
            tp_name = commands_to_names[tp_cmd1]
            tp_enum = name_to_enum[tp_name]
        else:
            if _tp_name.startswith("colormap"):
                _tp_name = _tp_name.replace("colormap", "color_map", 1)  # capwords
            tp_name = f'mv{_tp_name.title().replace("_", "")}'
            try:
                tp_enum = name_to_enum[tp_name]
            except KeyError:  # `tp_name` is wrong. Try to "fix" it case-by-case.
                # drawing item? (the `.removeprefix` calls from earlier causes this)
                if cpfx_draw in tp_cmd1.__name__ and not tp_name.startswith("mvDraw"):
                    tp_name = f'mvDraw{tp_name.removeprefix("mv")}'
                    tp_enum = name_to_enum[tp_name]
                # item handler? (global handlers shouldn't fail above)
                elif all(s in tp_cmd1.__name__ for s in ("item_", "_handler")):
                    tp_name = tp_name.replace("Item", "", 1)
                    tp_enum = name_to_enum[tp_name]
                # x4 input item?
                elif tp_cmd1.__name__[-1] == "x":
                    tp_name = f"{tp_name[:-1]}Multi"
                    tp_enum = name_to_enum[tp_name]
                else:
                    raise

        # build method parameters
        init_params = upd_param_annotations(
            inspect.signature(tp_cmd1).parameters
        )

        # Ideally, `.configure` should accept what `.configuration` returns
        # as keyword args. But not everything is writable. At the very least,
        # `type(itf)(**.itf.configuration())` MUST be possible so that the
        # interface can be accurately copied/reconstructed.
        # `get_config_parameters` handles a lot of this, but some detail work
        # may need to be done per type.
        rconfig_params = get_config_parameters(init_params)
        if tp_name in ("mvThemeColor", "mvThemeStyle"):
            # `.configure`    : -`target`, -`category`
            # `.configuration`: +`target`, +`category`
            wconfig_params = rconfig_params.copy()
            wconfig_params.pop('category', None)
            rconfig_params['target'] = init_params['target'].replace(
                kind=Parameter.KEYWORD_ONLY
            )
        else:
            wconfig_params = rconfig_params.copy()
        # `pos` is writable as configuration, but is considered a state...
        rconfig_params.pop('pos', '')

        name_to_def[tp_name] = ItemDefinition(
            name=tp_name,
            enum=tp_enum,
            command1=tp_cmd1,
            command2=tp_cmd2,
            init_params=types.MappingProxyType(init_params),
            rconfig_params=types.MappingProxyType(rconfig_params),
            wconfig_params=types.MappingProxyType(wconfig_params),
        )

    return types.MappingProxyType({n:name_to_def[n] for n in sorted(name_to_def)})  # type: ignore




@dataclasses.dataclass(slots=True, frozen=True)
class ElementDefinition:
    name1   : str
    name2   : str
    type    : Literal['mvThemeColor', 'mvThemeStyle']
    constant: str
    target  : int
    category: constants.ThemeCategory



@_tools.cache_once
def element_definitions() -> Mapping[str, ElementDefinition]:
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

    CORE = constants.ThemeCategory(dearpygui.mvThemeCat_Core)
    PLOT = constants.ThemeCategory(dearpygui.mvThemeCat_Plots)
    NODE = constants.ThemeCategory(dearpygui.mvThemeCat_Nodes)
    const_to_elem: dict[constants.ThemeCategory, dict[str, ElementDefinition]] = {
        CORE: {},
        PLOT: {},
        NODE: {},
    }

    RE_CAPS = re.compile(r'([A-Z])')

    for constant, target in dearpygui.__dict__.items():
        pfx, *name1 = constant.split("_", maxsplit=1)
        if pfx not in const_pfxs:
            continue
        name1 = name1[0] \
            .replace("_", "") \
            .replace("Background", "Bg") \
            .replace("bg", "Bg")
        name2 = '_'.join(re.sub(RE_CAPS, r' \1', name1).split()).lower()

        kind = 'mvThemeColor' if pfx.endswith("Col") else 'mvThemeStyle'

        if pfx.startswith('mvPlot'):
            category = PLOT
            if not name1.startswith('Plot'):
                name1 = f'Plot{name1}'
                name2 = f'plot_{name2}'
        elif pfx.startswith('mvNode'):
            category = NODE
            if not name1.startswith('Node'):
                name1 = f'Node{name1}'
                name2 = f'node_{name2}'
        else:
            category = CORE

        element = ElementDefinition(
            name1=name1,
            name2=name2,
            type=kind,
            constant=constant,
            target=target,
            category=category,
        )
        const_to_elem[category][constant] = element

    # Using the names formated above can cause plot and node
    # elements to shadow core elements. Core elements should
    # keep the more simple and intuitive name(s).
    #for cat in (PLOT, NODE):
    #    name_map = name_to_elem[cat]
    #    for name1, element in name_map.items():
    #        if name1 in name_to_elem[CORE]:
    #            name1 = f'{cat.name.title()}{name1}'
    #            assert name1 not in name_to_elem[CORE]
    #            assert name1 not in name_map
    #            object.__setattr__(element, 'name1', name1)
    #            object.__setattr__(element, 'name2', f'{cat.name.lower()}_{element.name2}')

    for cat in constants.ThemeCategory:
        const_to_elem[cat] = dict(
            sorted(const_to_elem[cat].items(), key=lambda x: x[1].name1)  # type: ignore
        )

    return types.MappingProxyType(
        const_to_elem[CORE] | const_to_elem[PLOT] | const_to_elem[NODE]
    )

@_tools.cache_once
def color_definitions() -> Mapping[str, ElementDefinition]:
    return types.MappingProxyType({
        k:v for k,v in element_definitions().items()
        if v.type == "mvThemeColor"
    })

@_tools.cache_once
def style_definitions() ->  Mapping[str, ElementDefinition]:
    return types.MappingProxyType({
        k:v for k,v in element_definitions().items()
        if v.type == "mvThemeStyle"
    })








# [ Signature Parsing, Formatting ]

def get_config_parameters(parameters: Mapping[str, Parameter]):
    """Return a mapping of item command parameters containing only
    configuration-related parameters."""
    excluded_names = (
        "tag", "id",      # read-only
        "parent",         # read-only (ish)
        "default_value",  # exposed via `item.g/set_value`
        "delay_search",   # can be set if supported, but never incl in `get_item_configuration`
    )
    excluded_parts = ("default",)
    return {
        p.name:p for p in parameters.values()
        if p.kind == Parameter.KEYWORD_ONLY
        and p.name not in excluded_names
        and all(npart not in p.name for npart in excluded_parts)
    }


def upd_param_annotations(parameters: Mapping[str, Parameter]) -> dict[str, Parameter]:
    """Return item command parameters with updated annotations."""
    upd_params = {}
    for p in parameters.values():
        if p.kind == Parameter.VAR_KEYWORD:
            continue
        # This specifically targets old Python 3.6 annotations and replaces
        # them with concrete type annotations. Several others are changed
        # for better accuracy.
        name = p.name
        anno = p.annotation

        # case-specific formatting
        if anno == Item:
            anno = 'Item'  # type alias
        elif name == 'label':
            anno = str | None
        elif name == 'pos':
            anno = tuple[int, int] | list[int]
        elif 'callback' in name or name == 'on_close':
            anno = Callable | None
        elif (
            'color' in name
            or (p.default and isinstance(p.default, tuple))
            and len(p.default) == 4
            and anno == typing.List[int] | typing.Tuple[int, ...]
        ):
            anno = tuple[int, int, int, int | None] | list[int]
        elif anno == typing.List[typing.List[float]]:
            anno = Sequence[Sequence[float]]
        # general-case formatting
        else:
            for tp in str, float, int:
                if anno != ((typing.List[tp] | typing.Tuple[tp, ...])):
                    continue
                anno = Sequence[tp]
                break
        upd_params[name] = Parameter(
            name,
            p.kind,
            annotation=anno,
            default=p.default,
        )
    return upd_params



_item_ref  = "A reference to an existing item (as a `int` uuid, `str` alias, or `int` item interface)"
_empty_ref = "None or 0 (default)"

@_tools.frozen_namespace
class _DocParseConst:
    RE_ARGS = re.compile(
        r'^\s*Args[;:]$', re.MULTILINE
    )
    RE_PARAM = re.compile(
        r'^\s+(?P<name>\w*)\s?\((?P<type>[^)]+)\):\s*(?P<doc>.*)',
        re.MULTILINE,
    )
    # XXX: This doesn't do the job. Kept as a reference for later (TODO).
    RE_UNION = re.compile(
        r'Union\[\s*(?:[^\s]+]?)(?:(?P<sep>,)\s*[^\s]+)+(?P<end>\])'
    )

    # "large-scope" replacements
    # TODO: regex
    TYPE_REPLACEMENTS_1 = (
        ("Union[int, str]"                      , "int | str"                 ),
        ("Union[List[int], Tuple[int, ...]]"    , f"Sequence[int]"            ),
        ("Union[List[float], Tuple[float, ...]]", f"Sequence[float]"          ),
        ("Union[List[str], Tuple[str, ...]]"    , f"Sequence[str]"            ),
        ("List[List[float]]"                    , f"Sequence[Sequence[float]]"),
        ("List[List[int]]"                      , f"Sequence[Sequence[int]]"  ),
    )
    # "small-scope" replacements
    TYPE_REPLACEMENTS_2 = (
        ("Dict" , "dict" ),
        ("List" , "list" ),
        ("Set"  , "set"  ),
        ("Tuple", "tuple")
    )

    HEAD_SPECIFIC_REPLACEMENTS: dict[str, str] = {}

    PARAM_GENERAL_REPLACEMENTS: dict[str, str] = {
        'before': (
            f"{_item_ref} that is parented by the container that will soon parent this one. If specified, this item will "
            f"be inserted into the parent's child slot preceding the referenced item. If this value is None or 0 (default), "
            f"the item will be added to the end of the slot."
        ),
        'callback': (
            'Called by Dear PyGui when the item is interacted with (usually clicked). Can be None, or any callable with '
            'a `__code__` attribute. Dear PyGui will send up to three positional arguments to the callback; '
            '`sender` (`tag` of the item *callback* is registered to), `app_data` (None, or an updated value associated '
            'with `sender`), and `user_data` (registered *user_data* value of `sender`). However, the callback is not '
            'required to accept all or any of these arguments.'
        ),
        'enabled': (
            "Sets the item's operational state. Setting to False disables the item's functionality. An item's operational "
            "state also affects which elements/components of a theme are applied to it (based off the *enabled_state* value "
            "of each theme component). This setting does not affect the item's visibility state."
        ),
        'filter_key': (
            'The text value of the item that will be used when applying filters.'
        ),
        'height': (
            'Vertical size of the item in pixels. Setting this value may override auto-scaling options for some items; this can be '
            'reversed by setting this back to 0. Note that the value is interpreted as unsigned.'
        ),
        'indent': (
            'Horizontal padding added to the left of the widget. Multiplicative with the `mvStyleVar_IndentSpacing` '
            'theme style element.'
        ),
        'label': (
            'An informal name for the item. Items that are visible in the user interface may also use this as their display '
            'name. The `"##"` delimiter can be used within the label text. If present, only text preceding the first '
            'use of this delimiter will be shown when displaying the label. You can prevent this behavior by escaping the '
            'second hash character with a carriage return (`#\\\\r#`).'
        ),
        'parent': (
            f"{_item_ref} that will become this item's parent. If {_empty_ref}, Dear PyGui will default to "
            f"using whatever item that is on top of the container stack."
        ),
        'show': (
            'Setting to True (default) will render the item and allow it to be seen, while False does the opposite. '
            'For items that cannot be visible in the user interface (handlers, registries, etc), the behavior of '
            '*show* is similar to that of *enabled* where False disables their functionality.'
        ),
        'source': (
            f"{_item_ref}. If specified, getting or setting this item's value will instead get or set the value of the "
            f"referenced item. If the item normally displays its' value, it will instead display the referenced item's "
            f"value."
        ),
        'tag': (
            'An item reference (as a `int` uuid, `str` alias, or `int` item interface) to bind to the interface. If '
            f'{_empty_ref}, or if the integer/string value of the reference is new or unused by another item, '
            "the interface creates a new item of its' type during initialization. If the value is not a new binding "
            "reference, the interface will (try to) operate on the item with an identifier matching that value."
        ),
        'track_offset': (
            'A numeric value between 0 and 1 that affects item tracking while scrolling when *tracked* is True. Common values are'
            ' 0.0 (top), 0.5 (center, default), and 1.0 (bottom).'
        ),
        'tracked': (
            "Enables (True, default) or disables (False) the item's ability to be tracked while scrolling."
        ),
        'use_internal_label': (
            "True (default) will append `'##<item_uuid>'` to the item's *label* value."
        ),
        'user_data': (
            'Can be set as any value or reference. For items with callback-related configuration options, Dear PyGui will send this '
            'as the third positional argument when invoking the callback(s).'
        ),
        'width': (
            f'Horizontal size of the item in pixels. Setting this value may override auto-scaling options for some items; this can be '
            'reversed by setting this back to 0. Note that the value is interpreted as unsigned.'
        ),
    }

    PARAM_SPECIFIC_REPLACEMENTS: dict[str, str] = {}


def upd_command_doc(command: ItemCommand, line_width: int = 92) -> str:
    """Return a formatted docstring parsed from a Dear PyGui item
    command."""
    s = command.__doc__ or ''
    s = s \
        .replace('\t', '    ') \
        .split('    Returns:')[0] \
        .split("    Yields:")[0] \

    key = _DocParseConst.RE_ARGS.search(s)
    if not key:
        return s

    header, body = s.split(key.group(0), maxsplit=1)
    header = textwrap.fill(
        f"{header.strip().rstrip('.')}.",
        line_width,
        subsequent_indent="    "
    )

    # TODO: Build an accurate regex for unions. Harder than it seems -- like
    # reading alphabet soup while drunk.
    for replacement in _DocParseConst.TYPE_REPLACEMENTS_1:
        body = body.replace(*replacement)

    params = array.array('u')
    for param in _DocParseConst.RE_PARAM.finditer(body):
        name, tp, doc = param.groups()
        if '(deprecated)' in doc:
            continue
        if name in _DocParseConst.PARAM_GENERAL_REPLACEMENTS:
            doc = _DocParseConst.PARAM_GENERAL_REPLACEMENTS[name]
        else:
            doc = doc.rstrip().rstrip('.')
            if doc:
                doc = f"{doc}."
        for replacement in _DocParseConst.TYPE_REPLACEMENTS_2:
            tp = tp.replace(*replacement)
        params.fromunicode(textwrap.fill(
            f"* {name} ({tp}): {doc}",
            line_width,
            initial_indent="        ",
            subsequent_indent="        ",
        ))
        params.fromunicode('\n\n')

    return ''.join((
        header,
        "\n\n    Args:\n",
        params.tounicode(),
        f"    Command: `dearpygui.{command.__name__}`"
    ))
