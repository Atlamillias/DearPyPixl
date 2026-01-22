def _init_module():
    from typing import overload, Sequence, Any

    from dearpypixl.core import parsing
    from dearpypixl.items import mvTheme, mvThemeComponent, mvThemeColor, mvThemeStyle


    namespace = {
        "mvTheme": mvTheme,
        "mvThemeComponent": mvThemeComponent,
        "mvThemeColor": mvThemeColor,
        "mvThemeStyle": mvThemeStyle,
    }

    def _overload1[T = Any](
        value: tuple[int, int] | Sequence[int],
        /, *,
        label: str | None = None,
        user_data: T = None,
        use_internal_label: bool = True,
        tag: int | str = 0,
        parent: int | str = 0,
    ) -> mvThemeStyle[T]: ...

    def _overload2[T = Any](
        x: float = 1.0, y: float = -1.0,
        /, *,
        label: str | None = None,
        user_data: T = None,
        use_internal_label: bool = True,
        tag: int | str = 0,
        parent: int | str = 0,
    ) -> mvThemeStyle[T]: ...

    ELEM_INFO = parsing.theme_style_info().values()
    ITEM_TYPE = mvThemeStyle
    ITEM_FUNC = ITEM_TYPE.__itemtype_command__

    for info in ELEM_INFO:

        def func(
            x = 1,
            y = -1,
            /, *,
            label = None,
            use_internal_label = True,
            user_data = None,
            tag = 0,
            parent = 0,
            __type=ITEM_TYPE,
            __func=ITEM_FUNC,
            __category=info.category,
            __target=info.target,
        ):
            if hasattr(x, "__iter__"):
                x, y = x  # type: ignore

            return __type(
                tag=__func(
                    __target, x, y,
                    label=label,
                    use_internal_label=use_internal_label,
                    user_data=user_data,
                    category=__category,
                    tag=tag,
                    parent=parent,
                ),
            )

        name = info.func_name
        _overload1.__name__ = _overload2.__name__ = func.__name__ = \
        _overload1.__qualname__ = _overload2.__qualname__ = func.__qualname__ = name

        overload(_overload1)
        overload(_overload2)

        namespace[name] = func

    namespace["__all__"] = tuple(namespace)

    globals().update(namespace)
    del globals()["_init_module"]

_init_module()
