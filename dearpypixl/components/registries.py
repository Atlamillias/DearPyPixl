import functools
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Union

from dearpygui import dearpygui, _dearpygui

from dearpypixl.constants import Key, Mouse
from dearpypixl.components.configuration import ItemAttribute, item_attribute
from dearpypixl.components.item import Item, ItemT
from dearpypixl.components.handlers import *
from dearpypixl.components.items.registries import (
    ValueRegistry,
    TextureRegistry,
    ColorMapRegistry,
    TemplateRegistry,
    FontRegistry,       # Unused
)


__all__ = [
    "AppEvents",
    "ItemEvents",

    "ValueRegistry",
    "TextureRegistry",
    "ColorMapRegistry",
    "TemplateRegistry",
    "FontRegistry",
]


def _manage_handler(handler: Item):
    def wrapped_method(_method):
        @functools.wraps(_method)
        def register_callback(self, callback: Callable = None, **kwargs):
            @functools.wraps(callback)
            def set_handler(callback):
                handler(label=callback.__name__,  # lambdas have `<lambda>`
                        callback=callback,
                        parent=int(self),
                        **kwargs)
                return callback

            if not callback:
                return set_handler
            return set_handler(callback)

        return register_callback

    return wrapped_method


class AppEvents(Item):                                                                                                               
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config")                                                                                                                                

    __is_container__ : bool     = True                                                                                                                                                                                                              
    __is_root_item__ : bool     = True                                                                                                                                                                                                              
    __is_value_able__: bool     = False                                                                                                                                                                                                             
    __able_parents__ : tuple    = ()                                                                                                                                                                                                                
    __able_children__: tuple    = ('KeyDownHandler', 'KeyPressHandler', 'KeyReleaseHandler', 'MouseMoveHandler', 'MouseWheelHandler', 'MouseClickHandler', 'MouseDoubleClickHandler', 'MouseDownHandler', 'MouseReleaseHandler', 'MouseDragHandler')
    __commands__     : tuple    = ()                                                                                                                                                                                                                
    __constants__    : tuple    = ('mvHandlerRegistry',)                                                                                                                                                                                            
    __command__      : Callable = dearpygui.add_handler_registry                                                                                                                                                                                    

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        show              : bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )

    ################################
    ######## Callback Deco. ########
    ################################
    @_manage_handler(KeyDownHandler)
    def while_key_down(self, callback: Callable = None, *, key: Key | int = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(KeyPressHandler)
    def on_key_press(self, callback: Callable = None, *, key: Key | int = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(KeyReleaseHandler)
    def on_key_up(self, callback: Callable = None, *, key: Key | int = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDownHandler)
    def on_mouse_button_down(self, callback: Callable = None, *, button: Mouse | int = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseClickHandler)
    def on_mouse_button_click(self, callback: Callable = None, *, button: Mouse | int = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDoubleClickHandler)
    def on_mouse_button_double_click(self, callback: Callable = None, *, button: Mouse | int = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseReleaseHandler)
    def on_mouse_button_up(self, callback: Callable = None, *, button: Mouse | int = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseMoveHandler)
    def on_mouse_move(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseWheelHandler)
    def on_mouse_wheel_scroll(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDragHandler)
    def on_mouse_drag(self, callback: Callable = None, *, button: Mouse | int = Mouse.ANY, threshold: float = 10.0, user_data: Any = None, **kwargs):
        ...


class ItemEvents(Item):                                                                                                                    
    show             : bool     = ItemAttribute("configuration", "get_item_config", "set_item_config")                                                                                                                                    

    __is_container__ : bool     = True                                                                                                                                                                                                                  
    __is_root_item__ : bool     = True                                                                                                                                                                                                                  
    __is_value_able__: bool     = False                                                                                                                                                                                                                 
    __able_parents__ : tuple    = ()                                                                                                                                                                                                                    
    __able_children__: tuple    = ('ActivatedHandler', 'ActiveHandler', 'ClickedHandler', 'DeactivatedAfterEditHandler', 'DeactivatedHandler', 'EditedHandler', 'FocusHandler', 'HoverHandler', 'ResizeHandler', 'ToggledOpenHandler', 'VisibleHandler')
    __commands__     : tuple    = ()                                                                                                                                                                                                                    
    __constants__    : tuple    = ('mvItemHandlerRegistry',)                                                                                                                                                                                            
    __command__      : Callable = dearpygui.add_item_handler_registry                                                                                                                                                                                   

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        show              : bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )
        self.__target_uuids: set[int] = set()

    @property
    @item_attribute(category="information")
    def targets(self) -> list[ItemT]:
        """Return a list of items that are bound to this item.
        """
        target_uuids = self.__target_uuids
        appitems = type(self)._AppItemsRegistry
        return [target_item for targets in target_uuids
                for target in targets if
                (target_item := appitems.get(target, None))]

    def bind(self, *item: ItemT):
        self_uuid = self._tag
        self_target_uuids = self.__target_uuids
        for i in item:
            dearpygui.bind_item_handler_registry(i._tag, self_uuid)
            self_target_uuids.add(i._tag)

    def unbind(self, *item: ItemT):
        self_target_uuids = self.__target_uuids
        for i in item:
            if i._tag not in self_target_uuids:
                raise ValueError(f"Cannot unbind {item.__qualname__!r} as it is not bound to this item.")
            dearpygui.bind_item_handler_registry(i._tag, 0)

    ################################
    ######## Callback Deco. ########
    ################################
    @_manage_handler(ActiveHandler)
    def while_active(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ActivatedHandler)
    def on_activation(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(DeactivatedHandler)
    def on_deactivation(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(DeactivatedAfterEditHandler)
    def on_deactivation_after_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ClickedHandler)
    def on_click(self, callback: Callable = None, *, user_data: Any = None, button=-1, **kwargs) -> Callable:
        ...

    @_manage_handler(EditedHandler)
    def on_edit(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(FocusHandler)
    def on_focus(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(HoverHandler)
    def on_hover(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ResizeHandler)
    def on_resize(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(ToggledOpenHandler)
    def on_toggle_open(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...

    @_manage_handler(VisibleHandler)
    def on_visible(self, callback: Callable = None, *, user_data: Any = None, **kwargs) -> Callable:
        ...
