"""Command API for DearPyPixl.

Glossary:
    * uuid: Refers to an unsigned integer value that is to be used
    to reference an existing item or to an item that will exist.

    * alias: Refers to a string value assigned to a *uuid*. Both it
    and the assigned *uuid* can be used to reference an existing item
    or to an item that will exist.

    * tag: Refers to a *uuid* or *alias*. In the context of Dear PyGui
    functions that create items, *tag* must not be bound to an existing
    item (i.e. cannot be in-use). In the context of Dear PyPixl item
    interfaces, *tag* may or may not be in-use.

    * item: Refers to a *tag* that is currently in-use.

    * interface: An instance Dear PyPixl's `AppItemType` class or
    subclass that wraps Dear PyGui's API. Interfaces can be used as
    values for `uuid`, `tag` and `item` arguments in both Dear PyGui and
    Dear PyPixl.

    * parent: An item that contain other items.

    * children: Items that are parented by another item. A child item
    cannot exist without a *parent*.

    * slot: Refers to an item's child slots. In the context of
    signatures, it refers to the index of the target slot;

        - `0`: Contains `mvFileExtension`, `mvFontRangeHint`, `mvNodeLink`,
        `mvAnnotation`, `mvDragLine`, `mvDragPoint`, `mvLegend`, and
        `mvTableColumn` child item only.

        - `1`: Contains all child items not specifically included in other
        slots.

        - `2`: Contains all drawing-related child items.

        - `3`: Contains `mvDragPayload` child items only.

    * container stack: A structure in Dear PyGui that contains references
    to existing container items. When the stack is not empty, the top-most
    item is used as the *parent* for any item created using a null `parent`
    argument.

    * configuration: Refers to an item's settings that can be updated using
    a general-use API hook.

    * information: Refers to various details regarding an item. Most are
    read-only, while others may be updated through a specific API hook.

    * state: Refers to an item's overall condition. Except for the `pos`
    state, item states are updated frame-by-frame or as a consequence of
    some other change.

    * callback: A callable with a `__code__` attribute that Dear PyGui
    will call when various conditions are met. When called by Dear PyGui,
    it will try to send a maximum of three positional arguments to the
    callable (in order);
        - `sender`: The *item* that *callback* is registered to.
        - `app_data`: A value associated `sender`.
        - `user_data`: The *user_data* value of `sender`.
    Dear PyGui will only send what the callable can accept, so if
    *callback* only accepts two positional arguments, it will pass
    `sender` and `app_data`, but not `user_data`.
"""
# pyright: reportTypedDictNotRequiredAccess=none
import os
import sys
import time
import types
import inspect
import functools
import itertools  # type: ignore
import contextlib
import importlib.metadata
from queue import Queue
from uuid import uuid4
from dearpygui import dearpygui, _dearpygui
from . import common, constants, tools, errors, parsing
from .common import (
    Item as ItemT,
    Any,
    Color,
    Self,
    Array,
    Sequence,
    Callable,
    Property,
    Literal,
    Unpack,
    TypeVar,
    Mapping,
    MappingProxy,
    MutableMapping,
    ParamSpec,
    TypedDict,
    SupportsIndex,

    overload,
    final,
    cast,
    TYPE_CHECKING,

    mvBuffer,
    mvMat4,
    mvVec4,
)
from .tools import Locker
if TYPE_CHECKING:
    from .interface import AppItemType
    from ..items import mvTheme, mvFont




_T = TypeVar("_T")
_P = ParamSpec("_P")

_ItemTree = dict[ItemT, tuple[list['_ItemTree'], list['_ItemTree'], list['_ItemTree'], list['_ItemTree']]]


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# ::::::::::::::::::::::::::::::::::::::::::::::::::::: Internal ::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

_SENTINEL = object()


def _clear_lockers(cls: type[_T]) -> type[_T]:
    """Helper decorator to remove leftover `Locker` references.
    """
    for k in tuple(cls.__dict__):
        v = inspect.getattr_static(cls, k)

        try:
            if isinstance(v, Locker):
                delattr(cls, k)
        except:
            pass

    return cls


def _dearpygui_override(target: Callable, reason: str = ''):
    """Overrides *target* with the decorated function."""
    def capture_fn(fn: Callable[_P, _T]) -> Callable[_P, _T]:
        module = sys.modules[target.__module__]
        setattr(module, target.__name__, fn)
        return fn
    return capture_fn


def _not_implemented(*args, **kwargs) -> Any:
    return NotImplemented


def _onetime_setup(setup_fn: Callable[[], Any], exclusions: Sequence[str] = ()) -> Callable[[type[_T]], type[_T]]:
    # DPX should not create the GPU context automatically, or at
    # very least, there should be some input needed by the user
    # even if it's just accessing the API. For normal items, this
    # is done by a `__new__` wrapper that simply unwraps itself
    # after one call. But most of the runtime API is static -- the
    # API will probably be used before any runtime interfaces are
    # made (if any are made at all).

    # NOTE: Debuggers will almost always trigger the setup.
    def capture_class(cls: type[_T]) -> type[_T]:
        mcls    = type(cls)
        wrapped = {}
        for name in cls.__dict__:
            # Walk around custom metaclass descriptors. Invoking them now
            # will cause a segfault (no GPU context).
            if name.startswith('_') or hasattr(mcls, name) or name in exclusions:
                continue

            value = inspect.getattr_static(cls, name)
            if not isinstance(value, (staticmethod, classmethod)):
                continue

            wrapped[name] = value
            wrapper = type(value)
            value   = value.__wrapped__

            def setup_method_closure(mthd: Callable):
                @functools.wraps(value)
                def method(*args, **kwargs) -> Any:
                    setup_fn()
                    r = mthd(*args, **kwargs)
                    # Replace all of the wrapped members with the
                    # original implementation.
                    for k,v in wrapped.items():
                        setattr(cls, k, v)
                    return r
                method.__name__ = (
                    f'onetime_setup_wrapper ({value.__name__})'
                )
                method.__qualname__ = (
                    f'onetime_setup_wrapper ({cls.__qualname__}.{value.__name__})'
                )
                return wrapper(method)

            setattr(cls, name, setup_method_closure(value))  # type: ignore

        return cls
    return capture_class


# HACK/BUG: This is part2 of the hack in `__init__.py`. Default
# implementation of `generate_uuid` is a HUGE bottleneck creating
# items en masse. This isn't not a micro optimization, but a matter
# of dozens of seconds when creating very large tables, registry
# children, etc. Honestly, I still wonder if it's worth all this
# trouble...
# Both users and dearpypixl MUST use the same implementation to
# avoid uuid collisions. This still doesn't completely fix the problem
# though; aliases are a big issue. When a user calls a DPG function to
# create an item and uses an alias, Dear PyGui will check its' alias
# registry only far enough to check if it exists, and will throw an
# error if it does. Otherwise, it creates a uuid and binds it to the
# alias. And nothing can be done about it. Nothing. Fortunately,
# users tend to only create aliases for important items. Using Dear
# PyGui's API, this can't be more than 100,000 items, right...?
# Otherwise, why even use Dear PyPixl?
_create_uuid : Callable[[], int] = itertools.count(start=100_000).__next__
_dearpygui_override(_dearpygui.generate_uuid)(lambda: _create_uuid())








# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::: API ::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# It's best to think of the classes below as modules. Because that's
# what they are -- inheritable modules.

from dearpygui._dearpygui import (
    setup_dearpygui as _app_prepare,
    bind_font as _app_set_font,
    bind_theme as _app_set_theme,
)


class _AppConfiguration(TypedDict, total=False):
    docking                   : bool
    docking_space             : bool
    load_init_file            : str
    init_file                 : str
    auto_save_init_file       : bool
    device                    : int
    auto_device               : bool
    allow_alias_overwrites    : bool
    manual_alias_management   : bool
    skip_required_args        : bool
    skip_positional_args      : bool
    skip_keyword_args         : bool
    wait_for_input            : bool
    manual_callback_management: bool


class _ApplicationMeta(common.ItemInterfaceMeta):
    # XXX: All of this needs to be set onto into `Application`
    # as well. Instances need their own hooks since their lookup
    # procedure doesn't extend this far up.
    docking                   : Property[bool] = common.ItemConfig()
    docking_space             : Property[bool] = common.ItemConfig()
    load_init_file            : Property[str]  = common.ItemConfig()
    init_file                 : Property[str]  = common.ItemConfig()
    auto_save_init_file       : Property[bool] = common.ItemConfig()
    device                    : Property[int]  = common.ItemConfig()
    auto_device               : Property[bool] = common.ItemConfig()
    allow_alias_overwrites    : Property[bool] = common.ItemConfig()
    manual_alias_management   : Property[bool] = common.ItemConfig()
    skip_required_args        : Property[bool] = common.ItemConfig()
    skip_positional_args      : Property[bool] = common.ItemConfig()
    skip_keyword_args         : Property[bool] = common.ItemConfig()
    wait_for_input            : Property[bool] = common.ItemConfig()
    manual_callback_management: Property[bool] = common.ItemConfig()

    @property
    def theme(self) -> 'mvTheme | Item | None':
        """[get] Return the application-level theme."""
        theme = self.get_theme()
        try:
            return Registry.__itemtype_registry__['mvAppItemType::mvTheme'].new(
                theme
            ) if theme else theme
        except KeyError:
            return theme
    @theme.setter
    def theme(self, value: ItemT | None) -> None:
        """[set] Set application-level theme."""
        return self.set_theme(value)

    @property
    def font(self) -> 'mvFont | Item | None':
        """[get] Return the application-level font item."""
        font = self.get_font()
        try:
            return Registry.__itemtype_registry__['mvAppItemType::mvFont'].new(
                font
            ) if font else font
        except KeyError:
            return font
    @font.setter
    def font(self, value: ItemT) -> None:
        """[set] Set the application-level font item."""
        self.set_font(value)

    @property
    def is_ok(self):
        """[get] Return True if the application has undergone its'
        setup procedure.
        """
        return Application.state()['ok']

    @property
    def clipboard_text(self):
        """[get] Return the current text value of the clipboard."""
        return self.get_clipboard_text()
    @clipboard_text.setter
    def clipboard_text(self, text: str):
        """[set] Set a text value onto the clipboard."""
        self.set_clipboard_text(text)

    def __repr__(self) -> str:
        return f"<class {self.__qualname__!r}>"


