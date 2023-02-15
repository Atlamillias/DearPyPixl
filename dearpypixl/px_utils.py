import functools
import contextlib
import itertools
import types
import inspect
from inspect import Parameter, _ParameterKind
from dearpygui import dearpygui as dpg, _dearpygui as _dpg
from .px_typing import (
    T, P,
    Any,
    ItemId,
    Array,
    DPGCallback,
    DPGCommand,
    DPG_CONFIG_DICT,
    DPG_INFO_DICT,
    DPG_STATES_DICT,
    PXLErrorFn,
    List,
    Tuple,
    Iterable,
    Callable,
    Sequence,
    Generator,
)




########################################
######## CLASS-BOUND UTILITIES #########
########################################

class classproperty(property):  # pyright special-cases property (== attribute, vs method)
    """Descriptor/decorator for binding class-level read-only properties."""

    # NOTE: This is functionally equivelent to chaining classmethod & property
    # in Python 3.9. Due to numerous problems as data descriptors, classmethod
    # chaining was deprecated in 3.11 (no weird behavior without __set__).

    __slots__ = ("__wrapped__",)

    def __init__(self, fn):
        self.__wrapped__ = fn

    def __set_name__(self, cls, name):
        # If the "original" callable is a descriptor, invoke its setname method.
        if set_name:=getattr(self.__wrapped__, "__set_name__", None):
            set_name(cls, name)

    def __get__(self, instance, cls):
        return self.__wrapped__(cls)




########################################
######### DPG GETTERS/SETTERS ##########
########################################

# CONFGURATION
def get_config(item: ItemId) -> DPG_CONFIG_DICT: ...
get_config = _dpg.get_item_configuration

def set_config(item: ItemId, **kwargs: DPG_CONFIG_DICT) -> None: ...
set_config = _dpg.configure_item


# VALUE
def get_value(item: ItemId) -> Any: ...
get_value = _dpg.get_value

def get_values(items: Sequence[ItemId]) -> list[Any]: ...
get_values = _dpg.get_values

def set_value(item: ItemId, value: Any) -> None: ...
set_value = _dpg.set_value

def set_values(items: Iterable[ItemId], values: Sequence[Any]) -> None:
    """Set values on several items. Stops once the shortest iterable is exhausted.

    Args:
        * items: Identifiers of items that will have their values set.
        * values: Values to apply to items.

    The value of each item in *items* will be set to the value in *values* at
    the same index.
    """
    for value, item in zip(values, items):
        set_value(item, value)


# INFO
def get_info(item: ItemId) -> DPG_INFO_DICT: ...
get_info = _dpg.get_item_info


# STATE
def get_state(item: ItemId) -> DPG_STATES_DICT: ...
get_state = _dpg.get_item_state




########################################
########## DPG ITEM UTILITIES ##########
########################################

# BUG: `dearpygui.generate_uuid` has considerable performance issues. The more uuids
# that exist, the longer it takes it takes `dearpygui.generate_uuid` to run.

# This workaround is problematic since collisions are possible when using the
# DPG API to create items (thus letting DPG generate it's own uuids). To help
# mitigate this, `start` is set a *little* high.
def generate_uuid() -> int:
    """Return an available integer item identifier."""

generate_uuid = itertools.count(start=1_000_000).__next__


def item_from_callable(_callable: DPGCommand, *args, **kwargs) -> ItemId:
    """Return the result of invoking a callable that returns or yields an item
    identifier. Any additional arguments passed to this function are sent to the
    callable.

    This will process any callable from DearPyGui that creates an item.


    >>> from dearpygui import dearpygui

    """
    item_uuid = _callable(*args, **kwargs)
    if isinstance(item_uuid, contextlib.ContextDecorator):
        item_uuid = item_uuid.__enter__()
        item_uuid.__exit__()
    return item_uuid


