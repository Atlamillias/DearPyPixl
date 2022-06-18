import inspect
import typing
from inspect import Signature, Parameter
from typing import TYPE_CHECKING, Union, Collection, Any, get_origin, get_args
from dearpygui import dearpygui as dpg

ItemT       = None
TemplateT   = None
WidgetItemT = None
if TYPE_CHECKING:
    from dearpypixl.itemtypes import ItemT, TemplateT, WidgetItemT


class _DearPyPixlErrorType(type):
    def __str__(cls) -> str:
        return f"<class {cls.__qualname__!r}>"  # no namespace path


class Error(Exception, metaclass=_DearPyPixlErrorType):
    ...


class DearPyGuiError(Error):
    """Error representing a SystemError thrown from DearPyGui. An attempt
    should first be made to diagnose any DearPyGui errors and throw an
    appropriate built-in exception before this one (i.e. this is a last
    resort).
    """
    message = "DearPyGui raised an error that could not be identified{}."

    def  __init__(self, comment: str = "", *args):
        if comment:
            comment = f": {comment}"
        self.message = self.message.format(comment)
        super().__init__(self.message, *args)

    def __str__(self):
        return self.message


def  _get_annotation_types(annotation: object):
    # get_origin(typing.List) -> built-in `list`, but get_origin(list)
    # -> None. So if it's None the annotation is used for the origin.
    # instead.
    origin = get_origin(annotation) or annotation
    args   = [arg for arg in get_args(annotation) if arg != Ellipsis]
    # The subscript can be Union, too.
    inner_types = [_get_annotation_types(anno) for anno in args] or [Any, []]
    # If there's no subscript, then origin cannot be Union (for
    # type hints).
    if not args or origin is not Union:
        # If origin is not a Union, then it needs to be a Collection
        # for `args` to exist.
        if issubclass(origin, Collection) and not issubclass(origin, (str, bytes, bytearray)):
            return [[annotation, [inner_types]]]
        # Otherwise there shouldn't be any, so pass an empty list.
        return [[annotation, []]]
    elif origin is Union and args:
        return inner_types
    raise TypeError(f"Unsupported annotation type {origin!r}.")

def _get_annotation_types(annotation:  object):
    origin = get_origin(annotation)
    if origin is Union:
        types = []
        for t in get_args(annotation):
            if t is Any:
                types.append(object)
                continue
            types.append(t)
        return tuple(types)
    elif origin:
        if origin is Any:
            return (object,)
        return (origin,)
    return (annotation,)


def err_item_not_created(item: ItemT, arguments: dict):
    """Troubleshoot a SystemError that DearPyGui has thrown while trying
    to create a new item.
    """
    itemtype = type(item)
    itemname = itemtype.__qualname__
    err_msg  = f"Error creating {itemname!r} item: {{}}."

    # Creating a modified signature of the DearPyGui function that
    # was called to create the item, excluding variable parameters.
    _var_args  = (Parameter.VAR_KEYWORD, Parameter.VAR_POSITIONAL)
    _signature = inspect.signature(itemtype.__command__)
    _cmdparams = {name: param for name, param in _signature.parameters.items()
                  if param.kind not in _var_args}
    signature: Signature = _signature.replace(parameters=_cmdparams.values())

    ## TEST 1 ##
    # Check if the constructor received an invalid argument (all
    # DearPyPixl-specific arguments would have been processed or
    # consumed at this point).
    try:
        boundargs = signature.bind_partial(**arguments)
    except TypeError as e:
        msg = e.args[0].replace(":", "")
        raise TypeError(err_msg.format(msg)) from None
    ## TEST 2 ##
    # Check the `parent` argument (a personal pitfall of mine).
    if "parent" in signature.parameters:
        stack_uuid  = dpg.top_container_stack()
        parent_uuid = arguments.get("parent", 0)
        if parent_uuid and not dpg.does_item_exist(parent_uuid):
            raise ValueError(err_msg.format("parent item does not exist")) from None
        # Check the top container on the container stack. If the
        # new item did not include a parent argument (or is default)
        # and the stack is empty, throw an error.
        if not stack_uuid and not parent_uuid:
            raise ValueError(err_msg.format("requires a parent (container stack is empty)")) from None
        # Either the container stack is not empty and there was a parent
        # argument OR the container stack uuid is the acting parent
        # because there's no specified parent; confirm if the parent
        # is suitable for this item.
        elif (not stack_uuid and parent_uuid) or (stack_uuid and not parent_uuid):
            parent       = parent_uuid or stack_uuid
            parent_type  = item.__registry__.get_type(dpg.get_item_info(parent)["type"])
            parent_able_childs = parent_type.able_children()
            item_able_parents  = item.able_parents()
            # If both of these are empty, then it means these items are
            # compatible.
            if not parent_able_childs and not item_able_parents:
                ...
            # This would also indicate compatibility.
            elif itemtype in parent_able_childs or parent_type in item_able_parents:
                ...
            else:
                raise ValueError(err_msg.format("incompatible parent")) from None
    ## TEST 3 ##
    # Compare the type of each argument value with the correspo-
    # nding annotation.
    for arg_name, arg_val in arguments.items():
        value_type  = type(arg_val)
        annotation  = signature.parameters[arg_name].annotation
        outer_types = _get_annotation_types(annotation)
        # Also include the type of the default value if one exists.
        if (default := signature.parameters[arg_name].default) is not Parameter.empty:
            # A duplicate of an existing type won't hurt anything -- add it anyway.
            outer_types = tuple((*outer_types, type(default)))

        if not isinstance(arg_val, outer_types):
            types_str = ", ".join((repr(t.__qualname__) for t in set(outer_types)))
            raise TypeError(err_msg.format(f"unexpected value type for {arg_name!r} (expected {types_str}, got {value_type!r})")) from None
        # Checking to see if the value type is a data structure. If so, type-check the
        # inner values (only 1 level down). If the structure is a dictionary, only the
        # keys are checked.
        # TODO: Thoroughly check all nested value types. Check values for dictionaries.
        if isinstance(arg_val, Collection) and not isinstance(arg_val, (str, bytes, bytearray)):
            inner_types = {_get_annotation_types(t)
                           for t in outer_types if get_args(t) is not Union}
            for inner_val in arg_val:
                for valid_types in inner_types:
                    if isinstance(arg_val, valid_types):
                        continue
                    types_str = ", ".join((repr(t.__qualname__) for t in set(valid_types)))
                    raise TypeError(err_msg.format(f"unexpected inner value type for {arg_name!r} (expected {types_str}, got {type(inner_val)!r})")) from None

    # Wave the white flag of surrender i.e. "I have no clue, you
    # figure it out".
    return DearPyGuiError(f"at '{itemname}.__init__(...)', '{itemname}.__command__(...)'")


def err_if_existential_crisis(item: ItemT) -> None | SystemError | TypeError:
    """Raise SystemError if this item exists in DearPyPixl but not DearPyGui.
    """
    if not dpg.does_item_exist(item.tag):
        return SystemError(f"This item does not or no longer exists; possibly deleted.")
    return None


def err_if_root_item(item: ItemT) -> None | TypeError:
    """Raise TypeError if this item is a root item and cannot be moved.
    """
    if item.__is_root_item__:
        return TypeError(f"Could not move item; {type(item).__qualname__!r} is a root item.")
    return None


def err_template_implementation(attr: str) -> NotImplementedError:
    return NotImplementedError(f"{attr!r} member is not available as a template.")