@_onetime_setup(lambda: Application(), ("create_context", "prepare", "state"))
@_clear_lockers
class Application(common.ItemInterface, int, metaclass=_ApplicationMeta):
    """Thread-safe, multi-paradigm "application" API for Dear PyGui
    and Dear PyPixl.

    Using Dear PyGui's API over this API will not invalidate any
    settings or states, including those uniquely exposed through
    Dear PyPixl.
    """
    docking                    = cast(bool, _ApplicationMeta.docking)
    docking_space              = cast(bool, _ApplicationMeta.docking_space)
    load_init_file             = cast(str , _ApplicationMeta.load_init_file)
    init_file                  = cast(str , _ApplicationMeta.init_file)
    auto_save_init_file        = cast(bool, _ApplicationMeta.auto_save_init_file)
    device                     = cast(int , _ApplicationMeta.device)
    auto_device                = cast(bool, _ApplicationMeta.auto_device)
    allow_alias_overwrites     = cast(bool, _ApplicationMeta.allow_alias_overwrites)
    manual_alias_management    = cast(bool, _ApplicationMeta.manual_alias_management)
    skip_required_args         = cast(bool, _ApplicationMeta.skip_required_args)
    skip_positional_args       = cast(bool, _ApplicationMeta.skip_positional_args)
    skip_keyword_args          = cast(bool, _ApplicationMeta.skip_keyword_args)
    wait_for_input             = cast(bool, _ApplicationMeta.wait_for_input)
    manual_callback_management = cast(bool, _ApplicationMeta.manual_callback_management)

    theme = cast(ItemT | None, _ApplicationMeta.theme)
    font  = cast(ItemT | None, _ApplicationMeta.font)

    is_ok = cast(bool, _ApplicationMeta.is_ok)

    clipboard_text = cast(str, _ApplicationMeta.clipboard_text)

    def __new__(cls, **kwargs: Unpack[_AppConfiguration]) -> Self:
        return super().__new__(cls, Application.tag)

    def __init__(self, **kwargs: Unpack[_AppConfiguration]):
        super().__init__()
        if not Application.state()['ok']:
            Application.create_context()
            Application.prepare()
        if kwargs:
            self.configure(**kwargs)

    __slots__ = ()

    # addtl. 'global' states
    __app_info = Locker({
        'theme': None,
        'font' : None,
    })
    __app_state = Locker({
        'ok': False,
    })

    @tools.staticproperty
    @final
    def tag():
        """[get] Return the running process ID."""
        return os.getpid()

    @tools.staticproperty
    def process_id() -> int:
        """[get] Return the running process ID."""
        return os.getpid()

    @tools.staticproperty
    @final
    def verison() -> str:
        # There's a 'DPG version' hook through `get_app_configuration`
        # but it requires created context.
        """[get] Return Dear PyGui's version number."""
        return importlib.metadata.version('dearpygui')

    @final
    @staticmethod
    def create_context():
        """Manufacture the logical GPU context for the calling thread.

        A thread cannot create the GPU context more than once, even if the
        context has been destroyed prior. Once a thread calls this function,
        subsequent calls from that thread thread do nothing.

        NOTE: Must be called before using the Dear PyGui API. Any thread
        calling Dear PyGui without first creating the context is terminated
        without error.
        """
        _dearpygui.create_context()

    @staticmethod
    def destroy_context():
        """Destroy the logical GPU context of the calling thread.

        GPU context cannot be re-created by a thread whose context has
        been destroyed.

        NOTE: Once the GPU context has been destroyed, the thread can
        no longer use most of the Dear PyGui API.
        """
        _dearpygui.destroy_context()

    @final
    @staticmethod
    @_dearpygui_override(_dearpygui.setup_dearpygui)
    @__app_state
    def prepare(locker: Locker, /):
        """Prepares Dear PyGui for use.

        If manually setting up Dear PyGui, this function should be
        called following `create_context`.

        A thread cannot call this function more than once. Subsequent
        calls raise `RuntimeError`.

        Once called, `Application.state()["ok"] will be True.
        """
        with locker:
            if locker.value['ok']:
                raise RuntimeError("DearPyGui already set up.")
            _app_prepare()
            locker.value['ok'] = True

    @staticmethod
    def configure(**kwargs: Unpack[_AppConfiguration]):
        """Update the application's settings.

        This function does nothing once a frame has been rendered.
        """
        _dearpygui.configure_app(**kwargs)

    @staticmethod
    def configuration() -> _AppConfiguration:
        """Return the application's settings."""
        return _dearpygui.get_app_configuration()  # type: ignore

    @staticmethod
    @__app_info
    def information(locker: Locker, /) -> common.ItemInfoDict:
        """Return various application details."""
        info = dict(common.ITEM_INFO_TEMPLATE)
        with locker:
            states = locker.value

            if states['font'] and not Registry.item_exists(states['font']):
                states['font'] = None

            if states['theme'] and not Registry.item_exists(states['theme']):
                states['theme'] = None

            info.update(
                states,
                type='Application'
            )
            return info  # type: ignore

    @staticmethod
    @__app_state
    def state(locker: Locker, /) -> common.ItemStateDict:
        """Return the application's state.

        The value of the "ok" key will be True if Dear PyGui has been
        set up and is ready for use.
        """
        state = dict(common.ITEM_STATE_TEMPLATE)
        with locker:
            state.update(locker.value)
            return state  # type: ignore

    @staticmethod
    def get_font() -> ItemT | None:
        """Return the application-level font item."""
        return Application.information()['font']

    @staticmethod
    @_dearpygui_override(dearpygui.bind_font)
    @__app_info
    def set_font(locker: Locker, /, font: ItemT | None):
        """Set the application-level font item.

        Args:
            * font: Reference to a `mvFont` item.
        """
        with locker:
            _app_set_font(font)  # type: ignore
            locker.value['font'] = font

    @staticmethod
    def get_theme() -> ItemT | None:
        """Return the application-level theme item."""
        return Application.information()['theme']

    @staticmethod
    @_dearpygui_override(dearpygui.bind_theme)
    @__app_info
    def set_theme(locker: Locker, /, theme: ItemT | None):
        """Set the application-level theme.

        Args:
            * theme: Reference to a `mvTheme` item.
        """
        with locker:
            _app_set_theme(theme)  # type: ignore
            locker.value['theme'] = theme

    @staticmethod
    def get_clipboard_text():
        """Return the current text value of the clipboard."""
        return _dearpygui.get_clipboard_text()

    @staticmethod
    def set_clipboard_text(text: str):
        """Set a text value onto the clipboard.

        Args:
            * text: A string value to set.
        """
        _dearpygui.set_clipboard_text(text)

    @staticmethod
    def platform():
        """Return the Dear PyGui platform constant."""
        return constants.Platform(_dearpygui.get_platform())

    @staticmethod
    def save_init_file(file: str):
        """Dump identity, position, and docking information of root
        windows to a file.

        A window is excluded if its' `no_saved_settings` configuration
        option is set to True.
        """
        return _dearpygui.save_init_file(file)








from dearpygui._dearpygui import (
    show_viewport as _viewport_show,
    maximize_viewport as _viewport_maximize,
    minimize_viewport as _viewport_minimize,
    set_viewport_resize_callback as _viewport_set_resize_callback,
    set_primary_window as _viewport_set_primary_window,
    toggle_viewport_fullscreen as _viewport_toggle_fullscreen,
    create_viewport as _viewport_create,
    get_viewport_configuration as _viewport_configuration,
    configure_viewport as _viewport_configure,
)


class _ViewportConfiguration(TypedDict, total=False):
    title        : str
    small_icon   : str
    large_icon   : str
    width        : int
    height       : int
    x_pos        : int
    y_pos        : int
    min_width    : int
    max_width    : int
    min_height   : int
    max_height   : int
    resizable    : bool
    vsync        : bool
    always_on_top: bool
    decorated    : bool
    clear_color  : Color
    disable_close: bool
    # dpx addtl.
    primary_window: ItemT | None
    callback      : Callable | None
    user_data     : Any

class _ViewportState(common.ItemStateDict, total=False):
    fullscreen: bool


class _ViewportMeta(common.ItemInterfaceMeta):
    title         : Property[str]             = common.ItemConfig()
    small_icon    : Property[str]             = common.ItemConfig()
    large_icon    : Property[str]             = common.ItemConfig()
    width         : Property[int]             = common.ItemConfig()
    height        : Property[int]             = common.ItemConfig()
    x_pos         : Property[int]             = common.ItemConfig()
    y_pos         : Property[int]             = common.ItemConfig()
    min_width     : Property[int]             = common.ItemConfig()
    max_width     : Property[int]             = common.ItemConfig()
    min_height    : Property[int]             = common.ItemConfig()
    max_height    : Property[int]             = common.ItemConfig()
    resizable     : Property[bool]            = common.ItemConfig()
    vsync         : Property[bool]            = common.ItemConfig()
    always_on_top : Property[bool]            = common.ItemConfig()
    decorated     : Property[bool]            = common.ItemConfig()
    clear_color   : Property[Color]           = common.ItemConfig()
    disable_close : Property[bool]            = common.ItemConfig()
    primary_window: Property[ItemT | None]    = common.ItemConfig()
    callback      : Property[Callable | None] = common.ItemConfig()
    user_data     : Property[Any]             = common.ItemConfig()
    is_ok         : Property[bool | None]     = common.ItemState("ok")
    is_visible    : Property[bool | None]     = common.ItemState("visible")
    is_fullscreen : Property[bool | None]     = common.ItemState("is_fullscreen")


