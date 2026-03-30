import typing
import io
import os
import re
import enum
import pathlib
import inspect
import zipfile
import string
import collections
import annotationlib
import dataclasses

if typing.TYPE_CHECKING:
    from inspect import _ParameterKind




# [ structures ]

if typing.TYPE_CHECKING:
    from inspect import _ParameterKind as ParameterKind
else:
    ParameterKind = type(inspect.Parameter.POSITIONAL_OR_KEYWORD)

class ParameterFlag(enum.IntFlag):
    NONE         = 0
    NO_WRITE     = 1 << 0
    NO_READ      = 1 << 1

class Parameter(inspect.Parameter):
    __slots__ = ("flags",)

    empty = inspect.Parameter.empty

    @classmethod
    def positional(cls, /, name: str, annotation: typing.Any = empty, default: typing.Any = empty, *, flags: ParameterFlag = ParameterFlag.NONE) -> Parameter:
        return cls(name, cls.POSITIONAL_ONLY, annotation, default, flags=flags)

    @classmethod
    def var_positional(cls, /, name: str, annotation: typing.Any = empty, default: typing.Any = empty, *, flags: ParameterFlag = ParameterFlag.NONE) -> Parameter:
        return cls(name, cls.VAR_POSITIONAL, annotation, default, flags=flags)

    @classmethod
    def keyword(cls, /, name: str, annotation: typing.Any = empty, default: typing.Any = empty, *, flags: ParameterFlag = ParameterFlag.NONE) -> Parameter:
        return cls(name, cls.KEYWORD_ONLY, annotation, default, flags=flags)

    @classmethod
    def var_keyword(cls, /, name: str, annotation: typing.Any = empty, default: typing.Any = empty, *, flags: ParameterFlag = ParameterFlag.NONE) -> Parameter:
        return cls(name, cls.VAR_KEYWORD, annotation, default, flags=flags)

    def __init__(self, /, name: str, kind: _ParameterKind = inspect.Parameter.POSITIONAL_OR_KEYWORD, annotation: typing.Any = empty, default: typing.Any = empty, *, flags: ParameterFlag = ParameterFlag.NONE) -> None:
        super().__init__(name, kind, default=default, annotation=annotation)  # type: ignore
        self.flags = flags

    def _format(self, *, quote_annotation_strings=False):
        empty = __class__.empty
        kind = self.kind

        formatted = self.name

        anno = self.annotation
        if self.annotation is not empty:
            formatted = f"{formatted}: {inspect.formatannotation(anno, quote_annotation_strings=False)}"

        default = self.default
        if default is not empty:
            if anno is not empty:
                formatted = f"{formatted} = {default}"
            else:
                formatted = f"{formatted}={default}"

        if kind == self.VAR_POSITIONAL:
            formatted = "*" + formatted
        elif kind == self.VAR_KEYWORD:
            formatted = "**" + formatted

        return formatted

    def replace(self, **kwargs) -> typing.Self:
        return __class__(
            name=kwargs.get("name", self.name),
            kind=kwargs.get("kind", self.kind),
            default=kwargs.get("default", self.default),
            annotation=kwargs.get("annotation", self.annotation),
            flags=kwargs.get("flags", self.flags),
        )

    def __format__(self, format_spec: str) -> str:
        return super().__format__(format_spec)


class FeatureFlag(enum.IntFlag):
    NONE                    = 0
    ROOT                    = 1 << 0
    PARENT                  = 1 << 1
    CHILD                   = 1 << 2
    ADDRESSABLE             = 1 << 3
    SUPPORTS_POSITIONING    = 1 << 4
    SUPPORTS_TOGGLE         = 1 << 5
    SUPPORTS_HOVER          = 1 << 6
    SUPPORTS_ACTIVE         = 1 << 7
    SUPPORTS_ACTIVATION     = 1 << 8
    SUPPORTS_DEACTIVATIONAE = 1 << 9
    SUPPORTS_FOCUS          = 1 << 10
    SUPPORTS_CLICK          = 1 << 11
    SUPPORTS_VISIBILITY     = 1 << 12
    SUPPORTS_EDITING        = 1 << 13
    SUPPORTS_CONTREGION     = 1 << 14
    SUPPORTS_RECTSIZE       = 1 << 15
    SUPPORTS_GEOMETRY       = 1 << 16
    SUPPORTS_SCROLLING      = 1 << 17

