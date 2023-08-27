"""Theme color-element interfaces."""

def _fill_namespace():
    # XXX: This is defined twice ('color.py' and 'style.py').
    # Change one when changing the other.
    from ._dearpypixl import interface, parsing, mkstub

    exported = mkstub.Exported(__name__)

    itp_ns = {}
    for const, tp_def in parsing.theme_color_definitions().items():
        # This is already sorted so that 'core' elements are processed
        # first. This is because some processed class names may overshadow
        # others; 'core' elements keep the more intuitive name, while 'plot'
        # and 'node' elements get renamed.
        itp = interface.itp_theme_element_from_def(tp_def)
        itp.__module__ = __name__
        if itp.__qualname__ in itp_ns:
            old_name = itp.__qualname__
            itp.__qualname__ = f"{itp.category.name.title()}{old_name}"
            assert itp.__qualname__ not in itp.__name__
            itp.__name__ = itp.__name__.replace(old_name, itp.__qualname__)
            assert itp.__qualname__ not in itp_ns
        exported(itp)
        itp_ns[itp.__qualname__] = itp

    globals().update(itp_ns)


_fill_namespace()