@_onetime_setup(lambda: Viewport(), ('create', 'state', 'close'))
@_clear_lockers
class Viewport(common.ItemInterface, str, metaclass=_ViewportMeta):
    """Thread-safe, multi-paradigm "viewport" API for Dear PyGui
    and Dear PyPixl.

    Using Dear PyGui's API over this API will not invalidate any
    settings or states, including those uniquely exposed through
    Dear PyPixl.
    """
    title: str     = cast(str, _ViewportMeta.title)
    small_icon     = cast(str, _ViewportMeta.small_icon)
    large_icon     = cast(str, _ViewportMeta.large_icon)
    width          = cast(int, _ViewportMeta.width)
    height         = cast(int, _ViewportMeta.height)
    x_pos          = cast(int, _ViewportMeta.x_pos)
    y_pos          = cast(int, _ViewportMeta.y_pos)
    min_width      = cast(int, _ViewportMeta.min_width)
    max_width      = cast(int, _ViewportMeta.max_width)
    min_height     = cast(int, _ViewportMeta.min_height)
    max_height     = cast(int, _ViewportMeta.max_height)
    resizable      = cast(bool, _ViewportMeta.resizable)
    vsync          = cast(bool, _ViewportMeta.vsync)
    always_on_top  = cast(bool, _ViewportMeta.always_on_top)
    decorated      = cast(bool, _ViewportMeta.decorated)
    clear_color    = cast(Color, _ViewportMeta.clear_color)
    disable_close  = cast(bool, _ViewportMeta.disable_close)
    primary_window = cast(ItemT | None, _ViewportMeta.primary_window)
    callback       = cast(Callable | None, _ViewportMeta.callback)
    user_data      = cast(Any, _ViewportMeta.user_data)

    is_ok          = cast(bool, _ViewportMeta.is_ok)
    is_visible     = cast(bool, _ViewportMeta.is_visible)
    is_fullscreen  = cast(bool, _ViewportMeta.is_fullscreen)

    def __new__(cls, **kwargs: Unpack[_AppConfiguration]) -> Self:
        return super().__new__(cls, Viewport.tag)

    def __init__(self, **kwargs: Unpack[_AppConfiguration]):
        super().__init__()
        if not Viewport.state()['ok']:
            Application()
            Viewport.create(**kwargs)
        elif kwargs:
            self.configure(**kwargs)


    __slots__ = ()

    __vp_config = Locker({
        'primary_window': None,
        'callback'      : None,
        'user_data'     : None,
    })
    __vp_state = Locker({
        'ok'        : False,
        'visible'   : False,
        'fullscreen': False,
    })

    tag: str = "DPG NOT USED YET"

    @final
    @staticmethod
    @_dearpygui_override(_dearpygui.create_viewport)
    @__vp_state
    def create(locker: Locker, /, **kwargs: Unpack[_ViewportConfiguration]) -> None:
        """Creates the Dear PyGui viewport.

        This will not display the viewport. To display it, call
        `Viewport.show`.

        If manually setting up Dear PyGui, this function should be called
        following `Application.prepare`.

        Only one Dear PyGui viewport can exist per process. Subsequent
        calls raise `RuntimeError`.

        `Viewport.state()["ok"]` will be True if the viewport has been
        created.

        Refer to `Viewport.configure` for argument details.
        """
        with locker:
            if locker.value['ok']:
                raise RuntimeError('viewport already exists.')

            if 'title' not in kwargs:
                kwargs['title'] = 'Application'
            kwds = dearpygui.create_viewport.__kwdefaults__ | kwargs
            _viewport_create(**kwds)
            locker.value['ok'] = True

    create.__func__.__func__.__kwdefaults__ = (
        dearpygui.create_viewport.__kwdefaults__ | (create.__func__.__func__.__kwdefaults__ or {})
    )

    @overload
    @staticmethod
    def show() -> None: ...
    @overload
    @staticmethod
    def show(*, minimized: bool = ...) -> None: ...
    @overload
    @staticmethod
    def show(*, maximized: bool = ...) -> None: ...
    @final
    @staticmethod
    @_dearpygui_override(_dearpygui.show_viewport)
    @__vp_state
    def show(locker: Locker, /, **kwargs) -> None:
        """Displays the viewport. Does nothing if the viewport is
        already visible.

        Args:
            * minimized: The viewport is shown minimized.

            * maximized: The viewport is shown maximized.


        The process cannot be reversed.
        """
        with locker:
            if not locker.value['visible']:
                _viewport_show(**kwargs)
                locker.value['visible'] = True

    @staticmethod
    def close():
        """Close the viewport and kill the runtime.

        Raises `RuntimeError` if the viewport is not created and visible.
        """
        vp_state = Viewport.state()
        if not vp_state['ok']:
            raise RuntimeError("viewport has not been created.")
        if not vp_state['visible']:
            raise RuntimeError("viewport is not visible.")
        _dearpygui.stop_dearpygui()

    @staticmethod
    @__vp_config
    def configure(locker: Locker, /, **kwargs: Unpack[_ViewportConfiguration]):
        """Update the viewport's settings.

        Args:
            * title: Text visible in the viewport's title bar.

            * small_icon: The icon visible in the top-left corner of the
            viewport's title bar.

            * large_icon: The icon visible on the operating system taskbar.

            * width: The viewport's horizontal size in non-fractional pixels.
            Note that this value is interpreted as unsigned by Dear PyGui's
            parser.

            * height: The viewport's vertical size in non-fractional pixels.
            Note that this value is interpreted as unsigned by Dear PyGui's
            parser.

            * x_pos: The horizontal position of the viewport's top-left corner
            as a non-fractional pixel value.

            * y_pos: The vertical position of the viewport's top-left corner
            as a non-fractional pixel value.

            * min_width: Lower-bound width clamp.

            * max_width: Upper-bound width clamp.

            * min_height: Lower-bound height clamp.

            * max_height: Upper-bound height clamp.

            * resizable: If True (default), the viewport is made resizable
            via user interaction. It can be programatically sized regardless
            of this value.

            * vsync: If True (default), the viewport's frame rate will be
            synchronized with the active display's refresh rate.

            * always_on_top: If True, the viewport appears above most other
            application windows.

            * decorated: If False, the viewport's border and title bar will
            not be rendered.

            * clear_color: A color value to paint the viewport's empty space.
            Does not work on Windows.

            * disable_close: If True, disables the functionality of the
            viewport's close button. The visual state of the button is not
            changed.

            * primary_window: Reference to a `mvWindowAppItem` item that will
            be used to fill the viewport. Can be unset by setting to None.

            * callback: A Dear PyGui-callable callback that will run whenever
            the viewport is resized via user interaction. Can be unset by
            setting to None.

            * user_data: Can be set as any value or reference, stored as-is.
            If *callback* is specified, Dear PyGui will send this as its' third
            positional argument (if able).


        Note that icon-related settings cannot be updated once the viewport
        is visible, although no error is thrown when attempting to do so.

        The coupling of *primary_window*, *callback* and *user_data* within
        the viewport's configuration is unique to Dear PyPixl, and cannot
        be updated using `dearpygui.configure_viewport`. Dear PyGui's
        `set_primary_window` and `set_viewport_resize_callback` functions
        can still be used to update these settings without dirtying
        Dear PyPixl's application state.
        """
        with locker:
            states = locker.value

            if 'primary_window' in kwargs:
                # BUG: process of setting the primary window makes the window forget its'
                # 'no_scrollbar' option, so it needs to be cached and re-applied when
                # the change is made.
                main_window = states['primary_window']
                primary_window = kwargs['primary_window']
                if primary_window:  # apply the new primary window
                    no_scrollbar = _dearpygui.get_item_configuration(primary_window)["no_scrollbar"]
                    _viewport_set_primary_window(primary_window, True)
                    states['primary_window'] = primary_window
                    _dearpygui.configure_item(primary_window, no_scrollbar=no_scrollbar)
                elif main_window:  # unset the primary window
                    no_scrollbar = _dearpygui.get_item_configuration(main_window)["no_scrollbar"]
                    _viewport_set_primary_window(main_window, False)
                    states['primary_window'] = None
                    _dearpygui.configure_item(main_window, no_scrollbar=no_scrollbar)

            if 'callback' in kwargs or 'user_data' in kwargs:
                callback  = kwargs.pop('callback', states['callback'])
                user_data = kwargs.pop('user_data', states['user_data'])
                _viewport_set_resize_callback(callback, user_data=user_data)  # type: ignore
                states.update(callback=callback, user_data=user_data)

            _viewport_configure(Viewport.tag, **kwargs)

    _dearpygui_override(_dearpygui.set_primary_window)(
        lambda window, value: Viewport.configure(primary_window=window if value else None)
    )

    _dearpygui_override(_dearpygui.set_viewport_resize_callback)(
        lambda callback, /, user_data=None: Viewport.configure(callback=callback, user_data=user_data)
    )


    @staticmethod
    @__vp_config
    def configuration(locker: Locker, /) -> _ViewportConfiguration:
        """Return the viewport's current settings.

        The coupling of *primary_window*, *callback* and *user_data*
        within the viewport's configuration is unique to Dear PyPixl,
        and will not be included in the return value of
        `dearpygui.get_viewport_configuration`.
        """
        cfg = _viewport_configuration(Viewport.tag)
        with locker:
            state_val = locker.value
            if state_val['primary_window'] and not Registry.item_exists(state_val['primary_window']):
                # state is dirty
                locker.value['primary_window'] = None
            cfg.update(state_val)
            return cfg  # type: ignore

    @staticmethod
    def information() -> common.ItemInfoDict:
        """Return various details regarding the viewport.

        The return value of this function does not contain anything
        useful at this time.
        """
        return dict(common.ITEM_INFO_TEMPLATE)  # type: ignore

    @staticmethod
    @__vp_state
    def state(locker: Locker, /) -> _ViewportState:
        """Return the viewport's state.

        The value of the "ok" key is True when the viewport has been
        created.

        The value of the "visible" key is True when the viewport is visible.

        The value of the "fullscreen" key is True while the viewport is
        being viewed in borderless fullscreen mode.
        """
        state = dict(common.ITEM_STATE_TEMPLATE)
        with locker:
            state.update(locker.value)
            return state  # type: ignore

    @staticmethod
    @_dearpygui_override(_dearpygui.toggle_viewport_fullscreen)
    @__vp_state
    def toggle_fullscreen(locker: Locker, /):
        """Swap between windowed and borderless fullscreen modes.

        `Viewport.state()["fullscreen"]` is True while the viewport is being
        viewed in borderles fullscreen mode.
        """
        with locker:
            _viewport_toggle_fullscreen()
            locker.value['fullscreen'] = not locker.value['fullscreen']

    @staticmethod
    @__vp_state
    def fullscreen(locker: Locker, /):
        """Set the viewport's viewing mode to borderless fullscreen."""
        with locker:
            if not locker.value['fullscreen']:
                _viewport_toggle_fullscreen()
                locker.value['fullscreen'] = True

    # XXX: No `is_maximized/minimized` hacks because using the title bar
    # buttons would dirty them.
    @staticmethod
    @_dearpygui_override(_dearpygui.maximize_viewport)
    @__vp_state
    def maximize(locker: Locker, /) -> None:
        """Maximize the viewport. The viewport will also exit borderless
        fullscreen.
        """
        with locker:
            if not locker.value['fullscreen']:
                _viewport_toggle_fullscreen()
                locker.value['fullscreen'] = False
            _viewport_maximize()

    @staticmethod
    @_dearpygui_override(_dearpygui.minimize_viewport)
    @__vp_state
    def minimize(locker: Locker, /) -> None:
        """Minimize the viewport. The viewport will also exit borderless
        fullscreen.
        """
        with locker:
            if not locker.value['fullscreen']:
                _viewport_toggle_fullscreen()
                locker.value['fullscreen'] = False
            _viewport_minimize()

    @staticmethod
    def active_window() -> ItemT | None:
        """Returns the identifier of the foreground root window item."""
        return _dearpygui.get_active_window()

    @staticmethod
    def mouse_pos_local():
        """Return the position of the mouse cursor relative to the
        active window item.
        """
        return _dearpygui.get_mouse_pos(local=True)

    @staticmethod
    def mouse_pos_global():
        """Return the position of the mouse cursor relative to the
        viewport.
        """
        return _dearpygui.get_mouse_pos(local=False)

    @staticmethod
    def mouse_drag_delta():
        """Return the distance the mouse cursor has traveled since
        the last update.
        """
        return _dearpygui.get_mouse_drag_delta()

    @staticmethod
    def mouse_plot_pos():
        """Return the position of the mouse cursor relative to the
        active `mvPlot` item.
        """
        return _dearpygui.get_plot_mouse_pos()

    @staticmethod
    def mouse_drawing_pos():
        """Return the position of the mouse cursor relative to the
        active `mvDrawlist` or  `mvViewportDrawlist` item."""
        return _dearpygui.get_drawing_mouse_pos()

    @staticmethod
    def output_frame_buffer(file: str = "", *, callback: Callable | None = None, **kwargs) -> None:
        """Take a screenshot of the viewport's content. Can only be called
        if at least one frame has been rendered. Unavailable on MacOS.

        Args:
            * file: A filename for the screenshot, saved in `.png` format.

            * callback: A Dear PyGui-callable callback. If specified, Dear
            PyGui will call it next frame; passing it a `mvBuffer` object
            as the callback's second positional argument. The buffer will
            contain the raw image data.
        """
        _dearpygui.output_frame_buffer(file, callback=callback)  # type:ignore