@dataclasses.dataclass(slots=True)
class ItemTypeInfo:
    name       : str
    command    : str
    value_type : typing.Any = None
    target_slot: typing.Literal[0, 1, 2, 3] = 1
    parents    : list[str] = dataclasses.field(default_factory=list)
    children   : list[str] = dataclasses.field(default_factory=list)
    parameters : list[Parameter] = dataclasses.field(default_factory=list)
    flags      : FeatureFlag = FeatureFlag.NONE

    def __init__(
        self,
        /,
        name       : str,
        command    : str,
        value_type : typing.Any = None,
        target_slot: typing.Literal[0, 1, 2, 3] = 1,
        parents    : typing.Sequence[str] = (),
        children   : typing.Sequence[str] = (),
        parameters : typing.Sequence[Parameter] = (),
        flags      : FeatureFlag = FeatureFlag.NONE,
    ) -> None:
        self.name        = name
        self.command     = command
        self.value_type  = value_type
        self.target_slot = target_slot
        self.parents     = [*parents]
        self.children    = [*children]
        self.parameters  = [*parameters]
        self.flags       = flags


@dataclasses.dataclass(slots=True)
class DearPyGuiMetadata:
    version  : str
    constants: list[str]          = dataclasses.field(default_factory=list)
    functions: list[str]          = dataclasses.field(default_factory=list)
    typedef  : list[ItemTypeInfo] = dataclasses.field(default_factory=list)

    def __init__(
        self,
        /,
        version  : str,
        *,
        constants: typing.Sequence[str]          = (),
        functions: typing.Sequence[str]          = (),
        typedef  : typing.Sequence[ItemTypeInfo] = (),
    ) -> None:
        self.version   = version
        self.constants = [*constants]
        self.functions = [*functions]
        self.typedef   = [*typedef]

    @property
    def semver(self, /) -> tuple[int, ...]:
        version = self.version.lower().strip("abcdefghijklmnopqrstuvwxyz.-_ ")
        return tuple(int(d) for d in version.split('.') if d)




# [ codecs ]

type Nullable[T] = T | None


def _deserialize_datadict[T](d, type: type[T], deserializers: typing.Mapping, /) -> T:
    if not isinstance(d, dict):
        raise TypeError(f"expected a dictionary — got {d!r}")

    kwargs = {}
    for k, v in d.items():
        if v is None:
            continue

        codec = deserializers.get(k)
        if callable(codec):
            v = codec(v)

        kwargs[k] = v

    return type(**kwargs)

def _deserialize_to_sequence(seq_type: type[typing.Sequence], val_type: type, values: typing.Sequence) -> typing.Any:
    return seq_type(val_type(v) for v in values)  # type: ignore

def _deserialize_to_strtuple(values: typing.Sequence) -> tuple[str, ...]:
    return _deserialize_to_sequence(tuple, str, values)

def _deserialize_intflags(type: type, value) -> typing.Any:
    if isinstance(value, str):
        value = (value,)

    mask = type(0)
    for name in value:
        mask |= type[str(name).upper()]  # type: ignore
    return mask

def _serialize_intflags[T: enum.IntEnum](type: type[T], value: T) -> list[str]:
    flags = []

    for flag in type:
        if value & flag:
            flags.append(flag._name_)

    return flags


class _RawParameter(typing.TypedDict, total=False):
    name: str
    kind: typing.NotRequired[Nullable[str]]
    annotation: typing.NotRequired[Nullable[str]]
    anno: typing.NotRequired[Nullable[str]]  # alias
    default: typing.NotRequired[Nullable[typing.Any]]
    flags: typing.NotRequired[Nullable[typing.Sequence[str]]]

_PARAMETER_DESERIALIZERS = {
    "name": str,
    "kind": lambda obj: _deserialize_intflags(ParameterKind, obj),
    "anno": str,
    "annotation": str,
    "flags": lambda obj: _deserialize_intflags(ParameterFlag, obj),
}

def deserialize_parameter(d: _RawParameter, /) -> Parameter:
    anno = d.pop("anno", None)
    if anno is not None and "annotation" not in d:
        d["annotation"] = anno

    return _deserialize_datadict(d, Parameter, _PARAMETER_DESERIALIZERS)

def serialize_parameter(obj: Parameter, /) -> _RawParameter:
    d = _RawParameter(name=obj.name, kind=obj.kind._name_)

    anno = obj.annotation
    if anno is not obj.empty:
        if not isinstance(anno, str):
            anno = annotationlib.type_repr(anno)
        d["annotation"] = anno

    default = obj.default
    if default is not obj.empty:
        d["default"] = default

    d["flags"] = _serialize_intflags(ParameterFlag, obj.flags)  # type: ignore

    return d


