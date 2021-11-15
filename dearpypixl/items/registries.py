import functools
from abc import ABCMeta, abstractmethod
from typing import Any, Callable, Union
from dearpypixl.constants import Key, Mouse
from dearpypixl.items.configuration import ItemAttribute, item_attribute
from dearpypixl.items.item import Item

from dearpypixl.items.handlers import *
from dearpygui import dearpygui
from dearpygui._dearpygui import (
    push_container_stack,
    pop_container_stack,
)


__all__ = [
    "AppEvents",
    "ItemEvents",
    
    # Unmodified
    "ValueRegistry",
    "TextureRegistry",
    "ColorMapRegistry",
    "TemplateRegistry",
    "FontRegistry",
]


def _manage_handler(handler: Item):
    def wrapped_method(_method):
        @functools.wraps(_method)
        def register_callback(self, callback: Callable = None, *args, **kwargs):
            @functools.wraps(callback)
            def set_handler(callback):
                handler(label=callback.__name__,  # lambdas have `<lambda>`
                        callback=callback, parent=int(self), *args, **kwargs)
                return callback

            if not callback:
                return set_handler
            return set_handler(callback)

        return register_callback

    return wrapped_method


class _RegistryItem(Item, metaclass=ABCMeta):
    @abstractmethod
    def _command() -> Callable:
        ...

    def __enter__(self):
        push_container_stack(self._tag)
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        pop_container_stack()