from dearpygui._dearpygui import (
    set_frame_callback as _runtime_set_frame_callback,
)


class _RuntimeConfiguration(TypedDict):
    frame_rate_limit: int
    clamp_frame_rate: bool
    update_interval : float


class _RuntimeMeta(common.ItemInterfaceMeta):
    frame_rate_limit: Property[int | None] = common.ItemConfig()
    clamp_frame_rate: Property[bool]       = common.ItemConfig()
    update_interval : Property[float]      = common.ItemConfig()


@_clear_lockers
class Runtime(common.ItemInterface, metaclass=_RuntimeMeta):
    frame_rate_limit = cast(int | None, _RuntimeMeta.frame_rate_limit)
    clamp_frame_rate = cast(bool, _RuntimeMeta.clamp_frame_rate)
    update_interval  = cast(float, _RuntimeMeta.update_interval)

    __slots__ = ()

    __rt_config = Locker({
        "update_interval" : 2.0,
        "render_interval" : 0.0,
        "frame_rate_limit": None,
        "clamp_frame_rate": False,
    })
    __rt_callbacks = Locker({})

    frame_callbacks: Mapping[int, Callable] = types.MappingProxyType(__rt_callbacks.value)

    @staticmethod
    @__rt_callbacks
    def get_frame_callback(locker: Locker, /, frame: int) -> Callable | None:
        """Return the callback scheduled to run on a specific frame,
        or None if no callback is scheduled.

        Args:
            * frame: Frame number to query.
        """
        with locker:
            return locker.value.get(frame, None)

    @staticmethod
    @_dearpygui_override(_dearpygui.set_frame_callback)
    @__rt_callbacks
    def set_frame_callback(locker: Locker, /,
        frame    : int,
        callback : Callable | None = _SENTINEL,  # type: ignore
        *,
        user_data: Any             = None
    ):
        """Schedule a callback to run on a specific frame. Can be used
        as a decorator.

        Args:
            * frame: The frame number in which *callback* will be scheduled.

            * callback: A Dear PyGui-callable callback, or None.

            * user_data: Send as the third positional argument to the
            callback (if able).
        """
        def capture_callback(callback: _T) -> _T:
            with locker:
                _runtime_set_frame_callback(frame, callback, user_data=user_data)  # type: ignore
                if not callback:
                    locker.value.pop(frame, None)
                else:
                    locker.value[frame] = callback
                return callback

        if callback is _SENTINEL:
            return capture_callback
        return capture_callback(callback)

    @staticmethod
    def callback_queue():
        """Return Dear PyGui's callback queue.

        Raises `SystemError` if the the `manual_callback_management`
        application setting is not True.
        """
        return _dearpygui.get_callback_queue()

    # XXX: `run_callbacks` is one of very few functions implemented in Dear
    # PyGui's public module. It's also *poorly* implemented -- un-typed, no
    # docstring, and the execution does not consider several factors.
    @staticmethod
    @_dearpygui_override(dearpygui.run_callbacks)
    def run_callback_queue(queue: Sequence[tuple[Callable | None, Any, Any, Any]]) -> None:
        """Process all callbacks in the given queue.

        Args:
            * queue: A sequence containing a callable to invoke and up to
            three positional arguments to pass to it. Argument(s) will
            not be passed to the callback if it cannot accept them.


        When the `manual_callback_management` application setting is
        True while building/starting the runtime event loop manually, this
        function should be called in the runtime event loop -- passing the
        return of `Runtime.callback_queue` or `dearpygui.get_callback_queue`
        as *queue*. This is automatically done when starting the runtime
        through `Runtime.start`.
        """
        if queue is None or not len(queue):  # custom queues may not be falsy when empty
            return
        for callback, *args in queue:
            try:
                parameters = tools.parameters(callback)
            except TypeError:
                # XXX: I'm not sure when this could be None as a result of
                # `get_callback_queue`, but the original implementation does
                # include a check.
                if callback is None:
                    continue
                raise
            # Dear PyGui (i.e. `get_callback_queue`) will always send its usual
            # three positional arguments, regardless if the function can accept
            # them. A user may have a different structure.
            args_count  = len(args)
            param_count = 0
            for p in parameters:
                if param_count >= args_count or p.kind in (
                    p.KEYWORD_ONLY,
                    p.VAR_KEYWORD,
                ):
                    break
                elif p.kind == p.VAR_POSITIONAL:
                    param_count = args_count
                    break
                param_count += 1
            callback(*args[:param_count])  # type:ignore

    @staticmethod
    def time_elapsed():
        """Return the number of seconds elapsed since the runtime was
        started.
        """
        return _dearpygui.get_total_time()

    @staticmethod
    def frame_count():
        """Return the number of frames rendered."""
        return _dearpygui.get_frame_count()

    @staticmethod
    def frame_rate():
        """Return the average frame rate over the last 120 frames."""
        return _dearpygui.get_frame_rate()

    @staticmethod
    def is_key_down(key: int):
        """Return True if a key is down, otherwise return False.

        Args:
            * key: Key event code to query.
        """
        return _dearpygui.is_key_down(key)

    @staticmethod
    def is_key_pressed(key: int):
        """Return True if a key is pressed, otherwise return False.

        Args:
            * key: Key event code to query.
        """
        return _dearpygui.is_key_pressed(key)

    @staticmethod
    def is_key_released(key: int):
        """Return True if a key is not down or pressed, otherwise
        return False.

        Args:
            * key: Key event code to query.
        """
        return _dearpygui.is_key_released(key)

    # Trying to avoid wrapping these; need to be as fast as
    # possible.
    # NOTE: The `staticmethod` wrappers won't stick around long. They
    #       don't have `__get__`, and therefore cannot be bound. Python
    #       knows this and will automatically unwrap them (this behavior
    #       is known but not publicly documented).
    render_frame = staticmethod(_dearpygui.render_dearpygui_frame)
    is_running   = final(staticmethod(_dearpygui.is_dearpygui_running))

    @staticmethod
    def prepare():
        """Complete any remaining setup necessary before starting
        the runtime.
        """
        Application.create_context()
        if not Application.state()['ok']:
            Application.prepare()
        vp_state = Viewport.state()
        if not vp_state['ok']:
            Viewport.create()
        if not vp_state['visible']:
            Viewport.show()

    queue: Queue[Callable] = Queue()

    @classmethod
    def start(cls, *args, **kwargs):
        """Start the runtime event loop and render the user interface.

        This function performs all of the required setup as necessary
        to start the runtime. For example, the minimum code required to
        start the runtime using Dear PyGui's API;
            >>> import dearpygui.dearpygui as dpg
            >>>
            >>> dpg.create_context()
            >>> dpg.setup_dearpygui()
            >>> dpg.create_viewport()
            >>> dpg.show_viewport()
            >>> while dpg.is_dearpygui_running():
            >>>     dpg.render_dearpygui_frame()
        Using Dear PyPixl's API;
            >>> from dearpypixl.api import Runtime
            >>>
            >>> Runtime.start()
        In addition, this function is prepared to handle Dear PyGui's
        event queue when the `manual_callback_management` application
        setting is True without any additional input from the user.
        """
        Runtime.prepare()

        rt_config    = Runtime.configure.__self__.value
        # XXX: no hot-swapping
        is_running   = Runtime.is_running
        render_frame = cls.render_frame
        queue        = cls.queue

        # `Queue.get` raises `Queue.Empty` when it's- well, empty. It
        # can be extremely punishing performance-wise when it's caught
        # repeatedly. Since a fixed-time step is used to control tasks,
        # this filler function can be looped without stalling the render.
        def recursive_task(_put_nowait=queue.put):
            # TODO: Maybe also do something useful here?
            _put_nowait(recursive_task)

        queue.put(recursive_task)

        def perf_counter(_counter=time.perf_counter):
            return 1000.0 * _counter()  # ms

        t_updates = 0
        ts_last_update = ts_last_render = perf_counter()

        render_frame()   # initialize item states

        if Application.configuration()['manual_callback_management']:
            get_queue = Runtime.callback_queue
            run_queue = cls.run_callback_queue

            while is_running():

                run_queue(get_queue())

                ts_this_update  = perf_counter()
                update_interval = rt_config['update_interval']
                t_updates += round(ts_this_update - ts_last_update, 3)
                ts_last_update = ts_this_update
                while t_updates >= update_interval:
                    queue.get_nowait()()
                    queue.task_done()
                    t_updates -= update_interval

                ts_this_render  = perf_counter()
                if ts_this_render - ts_last_render >= rt_config['render_interval']:
                    ts_last_render = ts_this_render
                    render_frame()

        else:
            while is_running():

                ts_this_update  = perf_counter()
                update_interval = rt_config['update_interval']
                t_updates += round(ts_this_update - ts_last_update, 3)
                ts_last_update = ts_this_update
                while t_updates >= update_interval:
                    queue.get_nowait()()
                    queue.task_done()
                    t_updates -= update_interval

                ts_this_render  = perf_counter()
                if ts_this_render - ts_last_render >= rt_config['render_interval']:
                    ts_last_render = ts_this_render
                    render_frame()

    @staticmethod
    def stop(*args, **kwargs):
        """Kill the runtime.

        Does not destroy the created GPU context.
        """
        if Runtime.is_running():
            _dearpygui.stop_dearpygui()

    @overload
    @staticmethod
    def configure(frame_rate_limit: int = ..., clamp_frame_rate: bool = ...): ...  # type: ignore
    @staticmethod
    @__rt_config  # type: ignore
    def configure(locker, **kwargs):  # type: ignore
        # This doesn't really need to be atomic. Worst-case is
        # it'll fix itself in a frame.
        config = locker.value

        config['update_interval'] = kwargs.get('update_interval', config['update_interval'])

        fr_limit = config['frame_rate_limit']
        if 'frame_rate_limit' in kwargs:
            fr_limit = kwargs['frame_rate_limit']
            if not fr_limit:
                fr_limit = None
            else:
                fr_limit = max(int(fr_limit), 0)
            config['frame_rate_limit'] = fr_limit
        fr_clamp = config['clamp_frame_rate']
        if 'clamp_frame_rate' in kwargs:
            fr_clamp = config['clamp_frame_rate'] = bool(kwargs['clamp_frame_rate'])
        if fr_limit and fr_clamp:
            config['render_interval'] = round(1000.0 / config['frame_rate_limit'], 1)

    @staticmethod
    @__rt_config
    def configuration(locker) -> _RuntimeConfiguration:
        config = locker.value.copy()
        del config['render_interval']
        return config









