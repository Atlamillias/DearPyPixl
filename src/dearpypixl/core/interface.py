import typing
import types

from . import protocols


__all__ = (
    "ItemInfoDict",
    "ItemStateDict",
    "Interface",
)




# [ mapping templates ]

class ItemInfoDict(typing.TypedDict):
    children: typing.Mapping[typing.Literal[0, 1, 2, 3], list[protocols.Item]]
    type: str
    target: int
    parent: protocols.Item | None
    theme: protocols.Item | None
    handlers: protocols.Item | None
    font: protocols.Item | None
    container: bool
    hover_handler_applicable: bool
    active_handler_applicable: bool
    focus_handler_applicable: bool
    clicked_handler_applicable: bool
    visible_handler_applicable: bool
    edited_handler_applicable: bool
    activated_handler_applicable: bool
    deactivated_handler_applicable: bool
    deactivatedae_handler_applicable: bool
    toggled_open_handler_applicable: bool
    resized_handler_applicable: bool

ITEM_INFO_TEMPLATE: ItemInfoDict = types.MappingProxyType(  # type:ignore
    ItemInfoDict(
        children=types.MappingProxyType(dict.fromkeys(range(4), ())),  # type:ignore
        type="",
        target=1,
        parent=None,
        theme=None,
        handlers=None,
        font=None,
        container=False,
        hover_handler_applicable=False,
        active_handler_applicable=False,
        focus_handler_applicable=False,
        clicked_handler_applicable=False,
        visible_handler_applicable=False,
        edited_handler_applicable=False,
        activated_handler_applicable=False,
        deactivated_handler_applicable=False,
        deactivatedae_handler_applicable=False,
        toggled_open_handler_applicable=False,
        resized_handler_applicable=False,
    )
)


class ItemStateDict(typing.TypedDict):
    ok: bool
    pos: typing.Annotated[list[int], 2]
    active: typing.NotRequired[bool]
    clicked: typing.NotRequired[bool]
    left_clicked: typing.NotRequired[bool]
    right_clicked: typing.NotRequired[bool]
    middle_clicked: typing.NotRequired[bool]
    edited: typing.NotRequired[bool]
    activated: typing.NotRequired[bool]
    deactivated: typing.NotRequired[bool]
    deactivated_after_edit: typing.NotRequired[bool]
    hovered: typing.NotRequired[bool]
    focused: typing.NotRequired[bool]
    visible: typing.NotRequired[bool]
    resized: typing.NotRequired[typing.Annotated[list[int], 2]]
    rect_min: typing.NotRequired[typing.Annotated[list[int], 2]]
    rect_max: typing.NotRequired[typing.Annotated[list[int], 2]]
    rect_size: typing.NotRequired[typing.Annotated[list[int], 2]]
    content_region_avail: typing.NotRequired[typing.Annotated[list[int], 2]]




# [ item interface type ]

# XXX: should be a protocol/abc, but it's not to make it easier
# to write metaclasses
class Interface:
    __slots__ = ()

    # registry is defined here so it's available to `Application` &
    # `Viewport` without fuss
    __itemtype_registry__: typing.ClassVar[dict[str, typing.Any]] = {}

    def __repr__(self, /) -> str:
        return f"{self.__class__.__name__}(tag={self.tag!r})"

    def information(self, /) -> ItemInfoDict | typing.Mapping[str, typing.Any]:
        info = ITEM_INFO_TEMPLATE.copy()
        info['type'] = self.__class__.__name__
        return info

    @classmethod
    def create(cls, /) -> typing.Self:
        raise NotImplementedError

    def destroy(self, /) -> None:
        raise NotImplementedError

    tag: protocols.Descriptor[int | str]

    def configure(self, /, **kwargs) -> None:
        raise NotImplementedError

    def configuration(self, /) -> typing.Mapping[str, typing.Any]:
        raise NotImplementedError

    def state(self, /) -> typing.Mapping[str, typing.Any]:
        raise NotImplementedError
