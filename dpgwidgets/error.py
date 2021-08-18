class ViewportError(Exception):
    """Raised when a Viewport instance is made and one already
    exists.
    """

class AppItemConfigError(Exception):
    """Raised when an Item's internal configuration cannot
    be properly set.
    """