@_clear_lockers
class Registry:
    __slots__ = ()

    # declared here for `Application`s `theme` and `font` properties
    __itemtype_registry__: dict[str, type['AppItemType']] = {}

    @final
    @staticmethod
    @_dearpygui_override(_dearpygui.generate_uuid)
    def create_uuid():
        """Generate a unique integer id for an item."""
        return _create_uuid()

    @staticmethod
    def create_alias(pfx: Any):
        """Generate a unique alias using `uuid.uuid4`."""
        uuid = str(uuid4())
        if not pfx:
            return uuid
        return f"{pfx}-{uuid}"

    @staticmethod
    def capture_next_item(callback: Callable, *, user_data: Any = None):
        """Intercept the next would-be item. It is not created.

        Args:
            * callback: A Dear PyGui-callable callback.
        """
        _dearpygui.capture_next_item(callback, user_data=user_data)

    @staticmethod
    def last_item() -> ItemT:
        """Return the identifier of the last item created."""
        return _dearpygui.last_item()

    @staticmethod
    def last_root_item() -> ItemT:
        """Return the identifier of the last root item created."""
        return _dearpygui.last_root()

    @staticmethod
    def last_container_item() -> ItemT:
        """Return the identifier of the last container item created."""
        return _dearpygui.last_container()

    @staticmethod
    def top_stack_item() -> ItemT:
        """Return the identifier of the item atop the container stack."""
        return _dearpygui.top_container_stack()

    @staticmethod
    def push_stack(item: ItemT):
        """Push an item onto the container stack.

        Args:
            * item: Reference to an existing item.
        """
        return _dearpygui.push_container_stack(item)

    @staticmethod
    def pop_stack() -> ItemT:
        """Remove the item atop the container stack and return its'
        identifier.
        """
        try:
            return _dearpygui.pop_container_stack()
        except SystemError:
            raise SystemError("the container stack is empty.") from None

    @staticmethod
    @contextlib.contextmanager
    def push_container(container: ItemT):
        """Context manager function for pushing an existing item to
        the container stack, then popping it from the stack after
        executing the statement body.

        Args:
            * container: Reference to an existing container item.


        The item is removed from the container stack only if it is
        the top-most item after executing the statement body.
        """
        try:
            _dearpygui.push_container_stack(container)
            yield container
        finally:
            if _dearpygui.top_container_stack() == container:
                _dearpygui.pop_container_stack()

    @staticmethod
    def get_item_uuid(alias: str) -> int:
        """Return an item's uuid using its' alias.

        Args:
            * alias: A string name used as an item identifier.
        """
        return _dearpygui.get_alias_id(alias)  # type: ignore

    @staticmethod
    def get_item_alias(uuid: int) -> str:
        """Return an item's alias using its' uuid.

        Args:
            * item: Reference to an item.


        This function returns None if the referenced item doesn't
        exist or if the item does not have an assigned alias.
        """
        return _dearpygui.get_item_alias(uuid)

    @staticmethod
    def set_item_alias(uuid: int, alias: str):
        """Assign a string alias to an item, allowing it to
        be used as an identifier for that item.

        Args:
            * uuid: Target item's integer identifier.

            * alias: A string name to use as an item identifier.
        """
        if not alias:
            _alias = Registry.get_item_alias(uuid)
            if _alias:
                Registry.remove_alias(Registry.get_item_alias(uuid))
        elif not Registry.alias_exists(alias):
            Registry.add_alias(alias, uuid)
        else:
            _dearpygui.set_item_alias(uuid, alias)

    @staticmethod
    def add_alias(alias: str, uuid: int):
        """Register a string alias to a uuid and allow it to be
        used as an identifier/reference.

        Args:
            * alias: A string name.

            * uuid: Target item's integer identifier.


        If the `allow_alias_overwrites` application setting is False,
        `SystemError` will be raised if the alias is already in-use.
        """
        return _dearpygui.add_alias(alias, uuid)

    @staticmethod
    def remove_alias(alias: str):
        """Unregister a string alias.

        Raises `ValueError` if *alias* is not registered.

        Args:
            alias: A string name.
        """
        try:
            _dearpygui.remove_alias(alias)
        except SystemError:
            if not isinstance(alias, str):
                raise TypeError(
                    f"expected str for `alias`, got {type(alias).__qualname__!r}."
                ) from None
            raise ValueError(f"{alias!r} alias does not exist.") from None

    @staticmethod
    def delete_item(item: ItemT, *, children_only: bool = False, slot: Literal[-1, 0, 1, 2, 3] = -1) -> None:
        """Delete this item and/or this item's children.

        Args:
            * children_only: If True, only this item's children are
            destroyed, and only those in *slot*.

            * slot: When *children_only* is True, items in this child slot
            are deleted. If this value is -1 (default), items in all child
            slots are deleted.
        """
        _dearpygui.delete_item(item, children_only=children_only, slot=slot)

    @staticmethod
    def item_exists(item: ItemT):
        """Return True if a uuid or alias is bound to an existing item.

        Args:
            * item: Reference to an item.
        """
        return _dearpygui.does_item_exist(item)

    @staticmethod
    def alias_exists(alias: str):
        """Return True if a string is registered as an alias. It may or
        may not be in-use.

        Args:
            * alias: String value for query.
        """
        return _dearpygui.does_alias_exist(alias)

    @staticmethod
    def aliases() -> list[str]:
        """Return all string values assigned as aliases to uuid's. They
        may or may not be in-use.
        """
        return _dearpygui.get_aliases()  # type: ignore

    @staticmethod
    def items() -> list[ItemT]:
        """Return the identifiers of all existing items."""
        return _dearpygui.get_all_items()  # type: ignore

    @staticmethod
    def windows() -> list[ItemT]:
        """Return the identifiers of all window (`mvWindowAppItem`) items.
        """
        return _dearpygui.get_windows()  # type: ignore

    @staticmethod
    def root_items() -> list[ItemT]:
        """Return the identifiers of all top-level items."""
        return [
            item
            for item in _dearpygui.get_all_items()
            if _dearpygui.get_item_info(item)["parent"]
        ]

    @staticmethod
    def tree_view() -> _ItemTree:
        """Return the parential trees of all existing item branches.

        This function returns a dictionary where item identifier keys
        are mapped to their respective child slots. Each slot contains
        a recursive tree-view mapping per child item in that slot.
        Items in the returned top-level mapping are root items.

        This isn't a function you want to call in a performance-
        sensitive area, as it needs to process every existing item.
        """

        with dearpygui.mutex():
            treeview = {}
            for root_item in Registry.root_items():
                treeview.update(Item.item_tree(root_item))
        return treeview