class _RawItemTypeInfo(typing.TypedDict, total=False):
    name       : str
    command    : str
    value_type : typing.NotRequired[Nullable[str]]
    target_slot: typing.NotRequired[Nullable[typing.Literal[0, 1, 2, 3]]]
    parents    : typing.NotRequired[Nullable[typing.Sequence[str]]]
    children   : typing.NotRequired[Nullable[typing.Sequence[str]]]
    parameters : typing.NotRequired[Nullable[typing.Sequence[_RawParameter]]]
    flags      : typing.NotRequired[Nullable[typing.Sequence[str]]]

_ITEMTYPEINFO_DESERIALIZERS = {
    "name"       : str,
    "command"    : str,
    "value_type"      : str,
    "target_slot": int,
    "parents"    : _deserialize_to_strtuple,
    "children"   : _deserialize_to_strtuple,
    "parameters" : lambda obj: tuple(deserialize_parameter(d) for d in obj),
    "flags"      : lambda obj: _deserialize_intflags(FeatureFlag, obj),
}

def deserialize_itemtypeinfo(d: _RawItemTypeInfo, /) -> ItemTypeInfo:
    return _deserialize_datadict(d, ItemTypeInfo, _ITEMTYPEINFO_DESERIALIZERS)

def serialize_itemtypeinfo(obj: ItemTypeInfo, /) -> _RawItemTypeInfo:
    d = _RawItemTypeInfo(name=obj.name, command=obj.command)

    value = obj.value_type
    if value is not None:
        if not isinstance(value, str):
            value = annotationlib.type_repr(value)
        d["value_type"] = value

    d["target_slot"]       = obj.target_slot
    d["parents"]    = list(obj.parents)
    d["children"]   = list(obj.children)
    d["parameters"] = [serialize_parameter(p) for p in obj.parameters]
    d["flags"]      = _serialize_intflags(FeatureFlag, obj.flags)  # type: ignore

    return d


class _RawDearPyGuiMetadata(typing.TypedDict, total=False):
    version  : str
    constants: typing.NotRequired[Nullable[typing.Sequence[str]]]
    functions: typing.NotRequired[Nullable[typing.Sequence[str]]]
    typedef  : typing.NotRequired[Nullable[typing.Sequence[_RawItemTypeInfo]]]

_DEARPYGUIMETADATA_DESERIALIZERS = {
    "version"  : str,
    "constants": lambda obj: tuple(str(s) for s in obj),
    "functions": lambda obj: tuple(str(s) for s in obj),
    "typedef"  : lambda obj: tuple(deserialize_itemtypeinfo(d) for d in obj),
}

def deserialize(d: _RawDearPyGuiMetadata, /) -> DearPyGuiMetadata:
    return _deserialize_datadict(d, DearPyGuiMetadata, _DEARPYGUIMETADATA_DESERIALIZERS)

deserialize_metadata = deserialize

def serialize(obj: DearPyGuiMetadata, /) -> _RawDearPyGuiMetadata:
    d = _RawDearPyGuiMetadata(
        version=obj.version,
        constants=[*obj.constants],
        functions=[*obj.functions],
        typedef=[serialize_itemtypeinfo(info_dict) for info_dict in obj.typedef],
    )

    return d

serialize_metadata = serialize




# [ metadata parsing ]

