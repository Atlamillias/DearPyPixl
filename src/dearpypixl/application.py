import typing
import threading

from dearpygui import dearpygui, _dearpygui

from dearpypixl.core import management
from dearpypixl.core import interface
from dearpypixl.core import codegen
from dearpypixl.core.protocols import property, Item
from dearpypixl.core.parsing import DEARPYGUI_VERSION

if typing.TYPE_CHECKING:
    from dearpypixl.items import mvTheme, mvFont


__all__ = ("Application",)




# [ managed global state ]

_GLOBAL_LOCK = threading.Lock()

_GLOBAL_INFO = {"font": None, "theme": None}

def _create_app_info_getter(key, item_type) -> typing.Any:
    def func(*, _key=key, _item_type=item_type) -> typing.Any:
        try:
            item = _GLOBAL_INFO[_key]
        except KeyError:
            return None

        if not item:
            return None

        if not _dearpygui.does_item_exist(item):
            _GLOBAL_INFO[_key] = None
            return

        if not isinstance(item, interface.Interface):
            return _item_type(tag=item)

        return item  # type: ignore

    del key, item_type
    return func

def _get_app_theme() -> typing.Any:  # type: ignore
    global _get_app_theme
    _get_app_theme = _create_app_info_getter(
        "theme", interface.Interface.__itemtype_registry__["mvAppItemType::mvTheme"]
    )
    return _get_app_theme()

def _set_app_theme(theme, /):
    _dearpygui.bind_theme(theme or 0)
    _GLOBAL_INFO["theme"] = theme or None

def _get_app_font() -> typing.Any:  # type: ignore
    global _get_app_font
    _get_app_font = _create_app_info_getter(
        "font", interface.Interface.__itemtype_registry__["mvAppItemType::mvFont"]
    )
    return _get_app_font()

def _set_app_font(font, /):
    _dearpygui.bind_font(font or 0)
    _GLOBAL_INFO["font"] = font or None


_GLOBAL_STATE = {"ok": False}

def _get_app_ok() -> typing.Any:
    return _GLOBAL_STATE["ok"]

def _set_app_ok(value = True, /):
    if value:
        # `setup_dearpygui()` segfaults if called more than once - raise an
        # error instead
        if _GLOBAL_STATE["ok"]:
            raise SystemError("dearpygui already set up")
        _dearpygui.create_context()
        _dearpygui.setup_dearpygui()
        management.unwrap_initializers()
    else:
        try:
            _dearpygui.destroy_context()
        except SystemError:
            pass
    _GLOBAL_STATE["ok"] = value




# [ API patches ]

@management.patched(dearpygui.setup_dearpygui)
def setup_dearpygui(**kwargs):
    with _GLOBAL_LOCK:
        _set_app_ok(True)

@management.patched(dearpygui.destroy_context)
def destroy_context(**kwargs):
    with _GLOBAL_LOCK:
        _set_app_ok(False)

@management.patched(dearpygui.bind_font)
def bind_font(font: int | str, **kwargs) -> int | str:
    with _GLOBAL_LOCK:
        _set_app_font(font)
    return font

@management.patched(dearpygui.bind_theme)
def bind_theme(theme: int | str, **kwargs) -> int | str:
    with _GLOBAL_LOCK:
        _set_app_font(theme)
    return theme




# [ Application ]

_PROPERTY_LOCALS = {
    "getter": _dearpygui.configure_app,
    "setter": _dearpygui.get_app_configuration
}

def _create_config_property(name):
    fget = codegen.create_function(
        name, ("self",), (f"return getter()['{name}']",),
        module=__name__, globals=globals(), locals=_PROPERTY_LOCALS,
    )
    fset = codegen.create_function(
        name, ("self", "value"), (f"setter({name}=value)",),
        module=__name__, globals=globals(), locals=_PROPERTY_LOCALS,
    )
    return property(fget, fset)

def _config_property() -> typing.Any:
    return codegen.DescriptorDelegate(_create_config_property)


class _AppConfigDict(typing.TypedDict, total=False):  # pyright: ignore[reportRedeclaration]
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

if DEARPYGUI_VERSION >= (2, 0):
    class _AppConfigDict(_AppConfigDict, total=False):
        docking_shift_only        : bool
        keyboard_navigation       : bool
        anti_aliasing             : bool
        anti_aliased_lines        : bool
        anti_aliased_lines_use_tex: bool
        anti_aliased_fill         : bool