# [ ITEM API ]

class Item:
    __slots__ = ()

    def get_alias(self: Any):
        """Return the string value assigned to the item's uuid."""
        return Registry.get_item_alias(self)

    def set_alias(self: Any, alias: str):
        """Assign a string value to the item's uuid, allowing it
        to be used as an identifier.
        """
        Registry.set_item_alias(self, alias)

    def configure(self: Any, /, **kwargs) -> None:  # type: ignore
        """Update the item's settings.

        Arguments vary depending the item's type.
        """
        try:
            _dearpygui.configure_item(self, **kwargs)
        except SystemError:
            if not Registry.item_exists(self):
                raise RuntimeError('item does not exist.') from None

            tp_def = parsing.item_definitions()[
                Item.information(self)['type'].removeprefix("mvAppItemType::")
            ]
            err = errors.err_arg_unexpected(self, tp_def.command1, **kwargs)
            if err:
                raise err from None
            raise

    def configuration(self: Any) -> MutableMapping:
        """Return the item's current settings."""
        return _dearpygui.get_item_configuration(self)

    def information(self: Any) -> common.ItemInfoDict:
        """Return various details regarding the item."""
        return _dearpygui.get_item_info(self)  # type: ignore

    def state(self: Any) -> common.ItemStateDict:
        """Return the item's conditional states."""
        return common.ITEM_STATE_TEMPLATE | _dearpygui.get_item_state(self)  # type: ignore

    def get_font(self) -> ItemT | None:
        """Return the font assigned to the item."""
        return Item.information(self)['font']

    def set_font(self: Any, font: ItemT | None):
        """Bind the item to a specific font.

        Text displayed for/within the item will use the font.
        The item's children will also use the font, unless a font
        is specifically set for them to use.

        Args:
            * font: Reference to a `mvFont` item.
        """
        _dearpygui.bind_item_font(self, font)  # type: ignore

    def get_theme(self) -> ItemT | None:
        """Return the theme assigned to the item."""
        return Item.information(self)['theme']

    def set_theme(self: Any, theme: ItemT | None):
        """Bind the item to a specific theme.

        The item (and children) will reflect the theme's elements.
        Elements of an item-bound theme are applied over elements
        propegated down from parenting item themes, or the
        application-level theme.

        Args:
            * theme: Reference to a `mvTheme` item.
        """
        return _dearpygui.bind_item_theme(self, theme)  # type: ignore

    def get_handlers(self: Any):
        """Return the item handler registry assigned to the item."""
        return Item.information(self)['handlers']

    def set_handlers(self: Any, handler_registry: ItemT | None):
        """Bind the item to a item handler registry.

        Args:
            * handler_registry: Reference to a `mvItemHandlerRegistry`
            item.
        """
        return _dearpygui.bind_item_handler_registry(self, handler_registry)  # type: ignore

    def get_value(self: Any):
        """Return the item's stored value.

        Not all item types can store a value. If the item cannot
        store a value, this function will always return None.
        """
        return _dearpygui.get_value(self)

    @staticmethod
    def get_values(items: Sequence[ItemT]) -> list[Any]:
        """Return the values of several children.

        Args:
            * items: A sequence of item references for the query.
        """
        return _dearpygui.get_values(items)  # type: ignore

    def set_value(self: Any, value: Any):
        """Update the item's value.

        Args:
            * value: Value to set. The value type varies depending on
            the item's type.


        Not all item types can store a value. However, no error is
        thrown while attempting to set the value of an item that
        cannot store it.
        """
        _dearpygui.set_value(self, value)

    @overload
    def children(self: Any) -> dict[Literal[0, 1, 2, 3], list[ItemT]]: ...
    @overload
    def children(self: Any, slot: Literal[0, 1, 2, 3]) -> list[ItemT]: ...
    def children(self: Any, slot: int = -1) -> dict[Literal[0, 1, 2, 3], list[ItemT]] | list[ItemT]:
        """Return all the item's child slots, or a specific slot.

        A child slot contains items parented by this item.

        Args:
            * slot: The target slot to return. A value of 0, 1, 2, or 3
            targets a specific slot, while -1 (default) is shorthand for
            "all slots".


        All items have a total of 4 child slots. Regardless of the parent,
        each slot stores specific type(s) of child items;
            - `0`: Contains `mvFileExtension`, `mvFontRangeHint`, `mvNodeLink`,
            `mvAnnotation`, `mvDragLine`, `mvDragPoint`, `mvLegend`, and
            `mvTableColumn` child item only.
            - `1`: Contains all child items not specifically included in other
            slots.
            - `2`: Contains all drawing-related child items.
            - `3`: Contains `mvDragPayload` child items only.

        The "slotting" of children is managed by Dear PyGui and cannot
        be controlled or changed by the user.
        """
        # if the item isn't a container everything will be empty
        children = _dearpygui.get_item_info(self)['children']
        if slot > -1:
            return children[slot]
        return children

    def delete(self: Any, *, children_only: bool = False, slot: Literal[-1, 0, 1, 2, 3] = -1) -> None:
        """Delete this item and/or this item's children.

        Args:
            * children_only: If True, only this item's children are
            destroyed, and only those in *slot*.

            * slot: When *children_only* is True, items in this child slot
            are deleted. If this value is -1 (default), items in all child
            slots are deleted.
        """
        _dearpygui.delete_item(self, children_only=children_only, slot=slot)

    def destroy(self: Any) -> None:
        """Delete the item and its' children, ignoring all errors.
        """
        try:
            Item.delete(self, children_only=False)
        except:
            pass

    def exists(self: Any) -> bool:
        """Return True if the item exists."""
        return _dearpygui.does_item_exist(self)

    def focus(self: Any):
        """Bring the item into the foreground and set it as the
        active item.
        """
        return _dearpygui.focus_item(self)

    def root_parent(self: Any) -> ItemT:
        """Return the item's top-level parent."""
        current_item = self
        while parent := _dearpygui.get_item_info(current_item)["parent"]:
            current_item = parent
        return current_item

    def item_branch(self: Any) -> list[ItemT]:
        """Return the item's direct ancestral hierarchy.

        This function returns a list of item identifiers. The last
        value in the list is always this item, and the first value
        is always item's top-level root parent. If this item is
        a top-level root item, it will be the only value in the
        list.
        """
        parents = [self]
        current_item = self
        while parent:=_dearpygui.get_item_info(current_item)["parent"]:
            parents.insert(0, parent)
            current_item = parent
        return parents

    def item_tree(self: Any, *, ancestors: bool = False, descendants: bool = True) -> _ItemTree:
        """Return the parential tree of the item's direct ancestors
        and/or descendants.

        Args:
            * ancestors: If True, the item's direct ancestors will be mapped
            along with this item. Their descendants are not mapped, except
            those required to map this item.

            * descendants: If True (default), the item's children will be
            recursively mapped.


        This function returns a dictionary of item identifier keys mapped
        to their child slots as a 4-tuple. Each value in the tuple contains
        recursive tree-view structures of every child item in that slot.

        The top-level dictionary returned by this function will only
        contain one "item-to-slots" pair. If *ancestors* is False, that
        item will be this one. Otherwise, it will be this item's root
        parent. If *descendants* is False, slots mapped to this item in the
        tree will be empty.
        """
        treeview = {self: ([], [], [], [])}
        children = treeview[self]
        if descendants:
            for i, slot in Item.information(self)['children'].items():
                children[i].extend(
                    Item.item_tree(c, descendants=descendants)
                    for c in slot
                )
        if ancestors:
            item, *parents = Item.item_branch(self)[::-1]
            for anscestor in parents:
                children = ([], [], [], [])
                children[Item.information(item)['target']].append(treeview)
                treeview = {anscestor: children}
        return treeview

    @staticmethod
    def text_size(text: str, *, wrap_width: int = -1, font: ItemT = 0) -> Array[float, float]:
        """Return the width and height of a string when rendered using a
        specific font.

        Args:
            * text: A string value for the query.

            * wrap_width: The number of pixels allowed before wrapping the text.
            If -1 (default), the text will not wrap regardless of the length.

            * font: Reference to a `mvFont` item for the query. If unspecified,
            the application-level font is used.
        """
        return _dearpygui.get_text_size(text, wrap_width=wrap_width, font=font)  # type: ignore