_TYPE_CONV_MAP = {
    "None"         : "None",
    "Int"          : "int",
    "Int4"         : "Array[int, Literal[4]]",
    "Float"        : "float",
    "Float4"       : "Array[float, Literal[4]]",
    "FloatVect"    : "Array[int, Any]",
    "Double"       : "float",
    "Double4"      : "Array[float, Literal[4]]",
    "DoubleVect"   : "Array[float, Any]",
    "Series"       : "Array[Array[float, Any], Literal[5]]",
    "String"       : "str",
    "UUID"         : "Item",  # "int | str"
    "Color"        : "Array[int, Literal[3, 4]]",
    "Object"       : "Any",
    "Bool"         : "bool",
    "Long"         : "int",
    "Integer"      : "int",
    "Dict"         : "dict",
    "Callable"     : "ItemCallback | None",  # "Callable | None"
    "IntList"      : "Array[int, Any]",
    "StringList"   : "Array[str, Any]",
    "FloatList"    : "Array[float, Any]",
    "DoubleList"   : "Array[float, Any]",
    "ListListInt"  : "Array[Array[int, Any], Any]",
    "ListFloatList": "Array[Array[float, Any], Any]",
    "Time"         : "dict[Literal['sec', 'min', 'hour', 'month_day', 'month', 'year', 'week_day', 'year_day', 'daylight_savings'], int]",
}
_STATE_CONV_MAP = {
    "Hovered"      : FeatureFlag.SUPPORTS_HOVER,
    "Active"       : FeatureFlag.SUPPORTS_ACTIVE,
    "Focused"      : FeatureFlag.SUPPORTS_FOCUS,
    "Clicked"      : FeatureFlag.SUPPORTS_CLICK,
    "Visible"      : FeatureFlag.SUPPORTS_VISIBILITY,
    "Edited"       : FeatureFlag.SUPPORTS_EDITING,
    "Activated"    : FeatureFlag.SUPPORTS_ACTIVATION,
    "Deactivated"  : FeatureFlag.SUPPORTS_ACTIVATION,
    "DeactivatedAE": FeatureFlag.SUPPORTS_DEACTIVATIONAE,
    "ToggledOpen"  : FeatureFlag.SUPPORTS_TOGGLE,
    "RectMin"      : FeatureFlag.SUPPORTS_GEOMETRY,
    #"RectMax"      : FeatureFlag.SUPPORTS_GEOMETRY,
    "RectSize"     : FeatureFlag.SUPPORTS_RECTSIZE,
    "ContAvail"    : FeatureFlag.SUPPORTS_CONTREGION,
    "Scrolled"     : FeatureFlag.SUPPORTS_SCROLLING,
}
_PARAMETER_DEPRECATIONS = {
    (2, 2): ("delay_search",),
}
_PARAMETER_CONV_MAP = {
    "source"            : Parameter.keyword("source", "int | str", "0"),
    "id"                : Parameter.keyword("tag", "int | str", "0", flags=ParameterFlag.NO_READ | ParameterFlag.NO_WRITE),
    "tag"               : Parameter.keyword("tag", "int | str", "0", flags=ParameterFlag.NO_READ | ParameterFlag.NO_WRITE),
    "search_delay"      : Parameter.keyword("delay_search","bool","False",flags=ParameterFlag.NO_READ | ParameterFlag.NO_WRITE),
    "parent"            : Parameter.keyword("parent", "int | str", "0", flags=ParameterFlag.NO_READ | ParameterFlag.NO_WRITE),
    "before"            : Parameter.keyword("before", "int | str", "0", flags=ParameterFlag.NO_READ | ParameterFlag.NO_WRITE),
    "label"             : Parameter.keyword("label", "str | None", "None"),
    "use_internal_label": Parameter.keyword("use_internal_label", "bool", "True"),
    "user_data"         : Parameter.keyword("user_data", "Any", "None"),
    "filter"            : Parameter.keyword("filter_key", "str", '""'),
    "drag_callback"     : Parameter.keyword("drag_callback", "Callable | None", "None"),
    "width"             : Parameter.keyword("width", "int", "0"),
    "pos"               : Parameter.keyword("pos", "Array[int, Literal[0, 2]]", "()", flags=ParameterFlag.NO_READ),
    "tracked"           : Parameter.keyword("tracked", "bool", "False"),
    "track_offset"      : Parameter.keyword("track_offset", "float", "0.5"),
    "height"            : Parameter.keyword("height", "int", "0"),
    "drop_callback"     : Parameter.keyword("drop_callback", "Callable | None", "None"),
    "show"              : Parameter.keyword("show", "bool", "True"),
    "payload_type"      : Parameter.keyword("payload_type", "str", '"$$DPG_PAYLOAD"'),
    "enabled"           : Parameter.keyword("enabled", "bool", "True"),
    "callback"          : Parameter.keyword("callback", "Callable | None", "None"),
    "indent"            : Parameter.keyword("indent", "int", "-1"),
}
_PARAMKIND_CONV_MAP = {
    "KEYWORD_ARG"   : ParameterKind.KEYWORD_ONLY,
    "POSITIONAL_ARG": ParameterKind.POSITIONAL_OR_KEYWORD,
    "REQUIRED_ARG"  : ParameterKind.POSITIONAL_OR_KEYWORD,
}
_DEFAULT_PARAMETERS = (
    _PARAMETER_CONV_MAP["label"],
    _PARAMETER_CONV_MAP["use_internal_label"],
    _PARAMETER_CONV_MAP["user_data"],
    _PARAMETER_CONV_MAP["tag"],
)

_CPPSWITCH_CAPTURE = r".+?(?P<content>switch\s*\(.+?\).+?default:.+?return.+?;).+?}"

_RE_ITEMTYPENAME = re.compile(r"mvAppItemType::(?P<type_name>.+?)(?:\)|,)")


def _get_cppswitch_content(s: str, /) -> list[tuple[list[str], str]]:
    s = s.partition("{")[2].rstrip("}")
    s = ' '.join(_s for _s in s.split() if _s).strip()
    assert s.startswith("case")

    default = s.rpartition("default: ")[2]
    s = s.removesuffix(f"default: {default}")

    result = []

    blocks = [chk for _ in s.split("case") if (chk:=_.strip())]
    cases = []
    for block in blocks:
        cond, _, body = block.partition(": ")
        cases.append(cond.strip().strip(":"))

        body = body.strip()
        if body:
            result.append((cases, body))
            cases = []

    result.append(([], default))

    return result