class _AppStateDict(typing.TypedDict, total=True):
    ok: bool


class Application(interface.Interface):
    __slots__ = ()

    __itemtype_identity__ = (0, "Application")

    @property
    def tag(self) -> int | str:
        return 0

    @classmethod
    def create(cls, /, **configuration: typing.Unpack[_AppConfigDict]) -> typing.Self:
        with _GLOBAL_LOCK:
            _set_app_ok(True)

        self = cls()
        self.configure(**configuration)
        return self

    def destroy(self, /) -> None:
        with _GLOBAL_LOCK:
            _set_app_ok(False)

    @property
    def version(self) -> tuple[int, ...]:
        return DEARPYGUI_VERSION

    @property
    def platform(self) -> str:
        return _dearpygui.get_app_configuration()["platform"]

    @property
    def device_name(self) -> str:
        return _dearpygui.get_app_configuration()["device_name"]

    docking: property[bool, bool] = _config_property()
    docking_space: property[bool, bool] = _config_property()
    load_init_file: property[str, str] = _config_property()
    init_file: property[str, str] = _config_property()
    auto_save_init_file: property[bool, bool] = _config_property()
    device: property[int, int] = _config_property()
    auto_device: property[bool, bool] = _config_property()
    allow_alias_overwrites: property[bool, bool] = _config_property()
    manual_alias_management: property[bool, bool] = _config_property()
    skip_required_args: property[bool, bool] = _config_property()
    skip_positional_args: property[bool, bool] = _config_property()
    skip_keyword_args: property[bool, bool] = _config_property()
    wait_for_input: property[bool, bool] = _config_property()
    manual_callback_management: property[bool, bool] = _config_property()

    if DEARPYGUI_VERSION >= (2, 0):
        docking_shift_only: property[bool, bool] = _config_property()
        keyboard_navigation: property[bool, bool] = _config_property()
        anti_aliasing: property[bool, bool] = _config_property()
        anti_aliased_lines: property[bool, bool] = _config_property()
        anti_aliased_lines_use_tex: property[bool, bool] = _config_property()
        anti_aliased_fill: property[bool, bool] = _config_property()

    @typing.overload
    def configure(self, /, **kwargs: typing.Unpack[_AppConfigDict]) -> None: ...  # pyright:ignore [reportInconsistentOverload]
    def configure(
        self,
        /, *,
        # `Application(**application.configuration())`
        platform = None, version = None, major_version = None, minor_version = None, device_name = None,
        **kwargs
    ) -> None:
        _dearpygui.configure_app(**kwargs)

    def configuration(self) -> _AppConfigDict:
        return _dearpygui.get_app_configuration()  # type: ignore

    @property
    def theme(self) -> mvTheme | None:
        """[get, set, del] the application-level theme item."""
        return _get_app_theme()
    @theme.setter
    def theme(self, value: Item | None, /) -> None:
        with _GLOBAL_LOCK:
            _set_app_theme(value)
    @theme.deleter
    def theme(self) -> None:
        with _GLOBAL_LOCK:
            _set_app_theme(None)

    @property
    def font(self) -> mvFont | None:
        """[get, set, del] the application-level font item."""
        return _get_app_font()
    @font.setter
    def font(self, value: Item | None) -> None:
        with _GLOBAL_LOCK:
            _set_app_font(value)
    @font.deleter
    def font(self) -> None:
        with _GLOBAL_LOCK:
            _set_app_font(None)

    def information(self) -> interface.ItemInfoDict:
        info = interface.ITEM_INFO_TEMPLATE.copy()
        with _GLOBAL_LOCK:
            info["theme"] = _get_app_theme()
            info["font"]  = _get_app_font()
        return info

    def state(self, /) -> _AppStateDict:
        with _GLOBAL_LOCK:
            state = {"ok": _get_app_ok()}
        return state  # type: ignore

    @property
    def clipboard_text(self) -> str:
        """[get] Return the current text value of the clipboard."""
        return _dearpygui.get_clipboard_text()
    @clipboard_text.setter
    def clipboard_text(self, text: str, /) -> None:
        """[set] a text value onto the clipboard."""
        _dearpygui.set_clipboard_text(text)

    def save_init_file(self, file: str) -> None:
        """Dump identity, position, and docking information of root
        windows to a file.

        A window is excluded if its' `no_saved_settings` configuration
        option is set to True.
        """
        return _dearpygui.save_init_file(file)
