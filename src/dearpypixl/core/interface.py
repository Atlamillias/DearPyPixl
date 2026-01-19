import typing
import types

from . import protocols

if typing.TYPE_CHECKING:
    from .appitem import AppItem


__all__ = (
    "ItemInfoDict", "ITEM_INFO_TEMPLATE",
    "ItemStateDict", "ITEM_STATE_TEMPLATE",
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
    hovered: bool | None
    active: bool | None
    focused: bool | None
    clicked: bool | None
    left_clicked: bool | None
    right_clicked: bool | None
    middle_clicked: bool | None
    visible: bool | None
    edited: bool | None
    activated: bool | None
    deactivated: bool | None

ITEM_STATE_TEMPLATE: ItemStateDict = types.MappingProxyType(  # type: ignore
    ItemStateDict(
        ok=True,
        hovered=None,
        active=None,
        focused=None,
        clicked=None,
        left_clicked=None,
        right_clicked=None,
        middle_clicked=None,
        visible=None,
        edited=None,
        activated=None,
        deactivated=None,
    )
)




# [ item interface type ]


# XXX: should be a protocol/abc, but it's not to make it easier
# to write metaclasses
class Interface:
    __slots__ = ()

    # registry is defined here so it's available to `Application` &
    # `Viewport` without fuss
    __itemtype_registry__: typing.ClassVar[dict[str, typing.Any]] = {}

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(tag={self.tag!r})"

    def information(self, /) -> ItemInfoDict | typing.Mapping[str, typing.Any]:
        info = ITEM_INFO_TEMPLATE.copy()
        info['type'] = self.__class__.__name__
        return info

    def state(self, /) -> ItemStateDict | typing.Mapping[str, typing.Any]:
        return ITEM_STATE_TEMPLATE.copy()

    tag: protocols.Descriptor[int | str]

    def configure(self, /, **kwargs) -> None:
        raise NotImplementedError

    def configuration(self) -> typing.Mapping[str, typing.Any]:
        raise NotImplementedError

    @classmethod
    def create(cls) -> typing.Self:
        raise NotImplementedError

    def destroy(self, /) -> None:
        raise NotImplementedError