def _parse_cppswitch(source: str, cppfunc_regex: str, /) -> tuple[list[tuple[list[str], str]], tuple[list[str], str]]:
    regex   = rf"(?s){cppfunc_regex}{_CPPSWITCH_CAPTURE}"
    pattern = re.compile(regex)
    content = pattern.search(source).group("content")  # type: ignore
    content = _get_cppswitch_content(content)
    default = content.pop(-1)

    return content, default

def _trim_cppnamespaces(strings: typing.Sequence[str], /) -> list[str]:
    return [s.rpartition("::")[-1] for s in strings]

def _clean_itemtype_names(type_names, /):
    return [name.removeprefix("mvAppItemType::") for name in type_names]


class _SourceParser(typing.Protocol):
    def __call__(self, source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None: ...


_PARSER_FILE_MAP = {}

def _source_parser[T: _SourceParser](filename: str, /) -> typing.Callable[[T], T]:
    def register_processor(processor, /):
        processors = _PARSER_FILE_MAP.get(filename)
        if processors is None:
            processors = _PARSER_FILE_MAP[filename] = []

        processors.append(processor)
        return processor

    filename = os.path.normpath(filename)

    return register_processor


@_source_parser("mvAppItem.cpp")
def _parse_states(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    pattern = re.compile(
        r"(?s)static\s+bool\s+CanItemType(?:Be|Have)"
        r"(?P<state>.+?)\(mvAppItemType.+?\{(?P<content>.+?)\}"
    )

    for match in pattern.finditer(source):
        state, cppswitch = match.groups()
        try:
            flag = _STATE_CONV_MAP[state]
        except KeyError:
            if state == "RectMax":
                continue
            raise

        content = _get_cppswitch_content(cppswitch)
        assert len(content) == 2

        conds, body = content[0]
        type_names = _trim_cppnamespaces(conds)

        for type_name in type_names:
            typedef_map[type_name].flags |= flag


@_source_parser("mvAppItem.cpp")
def _parse_flags(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    content, default = _parse_cppswitch(source, r"DearPyGui::GetEntityDescr?iptionFlags\(mvAppItemType.+?\{")

    for conds, body in content:
        type_names = _trim_cppnamespaces(conds)

        flags = FeatureFlag.NONE

        for flag_name in body.split("|"):
            flag_name = flag_name.partition("MV_ITEM_DESC_")[-1].strip(";\n\r\t ")
            # these can be inferred via item type name if needed e.g. `"handler" in name`
            if flag_name in ('', "HANDLER", "DRAW_CMP"):
                continue

            if flag_name == "CONTAINER":
                flags |= FeatureFlag.PARENT
            else:
                flags |= FeatureFlag[flag_name]

        if not (flags & FeatureFlag.ROOT):
            flags |= FeatureFlag.CHILD

        for type_name in type_names:
            # XXX: plot series are containers and I'm not sure why?
            if type_name.endswith("Series") and type_name != "mvCustomSeries":
                flags_ = flags & ~FeatureFlag.PARENT
            else:
                flags_ = flags

            typedef_map[type_name].flags |= flags_


@_source_parser("mvAppItem.cpp")
def _parse_target_slot(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    content, default = _parse_cppswitch(source, r"DearPyGui::GetEntityTargetSlot\(mvAppItemType.+?\{")
    default = default[1].split()[-1].strip("; \t\n\r")

    for conds, body in content:
        type_names = _trim_cppnamespaces(conds)
        target_slot = int(body.split()[-1].strip("; \t\n\r"))

        for type_name in type_names:
            typedef_map[type_name].target_slot = target_slot  # ty:ignore[invalid-assignment]


@_source_parser("mvAppItem.cpp")
def _parse_value_type(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    content, default = _parse_cppswitch(source, r"DearPyGui::GetEntityValueType\(mvAppItemType.+?\{")

    for conds, body in content:
        type_names = _trim_cppnamespaces(conds)
        value_type = _TYPE_CONV_MAP[body.rpartition("::")[2].strip("{},;() \t\n\r")]

        for type_name in type_names:
            typedef_map[type_name].value_type = value_type


@_source_parser("mvAppItem.cpp")
def _parse_parents(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    content, default = _parse_cppswitch(source, r"DearPyGui::GetAllowableParents\(mvAppItemType.+?\{")

    for conds, body in content:
        type_names = _trim_cppnamespaces(conds)
        parents    = [obj for obj in _trim_cppnamespaces(_RE_ITEMTYPENAME.findall(body))]

        for type_name in type_names:
            typedef_map[type_name].parents.extend(parents)  # ty:ignore[unresolved-attribute]


@_source_parser("mvAppItem.cpp")
def _parse_children(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    content, default = _parse_cppswitch(source, r"DearPyGui::GetAllowableChildren\(mvAppItemType.+?\{")

    for conds, body in content:
        type_names = _trim_cppnamespaces(conds)
        children   = [obj for obj in _trim_cppnamespaces(_RE_ITEMTYPENAME.findall(body))]

        for type_name in type_names:
            if not type_name.endswith("Series") or type_name == "mvCustomSeries":
                typedef_map[type_name].children.extend(children)  # ty:ignore[unresolved-attribute]


@_source_parser("mvAppItem.cpp")
def _parse_parameters(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    content = re.search(
        r"(?s)DearPyGui::GetEntityParser\(mvAppItemType.+?\{" + _CPPSWITCH_CAPTURE,
        source,
    ).group("content")  # ty:ignore[unresolved-attribute]

    buffer = []
    for s in content.partition("{")[2].rpartition("default:")[0].split():
        s = s.strip()
        if s:
            buffer.append(s)

    blocks = re.split(r"case\s+mvAppItemType::(?P<type_name>.+?):", ' '.join(buffer))
    while blocks[0] == '':
        blocks.pop(0)
    for i, block in enumerate(reversed(blocks)):
        if block.rstrip().endswith("}"):
            del blocks[len(blocks) - i:]
            break

    EMPTY = Parameter.empty

    search_args_start  = re.compile(r"\s*\(\s*{\s*(?P<content>mvPyDataType::.+)").search
    search_args_end    = re.compile(r"(?P<content>\s*}\s*\)\s*)$").search
    search_common_args = re.compile(r".+?\s*\)\s*\(\s*(?P<content>MV_PARSER_ARG_.+?)\s*\)\s*").search

    argreg_overload_searches = [
        re.compile(r"^mvPyDataType::\s*(?P<content>[\w_][\w\d]+?)\s*,").search,
        re.compile(r"^\"(?P<content>[\w_][\w\d]*?)\".").search,
        re.compile(r"^mvArgType::\s*(?P<content>[\w_][\w\d]+).").search,
        re.compile(r"^\"(?P<content>.*?)(?<!\\)\"").search,
        re.compile(r"^\"(?P<content>.*?)(?<!\\)\"").search,
    ]
    argreg_fallback_values: list[typing.Any] = (
        [EMPTY] * len(argreg_overload_searches)
    )

    version = tuple(
        int(s) for s in
        metadata.version.lower().strip(string.ascii_letters + string.punctuation + string.whitespace).split(".")[:2]
    )
    deprecations = set()
    for v, arguments in _PARAMETER_DEPRECATIONS.items():
        if version >= v:
            deprecations.update(arguments)

    while blocks:
        type_name = _trim_cppnamespaces((blocks.pop(0),))[0]
        type_info = typedef_map[type_name]

        unique_params = []
        common_params = [*_DEFAULT_PARAMETERS]

        params_seen = set(p.name for p in common_params)

        statements = blocks.pop(0).rpartition("break;")[0].strip("{} \t\r").split(';')
        iterator   = iter(statements)
        for stmt in iterator:
            stmt = stmt.strip("{} \t\r")
            if not stmt or stmt.startswith("//"):
                continue

            if (match := search_common_args(stmt)) is not None:
                content = match.group("content")

                for s in content.split("|"):
                    p_name = s.strip().removeprefix("MV_PARSER_ARG_").lower()

                    param = _PARAMETER_CONV_MAP[p_name]
                    if param.name in params_seen:
                        continue
                    params_seen.add(param.name)

                    if param.name not in deprecations:
                        common_params.append(param)

            elif (match := search_args_start(stmt)) is not None:
                content = match.group("content")
                while (match := search_args_end(content)) is None:
                    content += f" {next(iterator)}"  # shouldn't be empty

                if "DEPRECATED" in content:
                    continue

                parsed_values = argreg_fallback_values.copy()
                for i, search in enumerate(argreg_overload_searches):
                    content = content.lstrip(" \t\r,")

                    if (match := search(content)) is None:
                        break

                    parsed_values[i] = match.group("content")

                    content = content.removeprefix(match.group(0))

                p_anno, p_name, p_kind, p_default, p_help = parsed_values

                if p_name in params_seen or p_name in deprecations:
                    params_seen.add(p_name)
                    continue
                assert isinstance(p_anno, str)
                assert isinstance(p_name, str)

                p_anno = _TYPE_CONV_MAP[p_anno.strip()]

                if p_kind == "REQUIRED_ARG":
                    p_default = EMPTY

                try:
                    p_kind = _PARAMKIND_CONV_MAP[p_kind]  # ty:ignore[invalid-argument-type]
                except KeyError:
                    if p_default is not EMPTY:
                        p_kind = ParameterKind.KEYWORD_ONLY
                    else:
                        p_kind = ParameterKind.POSITIONAL_OR_KEYWORD

                if p_default is not EMPTY:
                    try:
                        default_ = eval(p_default)  # type: ignore
                    except SyntaxError: pass
                    except NameError:
                        _tmp = p_default.partition('.')[-1]  # type: ignore
                        assert _tmp
                        p_default = f"_dearpygui.{_tmp}"
                    else:
                        if isinstance(default_, (list, tuple)):
                            p_default = repr(tuple(default_))

                            count = len(default_)
                            if "_size" in p_name:
                                p_anno = f"Array[int, Literal[{count}]]"
                            elif "color" in p_name or count == 4 and abs(default_[-1]) == 255:
                                p_anno = "Array[int, Literal[3, 4]]"
                        elif isinstance(default_, float) and "float" not in p_anno:
                            p_anno = p_anno.rstrip() + " | float"
                else:
                    assert p_kind == ParameterKind.POSITIONAL_OR_KEYWORD

                p_flags = ParameterFlag.NONE

                if (
                    ((p_anno == "int | str" or p_anno == "str | int" or p_anno == "Item") and p_name != "source")
                    or
                    "default" in p_name or "value" in p_name or p_name.startswith("init") or p_name.endswith("tag")
                    or
                    len(p_name) == 1 or (len(p_name) == 2 and p_name[-1].isdigit())
                ):
                    p_flags |= ParameterFlag.NO_READ | ParameterFlag.NO_WRITE

                elif p_name == "size" and type_name == "mvFont" and metadata.semver >= (2, 3):
                    p_flags |= ParameterFlag.NONE

                elif p_kind == ParameterKind.POSITIONAL_OR_KEYWORD:
                    value_type = type_info.value_type or ''
                    if value_type.startswith("Array") and value_type.removeprefix("Array[").startswith(str(p_default)):
                        p_flags |= ParameterFlag.NO_READ
                    # `mvRadioButton`, `mvCombo`, `mvListbox`, etc
                    elif not (p_name == "items" and p_default == "()"):
                        p_flags |= ParameterFlag.NO_WRITE

                elif p_name == "category" and type_name in ("mvThemeColor", "mvThemeStyle"):
                    p_flags |= ParameterFlag.NO_WRITE

                elif p_name == "format" and type_name == "mvRawTexture":
                    p_flags |= ParameterFlag.NO_READ | ParameterFlag.NO_WRITE

                param = Parameter(name=p_name, kind=p_kind, annotation=p_anno, default=p_default, flags=p_flags)

                unique_params.append(param)

        parameters = type_info.parameters = [*type_info.parameters]
        assert len(parameters) == 0
        parameters.extend(unique_params)
        parameters.extend(common_params)

        if "tracked" in params_seen and "track_offset" not in params_seen:
            index = parameters.index(_PARAMETER_CONV_MAP["tracked"]) + 1
            parameters.insert(index, _PARAMETER_CONV_MAP["track_offset"])

        if "pos" in params_seen:
            type_info.flags |= FeatureFlag.SUPPORTS_POSITIONING


@_source_parser("mvAppItem.h")
def _parse_commands(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    content, default = _parse_cppswitch(source, r"GetEntityCommand\(mvAppItemType.+?\{")

    for conds, body in content:
        type_names = _trim_cppnamespaces(conds)
        command    = body.split('"', 2)[1]
        assert command.startswith("add_") or command.startswith("draw_")

        for type_name in type_names:
            typedef_map[type_name].command = command


@_source_parser("dearpygui.cpp")
def _parse_constants(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    match = re.search(r"(?s)GetModuleConstants\(.+?\{(?P<content>.+?)return\s+\w+Constants;\s*\}", source)
    assert match is not None

    content = match.group("content")
    pattern = re.compile(r'push_back\s*\(\s*\{\s*"(?P<variable>mv.+?)"\s*,.*?\}\s*\)\s*;')

    constants = [m.group("variable") for m in pattern.finditer(content)]
    metadata.constants = [*metadata.constants, *constants]


@_source_parser("dearpygui.cpp")
def _parse_functions(source: str, typedef_map: dict[str, ItemTypeInfo], metadata: DearPyGuiMetadata, /) -> None:
    pattern = re.compile(r"MV_ADD_COMMAND\s*\(\s*(?P<variable>[_a-zA-Z][_a-zA-Z0-9]+)\s*\)\s*;")

    functions = [m.group("variable") for m in pattern.finditer(source)]
    metadata.functions = [*metadata.functions, *functions]


def _parse(archive: zipfile.ZipFile, version, /):
    metadata = DearPyGuiMetadata(version)

    typedef_map = collections.defaultdict(lambda: ItemTypeInfo('', ''))
    parser_map  = _PARSER_FILE_MAP.copy()

    for fileinfo in archive.filelist:
        filename = os.path.normpath(fileinfo.filename)

        for fp in parser_map:
            if filename.endswith(fp):
                parsers = parser_map.pop(fp)
                break
        else:
            continue

        with archive.open(fileinfo, "r") as file:
            source = file.read().decode("utf-8")

        for parser in parsers:
            parser(source, typedef_map, metadata)

        if len(parser_map) == 0:
            break

    # post-processing
    for type_name, type_info in typedef_map.items():
        type_info.name = type_name

        if not (type_info.flags & FeatureFlag.ROOT):
            type_info.flags |= FeatureFlag.CHILD

        value_type = type_info.value_type
        if isinstance(value_type, str) and value_type.startswith("Array"):
            type_info.flags |= FeatureFlag.ADDRESSABLE

        assert type_info.flags & FeatureFlag.PARENT or type_info.flags & FeatureFlag.CHILD
        assert not (type_info.flags & FeatureFlag.ROOT and type_info.flags & FeatureFlag.CHILD)

    metadata.typedef = sorted(typedef_map.values(), key=lambda info: info.name)

    return metadata

@typing.overload
def parse(dir_or_zipfile_path: str | os.PathLike[str], /, version: str | None = None) -> DearPyGuiMetadata: ...
@typing.overload
def parse(archive: zipfile.ZipFile, /, version: typing.Any = None) -> DearPyGuiMetadata: ...
def parse(obj, /, version=None) -> DearPyGuiMetadata:
    if version is None:
        version = ''

    if isinstance(obj, zipfile.ZipFile):
        archive = obj
        opened  = False
    else:
        opened = True

        fspath = getattr(obj, "__fspath__", None)
        if callable(fspath):
            obj = fspath()

        fpath = pathlib.Path(obj)

        if zipfile.is_zipfile(fpath):
            archive = zipfile.ZipFile(fpath, 'r')
        else:
            if not fpath.is_dir():
                raise ValueError("file path is not a directory or ZIP file")

            patterns = tuple(zip(
                _PARSER_FILE_MAP,
                (re.compile(r"(?:.*?[/\\])?(" + re.escape(fn) + r")$") for fn in _PARSER_FILE_MAP)
            ))

            archive = zipfile.ZipFile(io.BytesIO(), 'w')

            dirpaths = [fpath / "src", fpath / "dearpygui"]
            while dirpaths:
                with os.scandir(dirpaths.pop(0)) as diriter:
                    for entry in diriter:
                        if entry.is_dir(follow_symlinks=False):
                            dirpaths.insert(0, pathlib.Path(entry.path))
                            continue

                        for filename, pattern in patterns:
                            if pattern.match(entry.path):
                                break
                        else:
                            continue

                        try:
                            zfstream = archive.open(filename, "w")
                            fsstream = open(entry.path, "rb")
                            zfstream.write(fsstream.read())
                        finally:
                            zfstream.close()
                            fsstream.close()

    try:
        md = _parse(archive, version)
    finally:
        if opened:
            archive.close()

    return md




# [ github utils ]

def download_zipfile(url: str, /):
    import urllib.request

    with urllib.request.urlopen(url) as resp:
        payload = resp.read()

    return zipfile.ZipFile(io.BytesIO(payload))

def get_dearpygui_releases(owner: str = "hoffstadt", repo: str = "DearPyGui"):
    import json
    import urllib.request

    with urllib.request.urlopen(f"https://api.github.com/repos/{owner}/{repo}/tags") as resp:
        payload = resp.read()

    return json.loads(payload.decode("utf-8"))

def download_dearpygui_release(tag: str = "latest", /, **kwargs) -> tuple[str, zipfile.ZipFile]:
    releases = get_dearpygui_releases(**kwargs)
    if tag.lower() == 'latest':
        release = releases[0]
    else:
        for release in releases:
            name = release["name"]
            if tag == name:
                break
        else:
            raise ValueError(f"{tag!r} not found")

    tag = release["name"].lstrip(" v ")
    url = release["zipball_url"]

    return tag, download_zipfile(url)




if __name__ == "__main__":
    # version, archive = _download_release()
    version, archive = "2.2.0", r"C:\Users\C69819\Downloads\DearPyGui-2.2.0.zip"
    md  = parse(archive, version)
    md2 = deserialize(serialize(md))
    assert md == md2
