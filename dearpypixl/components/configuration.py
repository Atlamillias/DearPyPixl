"""Contains objects used in defining, caching, or managing an item's internal configuration."""
import functools
from typing import Callable, Any, Union
from inspect import signature, _VAR_POSITIONAL, _KEYWORD_ONLY
from dearpygui._dearpygui import (
    # getters
    get_item_configuration,
    get_item_info as _get_item_info,
    get_item_state as _get_item_state,
    get_value,
    # setters
    configure_item,
    set_value,
    bind_colormap
)

CONFIGURATION = "configuration"
INFORMATION   = "information"
STATE         = "state"


def _get_positional_args_count(obj: Callable):
    # Emulating how DearPyGui doesn't require callbacks having 3 positional
    # arguments. Only pass sender/app_data/user_data if there's "room" to 
    # do so.
    pos_arg_cnt = 0
    for param in signature(obj).parameters.values():
        if param.kind == _VAR_POSITIONAL:
            pos_arg_cnt = 3
        elif param.kind != _KEYWORD_ONLY:
            pos_arg_cnt += 1

        if pos_arg_cnt >= 3:
            pos_arg_cnt = 3
            break
    return pos_arg_cnt


def prep_callback(obj, _callback: Callable | None):
    @functools.wraps(_callback)
    def callable_object(_=None, app_data=None, user_data=None, **kwargs):
        args = (obj, app_data, user_data)[0:pos_arg_cnt]
        _callback(*args, **kwargs)
    # Wrapping is done for a couple of reasons. Firstly, to ensure that
    # the Item instance of `sender` is returned instead of the identifier.
    # And second; nuitka compilation doesn't like DPG callbacks unless
    # they are wrapped (lambda, etc.)...for some reason.
    if callable(_callback):
        wrapper = callable_object
        pos_arg_cnt = _get_positional_args_count(_callback)
    elif _callback is None:
        wrapper = None
    else:
        raise ValueError(f"`callback` is not callable (got {type(_callback)!r}.")

    return wrapper


#########################################
#### `ItemAttribute` getters/setters ####
#########################################
ItemAttributeCommands = {}

def item_attr_command(func: Callable):
    """(Decorator) Registers a function as an item attribute command. The name of a
    registered command (string) can be passed as the getter/setter argument
    for an `ItemAttribute` instance."""

    ItemAttributeCommands[func.__qualname__] = func
    return func

# NOTE: These should all share the same signature (mirrors get/setattr).

# Setters
@item_attr_command
def set_item_config(__obj: object, __name: str, value: Any):
    configure_item(__obj._tag, **{__name: value})


@item_attr_command
def set_item_cached_config(__obj: object, __name: str, value: Any):
    # Set DPG configuration and cache the change on instance.
    # Required when the attribute can be set in DPG but not fetched.
    configure_item(__obj._tag, **{__name: value})
    # Set as private attribute
    setattr(__obj, f"_{__name}", value)


@item_attr_command
def set_item_value(__obj: object, __name: str, value: Any):
    # `value`, `default_value`
    set_value(__obj._tag, value)


@item_attr_command
def set_item_cached_colormap(__obj: object, __name: str, value: Any):
    try:
        colormap_uuid = int(value)
    except TypeError:
        raise TypeError(f"{__name!r} must be an instance of `Colormap` (got {type(value).__qualname__!r}).")
    bind_colormap(__obj._tag, colormap_uuid)
    # Can't reliably be fetched, so store the value on instance.
    setattr(__obj, f"_{__name}", value)


@item_attr_command
def set_item_callback(__obj: object, __name: str, value: Any):
    configure_item(__obj._tag, **{__name: prep_callback(__obj, value)})


# Getters
@item_attr_command
def get_item_config(__o: object, __name: str):
    return get_item_configuration(__o._tag)[__name]


@item_attr_command
def get_item_info(__o: object, __name: str):
    return _get_item_info(__o._tag)[__name]


@item_attr_command
def get_item_state(__o: object, __name: str):
    return _get_item_state(__o._tag)[__name]


@item_attr_command
def get_item_value(__o: object, __name: str = None):
    return get_value(__o._tag)


@item_attr_command
def get_item_cached(__o: object, __name: str):
    # Pull private attribute.
    return getattr(__o, f"_{__name}")


##################################
#### Configuration Management ####
##################################