class AppEvents(_RegistryItem):
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                                                                                                                               
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                                                                                                                           
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")                                                                                                                  
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                                                                                                                                

    _is_container     : bool     = True                                                                                                                                                                                                              
    _is_root_item     : bool     = True                                                                                                                                                                                                              
    _is_value_able    : bool     = False                                                                                                                                                                                                             
    _unique_parents   : tuple    = ()                                                                                                                                                                                                                
    _unique_children  : tuple    = ('KeyDownHandler', 'KeyPressHandler', 'KeyReleaseHandler', 'MouseMoveHandler', 'MouseWheelHandler', 'MouseClickHandler', 'MouseDoubleClickHandler', 'MouseDownHandler', 'MouseReleaseHandler', 'MouseDragHandler')
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                
    _unique_constants : tuple    = ('mvHandlerRegistry',)                                                                                                                                                                                            
    _command          : Callable = dearpygui.add_handler_registry                                                                                                                                                                                    

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
    def while_key_down(self, callback: Callable = None, *, key: Union[Key, int] = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(KeyPressHandler)
    def on_key_press(self, callback: Callable = None, *, key: Union[Key, int] = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(KeyReleaseHandler)
    def on_key_up(self, callback: Callable = None, *, key: Union[Key, int] = Key.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDownHandler)
    def on_mouse_button_down(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseClickHandler)
    def on_mouse_button_click(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDoubleClickHandler)
    def on_mouse_button_double_click(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseReleaseHandler)
    def on_mouse_button_up(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseMoveHandler)
    def on_mouse_move(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseWheelHandler)
    def on_mouse_wheel_scroll(self, callback: Callable = None, *, user_data: Any = None, **kwargs):
        ...

    @_manage_handler(MouseDragHandler)
    def on_mouse_drag(self, callback: Callable = None, *, button: Union[Mouse, int] = Mouse.ANY, threshold: float = 10.0, user_data: Any = None, **kwargs):
        ...


class ItemEvents(_RegistryItem):
    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                                                                                                                                   
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                                                                                                                               
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")                                                                                                                      
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")                                                                                                                                    

    _is_container     : bool     = True                                                                                                                                                                                                                  
    _is_root_item     : bool     = True                                                                                                                                                                                                                  
    _is_value_able    : bool     = False                                                                                                                                                                                                                 
    _unique_parents   : tuple    = ()                                                                                                                                                                                                                    
    _unique_children  : tuple    = ('ActivatedHandler', 'ActiveHandler', 'ClickedHandler', 'DeactivatedAfterEditHandler', 'DeactivatedHandler', 'EditedHandler', 'FocusHandler', 'HoverHandler', 'ResizeHandler', 'ToggledOpenHandler', 'VisibleHandler')
    _unique_commands  : tuple    = ()                                                                                                                                                                                                                    
    _unique_constants : tuple    = ('mvItemHandlerRegistry',)                                                                                                                                                                                            
    _command          : Callable = dearpygui.add_item_handler_registry                                                                                                                                                                                   

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
    def targets(self) -> list[Item]:
        """Return a list of items that are bound to this item.
        """
        target_uuids = self.__target_uuids
        appitems = type(self)._appitems
        return [target_item for targets in target_uuids
                for target in targets if
                (target_item := appitems.get(target, None))]

    def bind(self, *item: Item):
        self_uuid = self._tag
        self_target_uuids = self.__target_uuids
        for i in item:
            dearpygui.bind_item_handler_registry(i._tag, self_uuid)
            self_target_uuids.add(i._tag)

    def unbind(self, *item: Item):
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


##############################################################
# NOTE: The following are unmodified from the script output. #
##############################################################
class ValueRegistry(_RegistryItem):
    """Adds a value registry.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")                                                                             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")                                                                         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")                                                                

    _is_container     : bool     = True                                                                                                                                                            
    _is_root_item     : bool     = True                                                                                                                                                            
    _is_value_able    : bool     = False                                                                                                                                                           
    _unique_parents   : tuple    = ()                                                                                                                                                              
    _unique_children  : tuple    = ('BoolValue', 'IntValue', 'Int4Value', 'FloatValue', 'Float4Value', 'StringValue', 'DoubleValue', 'Double4Value', 'ColorValue', 'FloatVectValue', 'SeriesValue')
    _unique_commands  : tuple    = ()                                                                                                                                                              
    _unique_constants : tuple    = ('mvValueRegistry',)                                                                                                                                            
    _command          : Callable = dearpygui.add_value_registry                                                                                                                                    

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )


class TextureRegistry(_RegistryItem):
    """Adds a dynamic texture.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ('StaticTexture', 'DynamicTexture', 'RawTexture')                                               
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvTextureRegistry',)                                                                          
    _command          : Callable = dearpygui.add_texture_registry                                                                  

    def __init__(
        self                            ,
        label             : str  = None ,
        user_data         : Any  = None ,
        use_internal_label: bool = True ,
        show              : bool = False,
        **kwargs                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class ColorMapRegistry(_RegistryItem):
    """Adds a colormap registry.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ('ColorMap',)                                                                                   
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvColorMapRegistry',)                                                                         
    _command          : Callable = dearpygui.add_colormap_registry                                                                 

    def __init__(
        self                            ,
        label             : str  = None ,
        user_data         : Any  = None ,
        use_internal_label: bool = True ,
        show              : bool = False,
        **kwargs                        ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            **kwargs,
        )


class TemplateRegistry(_RegistryItem):
    """Adds a template registry.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ()                                                                                              
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvTemplateRegistry',)                                                                         
    _command          : Callable = dearpygui.add_template_registry                                                                 

    def __init__(
        self                           ,
        label             : str  = None,
        user_data         : Any  = None,
        use_internal_label: bool = True,
        **kwargs                       ,
    ) -> None:
        super().__init__(
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            **kwargs,
        )


class FontRegistry(_RegistryItem):
    """Adds a font registry.
    
    	Args:
    		label (str, optional): Overrides 'name' as label.
    		user_data (Any, optional): User data for callbacks
    		use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
    		tag (Union[int, str], optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
    		show (bool, optional): Attempt to render widget.
    		id (Union[int, str], optional): (deprecated) 
    	Returns:
    		Union[int, str]
    """

    label             : str      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "label")             
    user_data         : Any      = ItemAttribute("configuration", "get_item_configuration", "configure_item", "user_data")         
    use_internal_label: bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "use_internal_label")
    show              : bool     = ItemAttribute("configuration", "get_item_configuration", "configure_item", "show")              

    _is_container     : bool     = True                                                                                            
    _is_root_item     : bool     = True                                                                                            
    _is_value_able    : bool     = False                                                                                           
    _unique_parents   : tuple    = ()                                                                                              
    _unique_children  : tuple    = ('Font',)                                                                                       
    _unique_commands  : tuple    = ()                                                                                              
    _unique_constants : tuple    = ('mvFontRegistry',)                                                                             
    _command          : Callable = dearpygui.add_font_registry                                                                     

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