def is_item_cmd(_object: Any, /) -> bool:
    """Return True if an object is a callable defined in DearPyGui that creates
    and yields/returns an item identifier.

    Args:
        * _object: The object to inspect.


    >>> from dearpygui import dearpygui
    ...
    >>> is_item_cmd(dearpygui.window)
    True
    >>> is_item_cmd(dearpygui.add_window)
    True
    >>> is_item_cmd(dearpygui.configure_item)
    False
    >>> is_item_cmd(dearpygui.mutex)
    False
    >>> def non_dpg_fn(*args, tag: int | str = 0) -> int | str: ...
    >>> is_item_cmd(non_dpg_fn)
    False
    """
    # TODO: Look for false positives.
    try:
        signature = inspect.signature(_object)
    except:
        return False  # not callable or is built-in
    # defined in DPG
    if dpg.__name__ not in _object.__module__:
        return False
    # accepts an ItemId keyword argument
    if all(kwd not in signature.parameters for kwd in ("tag", "id")):
        return False
    # returns an ItemId
    if signature.return_annotation != ItemId:
        return False

    # minor optimization for future calls to `signature`
    if not hasattr(_object, "__signature__"):
        _object.__signature__ = signature
    return True


def is_ctxmgr_fn(_object: Any, /) -> bool:
    """Return True if a function is wrapped by `contextlib.contextmanager`.

    Args:
        * _object: The object to inspect.


    >>> from dearpygui import dearpygui
    ...
    >>> is_ctxmgr_fn(dearpygui.window)
    True
    >>> is_ctxmgr_fn(dearpygui.add_window)
    False
    >>> is_ctxmgr_fn(dearpygui.child_window)
    True
    >>> is_ctxmgr_fn(dearpygui.add_child_window)
    False
    >>> is_ctxmgr_fn(dearpygui.mutex)
    True
    """
    # XXX checking `co_name`, `co_names`, and `co_filename` on `__code__` is more
    # accurate, but I can't confirm the reliability of code objects.
    is_ctx_manager = all((
        callable(_object),
        _object.__globals__["__name__"] == "contextlib",
        _object.__module__ != "contextlib",
        isinstance(getattr(_object, "__wrapped__", None), types.FunctionType),
    ))
    return is_ctx_manager or False


def is_ok_dpg_callback(_object: Any, /) -> bool:
    """Return True if DearPyGui will be able to call the object."""
    return hasattr(_object, "__code__")


def does_itemid_exist(item_id: ItemId) -> bool:
    """Return True if an identifier is being used by DearPyGui."""
    # Despite their type-hints, the `item` param for `does_item/alias_exist` is type-sensitive
    # and will throw SystemError instead of just returning False.
    if isinstance(item_id, int):
        fn = _dpg.does_item_exist
    elif isinstance(item_id, str):
        fn = _dpg.does_alias_exist
    else:
        return False
    return fn(item_id)


@contextlib.contextmanager
def push_container(container_item: ItemId):
    try:
        _dpg.push_container_stack(container_item)
        yield container_item
    finally:
        if _dpg.top_container_stack() == container_item:
            _dpg.pop_container_stack()


def item_generator(item_factory: Callable[P, T], *args: P.args, **kwargs: P.kwargs) -> Generator[T, None, None]:
    """A generator that yields items indefinitely.

    Args:
        * item_factory: DearPyGui function or similar callable that returns/yields
        an item identifier.
        * args/kwargs: Positional/keyword-only arguments appropriate for *item_factory*.
    """
    while True:
        yield item_factory(*args, **kwargs)


def get_root_items() -> list[ItemId]:
    """Return the identifiers of all existing top-level items."""
    return [item for item in _dpg.get_all_items() if get_info(item)["parent"]]


def get_root_parent(item: ItemId) -> ItemId:
    current_item = item
    while (parent:=get_info(current_item)["parent"]):
        current_item = parent
    return current_item



########################################
######### PX INTERNAL HELPERS ##########
########################################

def create_parameter(
    name: str,
    *,
    kind      : _ParameterKind = Parameter.POSITIONAL_OR_KEYWORD,
    annotation: Any            = Parameter.empty,
    default   : Any            = Parameter.empty
) -> Parameter:
    return Parameter(name, kind, default=default, annotation=annotation)


