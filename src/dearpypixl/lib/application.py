import threading

from dearpypixl.core import management
from dearpypixl.core import interface
from dearpypixl.core import metautil
from dearpypixl.core.management import DEARPYGUI_VERSION

from dearpygui import dearpygui, _dearpygui


__all__ = (
    "Application", "application",
    "get_app_theme", "get_app_font", "is_app_ok", "get_app_info", "get_app_state",
)




# [ managed global state ]

_GLOBAL_LOCK = threading.Lock()

_GLOBAL_INFO = {"font": None, "theme": None}

def _create_app_info_getter(key, item_type):
    def func(*, _key=key, _item_type=item_type):
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

        return item  # pyright: ignore

    del key, item_type
    return func

def _get_app_theme():  # pyright: ignore
    global _get_app_theme
    _get_app_theme = _create_app_info_getter(
        "theme", interface.Interface.__item_registry__["mvAppItemType::mvTheme"]
    )
    return _get_app_theme()

def _set_app_theme(theme, /):
    _dearpygui.bind_theme(theme or 0)
    _GLOBAL_INFO["theme"] = theme or None

def _get_app_font():  # pyright: ignore
    global _get_app_font
    _get_app_font = _create_app_info_getter(
        "font", interface.Interface.__item_registry__["mvAppItemType::mvFont"]
    )
    return _get_app_font()

def _set_app_font(font, /):
    _dearpygui.bind_font(font or 0)
    _GLOBAL_INFO["font"] = font or None


_GLOBAL_STATE = {"ok": False}

def _get_app_ok():
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

@management.patch(dearpygui.setup_dearpygui)
def setup_dearpygui(**kwargs):
    with _GLOBAL_LOCK:
        _set_app_ok(True)

@management.patch(dearpygui.destroy_context)
def destroy_context(**kwargs):
    with _GLOBAL_LOCK:
        _set_app_ok(False)

@management.patch(dearpygui.bind_font)
def bind_font(font: int | str, **kwargs):
    with _GLOBAL_LOCK:
        _set_app_font(font)
    return font

@management.patch(dearpygui.bind_theme)
def bind_theme(theme: int | str, **kwargs):
    with _GLOBAL_LOCK:
        _set_app_font(theme)
    return theme




# [ DPX unique ]

def get_app_theme(obj=None, /):
    with _GLOBAL_LOCK:
        value = _get_app_theme()
    return value

def get_app_font(obj=None, /):
    with _GLOBAL_LOCK:
        value = _get_app_font()
    return value

def is_app_ok(obj=None, /):
    with _GLOBAL_LOCK:
        value = _get_app_ok()
    return value

_DEFAULT_APP_CHILDREN = type(int.__dict__)({0: (), 1: (), 2: (), 3: ()})

def get_app_info(obj=None, /):
    info = {
        "children": _DEFAULT_APP_CHILDREN,
        "type": '',
        "target": 1,
        "parent": None,
        "theme": None,
        "handlers": None,
        "font": None,
        "container": False,
        "hover_handler_applicable": False,
        "active_handler_applicable": False,
        "focus_handler_applicable": False,
        "clicked_handler_applicable": False,
        "visible_handler_applicable": False,
        "edited_handler_applicable": False,
        "activated_handler_applicable": False,
        "deactivated_handler_applicable": False,
        "deactivatedae_handler_applicable": False,
        "toggled_open_handler_applicable": False,
        "resized_handler_applicable": False,
    }
    with _GLOBAL_LOCK:
        info["theme"] = _get_app_theme()
        info["font"]  = _get_app_font()
    return info

def get_app_state(obj=None, /):
    with _GLOBAL_LOCK:
        state = {"ok": _get_app_ok()}
    return state  # type: ignore




# [ Application ]

_PROPERTY_LOCALS = {
    "getter": _dearpygui.configure_app,
    "setter": _dearpygui.get_app_configuration
}

@metautil.create_named_desc_factory
def _config_property(name):
    fget = metautil.create_function(
        name, ("self",), (
            f"try:",
            f"    return getter()['{name}']",
            f"except KeyError:",
            f"    raise AttributeError(f\"{name!r} not in dict returned from 'get_app_configuration()'\")"
        ),
        module=__name__, globals=globals(), locals=_PROPERTY_LOCALS,
    )
    fset = metautil.create_function(
        name, ("self", "value"), (f"setter({name}=value)",),
        module=__name__, globals=globals(), locals=_PROPERTY_LOCALS,
    )
    return property(fget, fset)


class Application(interface.Interface):
    __slots__ = ()

    @classmethod
    def create(cls, /, **configuration):
        with _GLOBAL_LOCK:
            _set_app_ok(True)

        self = cls()
        self.configure(**configuration)
        return self

    def destroy(self, /):
        with _GLOBAL_LOCK:
            _set_app_ok(False)

    exists = is_app_ok

    def configure(self, /, *, platform = None, version = None, major_version = None, minor_version = None, device_name = None, **kwargs):
        _dearpygui.configure_app(**kwargs)

    def configuration(self, /):
        return _dearpygui.get_app_configuration()  # type: ignore

    information = get_app_info
    state = get_app_state

    def save_init_file(self, file: str, /):
        return _dearpygui.save_init_file(file)

    @property
    def tag(self, /):  # pyrefly: ignore[bad-override]
        return 0

    @property
    def version(self, /):
        return DEARPYGUI_VERSION

    @property
    def platform(self, /):
        return _dearpygui.get_app_configuration()["platform"]

    @property
    def device_name(self, /):
        return _dearpygui.get_app_configuration()["device_name"]

    docking = _config_property()
    docking_space = _config_property()
    load_init_file = _config_property()
    init_file = _config_property()
    auto_save_init_file = _config_property()
    device = _config_property()
    auto_device = _config_property()
    allow_alias_overwrites = _config_property()
    manual_alias_management = _config_property()
    skip_required_args = _config_property()
    skip_positional_args = _config_property()
    skip_keyword_args = _config_property()
    wait_for_input = _config_property()
    manual_callback_management = _config_property()
    docking_shift_only = _config_property()
    keyboard_navigation = _config_property()
    anti_aliasing = _config_property()
    anti_aliased_lines = _config_property()
    anti_aliased_lines_use_tex = _config_property()
    anti_aliased_fill = _config_property()

    @property
    def theme(self, /):
        return _get_app_theme()
    @theme.setter
    def theme(self, value, /):
        with _GLOBAL_LOCK:
            _set_app_theme(value)
    @theme.deleter
    def theme(self, /):
        with _GLOBAL_LOCK:
            _set_app_theme(None)

    @property
    def font(self, /):
        return _get_app_font()
    @font.setter
    def font(self, value):
        with _GLOBAL_LOCK:
            _set_app_font(value)
    @font.deleter
    def font(self, /):
        with _GLOBAL_LOCK:
            _set_app_font(None)

    @property
    def clipboard_text(self, /):
        return _dearpygui.get_clipboard_text()
    @clipboard_text.setter
    def clipboard_text(self, text: str, /):
        _dearpygui.set_clipboard_text(text)


def application(*, __inst=Application(), **kwargs):
    # holding the lock for this check is pointless since we *can't*
    # hold it when calling `create()` as the lock is non-reentrant,
    # so just catch the potential error caused by a race condition
    if not _get_app_ok():
        try:
            __inst.create(**kwargs)
        except SystemError:
            assert _get_app_ok()

    return __inst