class BasicItem:
    __slots__ = ()

    def unstage(self: Any):
        """Remove this item from its' stage (`mvStage`) parent and
        add it to the item atop the container stack.

        The item must be parented by a stage (`mvStage`) item. The
        container stack cannot be empty.
        """
        return _dearpygui.unstage(self)

    def move(self: Any, *, parent: ItemT | None = 0, before: ItemT | None = 0):
        """Relocate the item.

        Args:
            * parent: Reference to a container item that will become
            the item's parent. If unspecified, the item's parent will
            not change.

            * before: Reference to an item parented by *parent* (or the
            item's current parent if *parent* is unspecified) that will
            proceed this item. If unspecified, the item will be added
            as the parenting item's newest child.


        The *before* keyword indicates where to move/add the item
        to amongst the other items in the child slot that will contain
        it. For example; to move a table row to be viewed as the first
        row in a table, *before* must be a reference to the first row
        item in the table's child slot 1.
        """
        return _dearpygui.move_item(self, parent=parent, before=before)  # type: ignore

    def move_index(self, index: SupportsIndex, *, parent: ItemT | None = 0):
        """Relocate the item.

        Args:
            * index: The new position of the item amongst other items
            in the child slot that will contain it.

            * parent: Reference to a container item that will become
            the item's parent. If unspecified, the item's parent will
            not change.

        Functionally similar to `Item.move`, except the item's new
        position in the parent's child slots is based on index, not
        another item. For example, in a scenario where a table row is
        created and you want it to be viewed as the first row in the
        table, `Item.move_index(table, row, 0)` is equivelent to
        `Item.move(row, before=Item.children(table, 1)[0])`.
        """
        item_info = Item.information(self)
        item_type = item_info['type']
        if item_type in (
            'mvAppItemType::mvFileExtension',
            'mvAppItemType::mvFontRangeHint',
            'mvAppItemType::mvNodeLink',
            'mvAppItemType::mvAnnotation',
            'mvAppItemType::mvDragLine',
            'mvAppItemType::mvDragPoint',
            'mvAppItemType::mvLegend',
            'mvAppItemType::mvTableColumn',
        ):
            slot = 0
        elif item_type == 'mvAppItemType::mvDragPayload':
            slot = 3
        elif item_type.startswith("mvAppItemType::mvDraw"):
            slot = 2
        else:
            slot = 1
        before = Item.children(parent or item_info['parent'], slot)[index]
        BasicItem.move(self, parent=parent, before=before)

    def move_up(self: Any):
        """Move the item up, or back one position in the child slot
        that contains it."""
        return _dearpygui.move_item_up(self)

    def move_down(self: Any):
        """Move the item down, or forward one position in the child
        slot that contains it.
        """
        return _dearpygui.move_item_down(self)


class Container:
    __slots__ = ()

    def reorder(self: Any, slot: Literal[0, 1, 2, 3], new_order: Sequence[ItemT]):
        """Re-arrange an item's children within in a specific slot.

        Args:
            * slot: The index of the target slot.

            * new_order: The contents of the target slot, arranged as
            desired.

        *new_order* must contain references to all of the children in
        the target slot of the item, so its' length must also match.

        An example of reversing the positions of rows in a table;
            >>> table = ...  # table reference
            >>>
            >>> rows = Item.children(table, 1)
            >>> rows.reverse()
            >>> Container.reorder(table, 1, rows)
        """
        return _dearpygui.reorder_items(self, slot, new_order)  # type: ignore

    def is_top_stack(self: Any) -> bool:
        """Return True if the item is atop the container stack."""
        return bool(Registry.top_stack_item() == self)

    def push_stack(self: Any):
        """Push the item onto the container stack."""
        return Registry.push_stack(self)

    def pop_stack(self: Any):
        """If the item is atop the container stack, pop it off the
        stack. Does nothing otherwise.
        """
        if Registry.top_stack_item() == self:
            Registry.pop_stack()


class NodeEditor:
    __slots__ = ()

    def selected_nodes(self: Any) -> list[ItemT]:
        """Return the editor's selected nodes."""
        return _dearpygui.get_selected_nodes(self)  # type:ignore

    def selected_links(self: Any) -> list[ItemT]:
        """Return the editor's selected links."""
        return _dearpygui.get_selected_links(self)  # type:ignore

    def clear_selected_nodes(self: Any) -> None:
        """Clear the editor's selected nodes."""
        _dearpygui.clear_selected_nodes(self)

    def clear_selected_links(self: Any) -> None:
        """Clear the editor's selected links."""
        _dearpygui.clear_selected_links(self)


class Table:
    __slots__ = ()

    def is_cell_highlighted(self: Any, irow: int, icol: int) -> bool:
        """Return True if a specific cell is highlighted.

        Args:
            * irow: The index of the cell's row.

            * icol: The index of the cell's column.
        """
        return _dearpygui.is_table_cell_highlighted(self, irow, icol)

    def is_col_highlighted(self: Any, icol: int) -> bool:
        """Return True if a specific column is highlighted.

        Args:
            * icol: The index of the column to query.
        """
        return _dearpygui.is_table_column_highlighted(self, icol)

    def is_row_highlighted(self: Any, irow: int) -> bool:
        """Return True if a specific row is highlighted.

        Args:
            * irow: The index of the row to query.
        """
        return _dearpygui.is_table_row_highlighted(self, irow)

    def set_cell_highlight(self: Any, irow: int, icol: int, color: Color | None):
        """Highlight or remove the highlight of a specific cell in
        the table.

        Args:
            * irow: The index of the cell's row.

            * icol: The index of the cell's column.

            * color: An RGB or RGBA color value sequence when
            highlighting, or None when clearing the highlight.
        """
        if color is None:
            _dearpygui.unhighlight_table_cell(self, irow, icol)
        else:
            _dearpygui.highlight_table_cell(self, irow, icol, color)  # type: ignore

    def set_col_highlight(self: Any, icol: int, color: Color | None):
        """Highlight or remove the highlight of a specific column in
        the table.

        Args:
            * icol: The index of the column.

            * color: An RGB or RGBA color value sequence when
            highlighting, or None when clearing the highlight.
        """
        if color is None:
            _dearpygui.unhighlight_table_column(self, icol)
        else:
            _dearpygui.highlight_table_column(self, icol, color)  # type: ignore

    def set_row_highlight(self: Any, irow: int, color: Color | None):
        """Highlight or remove the highlight of a specific row in
        the table.

        Args:
            * irow: The index of the row.

            * color: An RGB or RGBA color value sequence when
            highlighting, or None when clearing the highlight.
        """
        if color is None:
            _dearpygui.unhighlight_table_row(self, irow)
        else:
            _dearpygui.highlight_table_row(self, irow, color)  # type: ignore

    def set_row_color(self: Any, irow: int, color: Color | None):
        """Update the background color of a row in the table.

        Args:
            * irow: The index of the row.

            * color: An RGB or RGBA color value sequence when changing or
            setting a color, or None to use the default background color.
        """
        if color is None:
            _dearpygui.unset_table_row_color(self, irow)
        else:
            _dearpygui.set_table_row_color(self, irow, color)  # type: ignore

    if Application.verison < "1.9.2":
        def get_x_scroll_pos(self: Any):
            """Return the current horizontal view position of the item.

            This method will return 0.0 if the position is currently the
            default position, or -1.0 if the position is at the end of
            the scroll region. Otherwise, returns a value of 1.0 or greater.

            When the scroll position is 1.0 or greater, it means that the
            left-most edge of the current view area extends that many
            pixels away from the right-most edge of the default view area.

            This method is only available when using Dear PyGui version
            1.9.2.
            """
            return _dearpygui.get_x_scroll(self)

        def set_x_scroll_pos(self: Any, value: float):
            """Change the item's horizontal view position.

            Args:
                * value: Adjust the viewable area to this position.


            0.0 will set the position to the default view, or the "first
            page". -1.0 will set the view to the end of the scroll region,
            or the "last page".

            This method is only available when using Dear PyGui version
            1.9.2.
            """
            _dearpygui.set_x_scroll(self, value)

        def x_scroll_max(self: Any):
            """Return the number of pixels beyond the right-most edge of the
            default view area where the item's content ends.

            This method is only available when using Dear PyGui version
            1.9.2.
            """
            return _dearpygui.get_x_scroll_max(self)

        def get_y_scroll_pos(self: Any):
            """Return the current vertical scroll position of the item.

            This method will return 0.0 if the scroll position is currently
            the default position, or -1.0 if the position is at the end of
            the scroll region. Otherwise, returns a value of 1.0 or greater.

            When the scroll position is 1.0 or greater, it means that the
            upper-most edge of the current view area extends that many pixels
            away from the bottom-most edge of the default view area.

            This method is only available when using Dear PyGui version
            1.9.2.
            """
            return _dearpygui.get_y_scroll(self)

        def set_y_scroll_pos(self: Any, value: float):
            """Change the item's vertical view position.

            Args:
                * value: Adjust the viewable area to this position.


            0.0 will set the position to the default view, or the "first
            page". -1.0 will set the view to the end of the scroll region,
            or the "last page".

            This method is only available when using Dear PyGui version
            1.9.2.
            """
            _dearpygui.set_y_scroll(self, value)

        def y_scroll_max(self: Any):
            """Return the number of pixels beyond the bottom-most edge of
            the default view area where the item's content ends.

            This method is only available when using Dear PyGui version
            1.9.2.
            """
            return _dearpygui.get_y_scroll_max(self)
    else:
        get_x_scroll_pos = _not_implemented
        set_x_scroll_pos = _not_implemented
        x_scroll_max     = _not_implemented
        get_y_scroll_pos = _not_implemented
        set_y_scroll_pos = _not_implemented
        y_scroll_max     = _not_implemented


class Plot:
    __slots__ = ()

    def is_queried(self: Any):
        return _dearpygui.is_plot_queried(self)

    @staticmethod
    def auto_fit_data(axis: ItemT):
        """Set the viewing area of the plot to the boundries of
        an axis' visibly plotted data.

        Args:
            * axis: Reference to a `mvPlotAxis` item.
        """
        return _dearpygui.fit_axis_data(axis)

    @staticmethod
    def get_limits(axis: ItemT) -> Array[float, float]:
        """Return the lower and upper limits of the axis of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.
        """
        return _dearpygui.get_axis_limits(axis)  # type: ignore

    @staticmethod
    def set_limits(axis: ItemT, ymin: float, ymax: float):
        """Set the axis' lower and upper limits of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.

            * ymin: Lower-bound axis limit.

            * ymax: Upper-bound axis limit.
        """
        _dearpygui.set_axis_limits(axis, ymin, ymax)

    @staticmethod
    def reset_limits(axis: ItemT):
        """Clear explicitly set lower and upper limits of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.
        """
        _dearpygui.set_axis_limits_auto(axis)

    @staticmethod
    def set_ticks(axis: ItemT, label_pairs: Sequence[Array[str, int | str]]):
        """Update the axis' tick labels and values of an axis.

        Args:
            * axis: Reference to a `mvPlotAxis` item.

            * label_pairs: A sequence of pairs, where each pair contains
            the tick label to use and the value of that tick.
        """
        return _dearpygui.set_axis_ticks(axis, label_pairs)

    @staticmethod
    def reset_ticks(axis: ItemT):
        """Clear explicitly set tick labels and values of an axis."""
        return _dearpygui.reset_axis_ticks(axis)