def upd_param_annotations(parameters: dict[str, inspect.Parameter]) -> dict[str, inspect.Parameter]:
    """Updates source DPGCommand parameters with more accurate and/or PX annotations."""
    upd_params = {}
    for param in parameters.values():
        if param.kind == Parameter.VAR_KEYWORD:
            continue

        p_name = param.name
        p_anno = param.annotation

        # formatting (specific-case)
        if p_name == "pos":
            p_anno = Array[int, int]
        elif "callback" in param.name:
            p_anno = DPGCallback
        elif p_anno == ItemId:
            p_anno = "ItemId"
        elif "color" in p_name or (param.default and isinstance(param.default, tuple)
        and len(param.default) == 4 and p_anno == (List[int] | Tuple[int, ...])):
            p_anno = Array[int, int, int, int | None]
        else:  # general-case
            for tp in str, float, int:
                if p_anno != (List[tp] | Tuple[tp, ...]):
                    continue
                p_anno = Sequence[tp]
                break
        upd_params[p_name] = Parameter(p_name, param.kind, default=..., annotation=p_anno)
    return upd_params


def writable_cfg_from_params(parameters: dict[str, inspect.Parameter]):
    excl_names = "tag", "id", "parent", "default_value"
    excl_n_pts = "default",
    return {p_name: param for p_name, param in parameters.items()
            if param.kind == Parameter.KEYWORD_ONLY
            and p_name not in excl_names
            and not any(pt in p_name for pt in excl_n_pts)}



########################################
######## DPG ITEM ERROR HELPERS ########
########################################

def _get_cmd_err_signature(command: DPGCommand):
    variadics = (inspect.Parameter.VAR_KEYWORD, inspect.Parameter.VAR_POSITIONAL)
    signature = inspect.signature(command)
    return signature.replace(parameters=(
        p for p in signature.parameters.values() if p.kind not in variadics)
    )


def _error_prefix(msg: str = ""):
    def process_err_fn(fn: PXLErrorFn[P]) -> PXLErrorFn[P]:
        @functools.wraps(fn)
        def err_fn_wrapper(*args: P.args, **kwargs: P.kwargs) -> Exception | None:
            err = fn(*args, **kwargs)
            if isinstance(err, Exception):
                err = type(err)(f"{message}{err.args[0]}", *err.args[1:])
            return err
        message = msg
        if message:
            message = f"{message}: "
        return err_fn_wrapper
    return process_err_fn



@_error_prefix()
def err_item_exists(item: ItemId, command: DPGCommand, *args, **kwargs):
    if isinstance(item, int):
        item_exists = dpg.does_item_exist(item)
    elif isinstance(item, str):
        item_exists = dpg.does_alias_exist(item)
    else:
        return TypeError(f"expected int, str identifier (got {item}).")
    if item and item_exists:
        return ValueError("item already exists.")


@_error_prefix("unexpected argument")
def err_arg_unexpected(item: ItemId, command: DPGCommand, *args, **kwargs):
    signature = _get_cmd_err_signature(command)
    try:
        signature.bind_partial(*args, **kwargs)
    except TypeError as e:
        return TypeError(e.args[0].replace(":",""))


@_error_prefix("invalid argument")
def err_arg_invalid(item: ItemId, command: DPGCommand, *args, **kwargs):
    ...