class ItemAttribute:
    """Descriptor object for accessing DearPyGui item attributes. Functionally similar
    to the `property` built-in, but cannot be used as a decorator.

    Attributes:
        * category: str
        * getter: Callable | None
        * setter: Callable | None
        * target: str
        * doc: str
    """
    CONFIGURATION = CONFIGURATION
    INFORMATION   = INFORMATION
    STATE         = STATE

    next_class_item_attrs = {
        CONFIGURATION: set(),
        INFORMATION  : set(),
        STATE        : set(),
        "cached"     : set(),
    }

    def __init__(
        self,
        category: str                        ,
        getter  : Union[str, Callable, None] ,
        setter  : Union[str, Callable, None] ,
        target  : str                        = None,
        doc     : str                        = None,
    ):
        """
        Args:
            * category (str): Value should be `configuration`, `information` or `state`.
            * getter (str | Callable | None): Object that is called to retrieve the 
            attribute value. If the command is registered, the name of the command is also
            an accepted value. A call to the object must be able be resolved using the same
            arguments required for `getattr`, and must accept those arguments.
            * setter (str | Callable | None): Object that is called to set the attribute
            to a passed value. If the command is registered, the name of the command is also
            an accepted value. A call to the object must be able to be resolved using the same
            arguments required for `setattr`, and must accept those arguments.
        """
        self.category = category
        self.fget     = getter
        self.fset     = setter
        self.target   = target

        if doc is None and getter is not None:
            doc = getter.__doc__
        self.__doc__ = doc
        self._name = ''

    def __set_name__(self, __type: type, name: str):
        self._name  = name
        self.target = name if not self.target else self.target
        
        if self.category not in self.next_class_item_attrs:
            raise ValueError(f"`category` must be 'configuration', 'state', or 'information' (got {self.category!r}).")

        for attr in ("fget", "fset"):
            value = getattr(self, attr)
            
            if callable(value):
                item_attr_command(value)  # Verifying signature
                setattr(self, attr, value)
            elif isinstance(value, str):
                try:
                    setattr(self, attr, ItemAttributeCommands[value])
                except KeyError:
                    raise ValueError(f"No registered command found for {value!r}.")
        ItemAttribute.next_class_item_attrs[self.category].add(name)
        # Mark attribute as cached if necessary
        if "cache" in self.fget.__qualname__:
            ItemAttribute.next_class_item_attrs["cached"].add(name)

    def __get__(self, instance: object, _type: type):
        if instance is None:
            return self
        return self.fget(instance, self.target)

    def __set__(self, instance: object, value):
        # NOTE: `try`/`except` blocks are used instead of conditional `if` checks. This may
        #       add overhead to startup and imports, but normal attribute access at runtime
        #       is faster.  
        try:
            self.fset(instance, self.target, value)
        except TypeError as e:
            if self.fset is None:
                raise AttributeError(f"The {self._name!r} attribute is read-only and cannot be set.")
            raise e


def item_attribute(cls_attribute: Union[Callable, str] = None, *, category: str):
    """(Decorator) Alternative to using the `ItemAttribute` descriptor. Registers class-
    defined attributes that are to be managed as item attributes  Useful if
    the behavior of the `ItemAttribute` descriptor isn't suitable, and a more simple/complex
    implementation is required for proper attribute access. If this is used as a method
    decorator, this must be the inner decorator.

    Args:
        * cls_attribute (Callable | str): The attribute to register. If it is a method,
        `cls_attribute.__name__` is registered.
        * category (str, keyword-only): Category to register the attribute under.
        Must be "configuration", "information", or "state".

    Examples:
    >>> class ProtoItem:
    ...     x = item_attribute("x", category="configuration")
    None
    >>> class ProtoItem:
    ...     @property
    ...     @item_attribute(category="configuration")
    ...     def config_property(self):
    ...         ...
    None
    """

    @functools.wraps(cls_attribute)
    def register(obj):
        # Register the attribute by category.
        if isinstance(obj, str):
            name = obj
        elif callable(obj):
            # `obj` should be a method
            name = obj.__name__
        else:
            raise ValueError(f"`obj` must be a string or callable method (got {type(obj)!r}).")
            
        try:
            ItemAttribute.next_class_item_attrs[category].add(name)
        except KeyError:
            raise ValueError(f"`category` must be 'configuration', 'state', or 'information' (got {category!r}).")
        return obj
    
    if cls_attribute:
        return register(cls_attribute)
    return register
    