class PlotAxis:
    __slots__ = ()

    def auto_fit_data(self: Any):
        """Set the viewing area of the plot to the boundries of
        the visible plotted data.
        """
        return _dearpygui.fit_axis_data(self)

    def get_limits(self: Any) -> Array[float, float]:
        """Return the lower and upper limits of the axis."""
        return _dearpygui.get_axis_limits(self)  # type: ignore

    def set_limits(self: Any, ymin: float, ymax: float):
        """Set the axis' lower and upper limits.

        Args:
            * ymin: Lower-bound axis limit.

            * ymax: Upper-bound axis limit.
        """
        _dearpygui.set_axis_limits(self, ymin, ymax)

    def reset_limits(self: Any):
        """Clear explicitly set lower and upper limits."""
        _dearpygui.set_axis_limits_auto(self)

    def set_ticks(self: Any, label_pairs: Sequence[Array[str, int | str]]):
        """Update the axis' tick labels and values.

        Args:
            * label_pairs: A sequence of pairs, where each pair contains
            the tick label to use and the value of that tick.
        """
        return _dearpygui.set_axis_ticks(self, label_pairs)

    def reset_ticks(self: Any):
        """Clear explicitly set tick labels and values."""
        return _dearpygui.reset_axis_ticks(self)



_Vec4 = Sequence[float] | mvBuffer | mvVec4

class Drawing:
    __slots__ = ()

    @staticmethod
    def apply_transform(draw_node: ItemT, transform: Sequence[float] | mvBuffer | mvVec4 | mvMat4) -> None:
        """Apply a transformation to a drawing node.

        Args:
            * draw_node: Reference to a `mvDrawNode` item.

            * transform: A flat 4x4 matrix that will be used in the
            transformation.

        *transform* will be used to multiply the points of the node's
        children. If a child is another node, the matricies will
        concatenate.
        """
        return _dearpygui.apply_transform(draw_node, transform)

    @staticmethod
    def set_clip_space(draw_layer: ItemT, top_left_x: float, top_left_y: float, width: float, height: float, min_depth: float, max_depth: float) -> None:
        """Set the point clipping area for a drawing layer.

        Only enabled when the layer's "depth_clipping" setting is
        True.

        Args:
            * item: Reference to a `mvDrawLayer` item.

            * top_left_x: Pixel position of the clip region's top-left corner.

            * top_left_y: Pixel position of the clip region's top-right corner.

            * width: The clip region's horizontal size in non-fractional
            pixels. Note that this value is interpreted as unsigned by Dear
            PyGui's parser.

            * height: The clip region's vertical size in non-fractional pixels.
            Note that this value is interpreted as unsigned by Dear PyGui's
            parser.

            * min_depth: Lower-bound depth clamp.

            * max_depth: Upper-bound depth clamp.
        """
        return _dearpygui.set_clip_space(draw_layer, top_left_x, top_left_y, width, height, min_depth, max_depth)

    @staticmethod
    def create_fps_matrix(eye: _Vec4, pitch: float, yaw: float) -> mvMat4:
        """Helper function for creating a "first person shooter" matrix.

        Args:
            * eye:

            * pitch:

            * yaw:
        """
        return _dearpygui.create_fps_matrix(eye, pitch, yaw)  # type: ignore

    @staticmethod
    def create_lookat_matrix(eye: _Vec4, target: _Vec4, up: _Vec4) -> mvMat4:
        return _dearpygui.create_lookat_matrix(eye, target, up)  # type: ignore

    @staticmethod
    def create_orthographic_matrix(left: float, right: float, bottom: float, top: float, zNear: float, zFar: float) -> mvMat4:
        """Helper function for creating a orthographic matrix.

        Args:
            * left: Position of the clipping plane's left-most edge.

            * right: Position of the clipping plane's right-most edge.

            * bottom: Position of the clipping plane's lower-most edge.

            * top: Position of the clipping plane's upper-most edge.

            * zNear: Value used to calculate the minimum corner of the
            clipping plane.

            * zFar: Value used to calculate the maxmimum corner of the
            clipping plane.
        """
        return _dearpygui.create_orthographic_matrix(left, right, bottom, top, zNear, zFar)

    @staticmethod
    def create_perspective_matrix(fov: float, aspect: float, zNear: float, zFar: float) -> mvMat4:
        """Helper function for creating a perspective matrix.

        Args:
            * fov: Field-of-view angle.

            * aspect: Aspect ratio value.

            * zNear: Nearest z-axis point in the perspective.

            * zFar: Farthest z-axis point in the perspective.
        """
        return _dearpygui.create_perspective_matrix(fov, aspect, zNear, zFar)

    @staticmethod
    def create_rotation_matrix(angle: float, axis: _Vec4) -> mvMat4:
        """Helper function for creating a rotation matrix from a given
        angle and four-dimensional vector.

        Args:
            angle: The angle of rotation.

            axis: A four-dimensional vector that will be used
            to create the matrix.
        """
        return _dearpygui.create_rotation_matrix(angle, axis)  # type: ignore

    @staticmethod
    def create_scale_matrix(scales: _Vec4) -> mvMat4:
        """Helper function for creating a scaling matrix from a
        four-dimensional vector.

        Args:
            scales: A four-dimensional vector that will be used
            to create the matrix.
        """
        return _dearpygui.create_scale_matrix(scales)  # type: ignore

    @staticmethod
    def create_translation_matrix(translation: _Vec4) -> mvMat4:
        """Helper function for creating a translation matrix from a four-
        dimensional vector.

        Args:
            translation: A four-dimensional vector that will be used
            to create the matrix.
        """
        return _dearpygui.create_translation_matrix(translation)  # type: ignore


class DrawLayer(Drawing):
    __slots__ = ()

    def set_clip_space(self: Any, top_left_x : float, top_left_y : float, width : float, height : float, min_depth : float, max_depth : float) -> None:
        """Set the point clipping area for the drawing layer.

        Only enabled when the layer's "depth_clipping" setting is
        True.

        Args:
            * top_left_x: Pixel position of the clip region's top-left corner.

            * top_left_y: Pixel position of the clip region's top-right corner.

            * width: The clip region's horizontal size in non-fractional
            pixels. Note that this value is interpreted as unsigned by Dear
            PyGui's parser.

            * height: The clip region's vertical size in non-fractional pixels.
            Note that this value is interpreted as unsigned by Dear PyGui's
            parser.

            * min_depth: Lower-bound depth clamp.

            * max_depth: Upper-bound depth clamp.
        """
        _dearpygui.set_clip_space(self, top_left_x, top_left_y, width, height, min_depth, max_depth)


class DrawNode(Drawing):
    __slots__ = ()

    def apply_transform(self: Any, transform: Sequence[float] | mvBuffer | mvVec4 | mvMat4) -> None:
        """Apply a transformation to the drawing node.

        Args:
            * transform: A flat 4x4 matrix that will be used in the
            transformation.

        *transform* will be used to multiply the points of the node's
        children. If a child is another node, the matricies will
        concatenate.
        """
        _dearpygui.apply_transform(self, transform)


class Window:
    __slots__ = ()

    def get_x_scroll_pos(self: Any):
        """Return the current horizontal view position of the item.

        This method will return 0.0 if the position is currently the
        default position, or -1.0 if the position is at the end of
        the scroll region. Otherwise, returns a value of 1.0 or greater.

        When the scroll position is 1.0 or greater, it means that the
        left-most edge of the current view area extends that many
        pixels away from the right-most edge of the default view area.
        """
        return _dearpygui.get_x_scroll(self)

    def set_x_scroll_pos(self: Any, value: float):
        """Change the item's horizontal view position.

        Args:
            * value: Adjust the viewable area to this position.


        0.0 will set the position to the default view, or the "first
        page". -1.0 will set the view to the end of the scroll region,
        or the "last page".
        """
        _dearpygui.set_x_scroll(self, value)

    def x_scroll_max(self: Any):
        """Return the number of pixels beyond the right-most edge of the
        default view area where the item's content ends."""
        return _dearpygui.get_x_scroll_max(self)

    def get_y_scroll_pos(self: Any):
        """Return the current vertical scroll position of the item.

        This method will return 0.0 if the scroll position is currently
        the default position, or -1.0 if the position is at the end of
        the scroll region. Otherwise, returns a value of 1.0 or greater.

        When the scroll position is 1.0 or greater, it means that the
        upper-most edge of the current view area extends that many pixels
        away from the bottom-most edge of the default view area.
        """
        return _dearpygui.get_y_scroll(self)

    def set_y_scroll_pos(self: Any, value: float):
        """Change the item's vertical view position.

        Args:
            * value: Adjust the viewable area to this position.


        0.0 will set the position to the default view, or the "first
        page". -1.0 will set the view to the end of the scroll region,
        or the "last page".
        """
        _dearpygui.set_y_scroll(self, value)

    def y_scroll_max(self: Any):
        """Return the number of pixels beyond the bottom-most edge of
        the default view area where the item's content ends.
        """
        return _dearpygui.get_y_scroll_max(self)



mvBuffer = cast(type[mvBuffer], dearpygui.mvBuffer)
mvVec4   = cast(type[mvVec4], dearpygui.mvVec4)
mvMat4   = cast(type[mvMat4], dearpygui.mvMat4)