@_error_prefix()
def _err_incompatible_parent(item: ItemId, command: DPGCommand, *args, parent: ItemId = 0, **kwargs) -> Exception | None:
    parent = parent or dpg.top_container_stack()
    if not parent:
        return

    parent_fname = get_info(parent)["type"]
    parent_name  = parent_fname.split("mvAppItemType::mv")[-1].lower()
    child_name   = command.__name__.removeprefix("add_").replace("_", "").lower()
    # Almost pointless to continue if the parent is universal-ish. It may
    # not be compatible, but there's no way to confirm.
    universal_parents = ("stage", "templateregistry",)  # can parent MOST items
    one_parent_items  = ("series", "theme",)            # known items that the above can't parent
    if any(s in parent_name for s in universal_parents):
        if any(s in child_name for s in one_parent_items):
            return ValueError("incompatible parent type.")
        return
    # It's not possible to perfectly determine parent/child compatibility w/o
    # hardcoding it, but a few confident guesses can be made using the parent's
    # type and name of the command used.
    err = f"incompatible parent type for {command.__name__.removeprefix('add_')!r} item (try {{}})."
    if child_name.startswith("draw") and all(s not in parent_name for s in ("drawlist", "stage")):
        return ValueError(err.format("`mvStage`, `mvDrawlist`"))
    elif "handler" in child_name and "handlerregistry" not in parent_name:
        return ValueError(err.format("`mvItemHandlerRegistry`, `mvHandlerRegistry`"))
    elif "theme" in child_name and "theme" not in parent_name:
        return ValueError("`mvTheme`, `mvThemeComponent`")
    elif "plot" in child_name and parent_name != "plot":
        return ValueError("`mvPlot`, `mvPlotLegend`, `mvPlotAxis`, etc")
    elif "series" in child_name and "axis" not in parent_name:
        return ValueError("`mvPlotAxis`")
    elif "node" in child_name and "node" not in parent_name:
        return ValueError("`mvNodeEditor`, `mvNode`, `mvNodeAttribute`, etc.")
    elif "table" in child_name and "table" not in parent_name:
        return ValueError("`mvTable`, `mvTableRow`")
    elif "font" in child_name and "font" not in parent_name:
        return ValueError("`mvFont`, `mvFontRegistry`")
    # possibly missed a special case above (not definitive)
    elif "window" in parent_name:
        return ValueError("incompatible parent type.")


@_error_prefix("invalid `parent`")
def err_parent_invalid(item: ItemId, command: DPGCommand, *args, **kwargs):
    if "parent" not in _get_cmd_err_signature(command).parameters:
        return

    cstack_item = dpg.top_container_stack()
    parent_item = kwargs.get("parent", 0)
    # CASE 1: `parent` is not `int` nor `str` (also prevents error in CASE 2)
    if not isinstance(parent_item, (int, str)):
        return ValueError(f"expected `int` or `str` (got {type(parent_item)!r}).")
    # CASE 2: the included parent does not exist
    if parent_item and not dpg.does_item_exist(parent_item):
        return ValueError("item does not exist.")
    # CASE 3: did not include parent while the container stack is empty
    elif not parent_item and not cstack_item:
        return TypeError("missing argument (container stack is empty).")
    # CASE 4: a parent is available, but maybe incompatible
    return _err_incompatible_parent(item, command, *args, **kwargs)


@_error_prefix()
def err_create_item(item: ItemId, command: DPGCommand, *args, **kwargs) -> Exception:
    """Return an appropriate exception when a DPG item could not be created."""
    err_fns = (
        # TEST 1: check if the item already exists/check the pytype of `item`
        err_item_exists,
        # TEST 2: check for invalid arguments (BUG: triggers on deprecated arguments)
        err_arg_unexpected,
        # TEST 3: check the `parent` argument
        err_parent_invalid,
        # TEST 4: check argument types (TODO)
        err_arg_invalid,
    )
    for err_fn in err_fns:
        if err:=err_fn(item, command, *args, **kwargs):
            return err
    # *waves white flag of surrender*
    return SystemError("could not create item -- verify that the arguments are appropriate.")


########################################
######### MISCELLANEOUS UTILS ##########
########################################

def forward_method(target: str, name: str = None, *, call: bool = False):
    """Calls to a bound method wrapped by this function will instead call the method of
    the same name found on `self.target`. The result of that method is returned, while
    the original method is not called.

    This:
    >>> @forward_method("list_obj")
    ... def append(self, obj):
    ...     ...

    Becomes this:
    >>> def append(self, obj):
    ...     return self.list_obj.append(obj)

    If *call* is True, then the method is looked up on the result of calling
    `self.target` without arguments.
    """

    def process_method(mthd):
        if not call:
            @functools.wraps(mthd)
            def forwarded_method(self, *args, **kwargs):
                return getattr(getattr(self, target), mthd_name)(*args, **kwargs)
        else:
            @functools.wraps(mthd)
            def forwarded_method(self, *args, **kwargs):
                return getattr(getattr(self, target)(), mthd_name)(*args, **kwargs)
        mthd_name = name or mthd.__name__
        return forwarded_method

    if not isinstance(target, str):
        raise TypeError(f"`attr` expected as a string, got {type(target).__qualname__!r}.")
    return process_method



