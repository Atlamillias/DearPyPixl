from . import dpg
from .dpgwrap.stylize import Font as _Font
from .dpgwrap._item import Item



class Font:
    def __init__(self, name: str, size: float):
        self.name = name





class FontStyle(_Font):
    def __init__(self, file: str, size: float):
        super().__init__(file, size)
        