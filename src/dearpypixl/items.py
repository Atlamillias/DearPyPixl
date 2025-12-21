



def _build_itemtype_factory():
    import inspect

    from . import _parsing
    from ._interface import (  # can't wildcard import in optimized scopes
        AppItemMeta, RegistryType, RootType, ContainerType, BasicType,
        TableItemType, TableType, HandlerType, WindowType, DrawingType,
        DrawNodeType, FontType, PlotType, PlotAxisType, PlottingType,
        NodeEditorType, NodeType, ThemeElementType, ThemeType,
        SupportsCallback, SupportsSized, SupportsValueArray, AppItemType
    )


    def create_itemtype(tp_def: _parsing.ItemDefinition) -> type[AppItemType]:
        tp_name: str = tp_def.name # type: ignore
        reg_key = f'mvAppItemType::{tp_name}'

        # cached?
        if reg_key in AppItemMeta.__itemtype_registry__:
            cls = AppItemMeta.__itemtype_registry__[reg_key]

        else:
            params = inspect.signature(tp_def.command1).parameters

            ll_bases = []
            if "parent" not in params:
                if any(
                    tp_def.command1.__name__.endswith(n) for n in ('_registry', 'theme')
                ):
                    ll_bases.append(RegistryType)
                else:
                    ll_bases.append(RootType)
            elif tp_def.is_container:
                ll_bases.append(ContainerType)
                ll_bases.append(BasicType)
            else:
                ll_bases.append(BasicType)

            hl_bases = []
            if tp_name == 'mvTable':
                hl_bases.append(TableItemType)
            elif tp_name.startswith("mvTable"):
                hl_bases.append(TableType)
            elif "Handler" in tp_name and not RegistryType in ll_bases:
                hl_bases.append(HandlerType)
            elif "Window" in tp_name:
                assert any(b in ll_bases for b in (ContainerType, RootType))
                hl_bases.append(WindowType)
            elif tp_name == 'mvDrawNode':
                hl_bases.append(DrawNodeType)
            elif tp_name.startswith('mvDraw') or "Drawlist" in tp_name:
                hl_bases.append(DrawingType)
            elif tp_name == 'mvFont':
                hl_bases.append(FontType)
            elif tp_name == "mvPlot":
                assert tp_def.is_container
                hl_bases.append(PlotType)
            elif tp_name == 'mvPlotAxis':
                hl_bases.append(PlotAxisType)
            elif any(n in tp_name for n in ("Plot", "Series", "mvAnnotation", "mvLegend")):
                hl_bases.append(PlottingType)
            elif tp_name == 'mvNodeEditor':
                hl_bases.append(NodeEditorType)
            elif tp_name.startswith("mvNode"):
                hl_bases.append(NodeType)
            elif tp_name == "mvTheme":
                hl_bases.append(ThemeType)
            elif tp_name.startswith("mvTheme"):
                hl_bases.append(ThemeElementType)

            fn_bases = []
            if any(
                s in tp_def.command1.__name__
                for s in ("_series", "theme_color", "theme_style")
            ):
                fn_bases.append(SupportsValueArray)
            if all(p in params for p in ("pos", "width", "height")):
                fn_bases.append(SupportsSized)
            if "callback" in params:
                fn_bases.append(SupportsCallback)

            bases = [*fn_bases, *hl_bases, *ll_bases]
            assert bases

            class_body = {
                '__doc__'  : _parsing.upd_command_doc(tp_def.command1),
                '__slots__': (),
            }

            cls = type(
                tp_name,
                tuple(bases),
                class_body,
                command=tp_def.command1,
                identity=(tp_def.enum, f"mvAppItemType::{tp_name}")
            )

        return cls  # type: ignore

    return create_itemtype

_create_itemtype = _build_itemtype_factory()


def _fill_namespace():
    from . import _interface, _parsing, _mkstub

    exported = _mkstub.Exported(__name__)

    namespace = dict(
        exp for exp in _mkstub.Exported.fetch(_interface).items()
    )
    for tp_def in _parsing.item_definitions().values():
        if not tp_def:
            continue

        itp = exported(_create_itemtype(tp_def))
        itp.__module__ = __name__
        namespace[itp.__qualname__] = itp
        # set an alias
        if itp.__qualname__ == "mvWindowAppItem":
            namespace['mvWindow'] = namespace['Window'] = itp
            exported(itp, 'mvWindow')
            exported(itp, 'Window')
        elif itp.__qualname__  == 'mvAnnotation':
            namespace['PlotAnnotation'] = itp
            exported(itp, 'PlotAnnotation')
        else:
            alias = itp.__qualname__.removeprefix('mv')
            if alias[0].isdigit():
                alias = f'{alias[2:]}{alias[0]}{alias[1].upper()}'
            assert alias not in namespace
            namespace[alias] = itp
            exported(itp, alias)

    globals().update(namespace)


_fill_namespace()
