import typing

if typing.TYPE_CHECKING:
    from dearpypixl.core.appitem import _ItemInfoDict
    from dearpypixl.core.protocols import Descriptor


__all__ = ("Interface",)




# XXX: should be a protocol/abc, but it's not to make it easier
# to write metaclasses
class Interface:
    """Defines the DearPyPixl "interface" protocol. Within the
    context of DearPyPixl, a typical interface is an object that
    operates on a DearPyGui item or system. Some homebrew systems
    derive from this class to maintain a consistent API.

    Subclasses must implement the :py:meth:~`Interface.create()`
    class method, the :py:var:~Interface.tag` property, and the
    :py:meth:~`Interface.destroy()` and :py:meth:~`Interface.configure()`
    instance methods.
    """
    __slots__ = ()

    tag: Descriptor[int | str]

    @classmethod
    def create(cls, /) -> typing.Self:
        raise NotImplementedError

    def destroy(self, /) -> None:
        raise NotImplementedError

    def configure(self, /, **kwargs) -> None:
        raise NotImplementedError

    def configuration(self, /) -> typing.Any:
        return {}

    def state(self, /) -> typing.Any:
        return {}

    # registry is defined here so it's available to `Application` &
    # `Viewport` without fuss
    __item_registry__: typing.ClassVar[dict[typing.Any, typing.Any]] = {}

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}(tag={self.tag!r})"

    def information(self, /) -> _ItemInfoDict:
        return {
            "children": {0: [], 1: [], 2: [], 3: []},
            "type": self.__class__.__name__,
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
