import dearpypixl.appitems.colors
from dearpypixl.appitems.colors import *

from typing import Union, Any
from dearpygui import dearpygui

__all__ = [*dearpypixl.appitems.colors.__all__]


class ColorMap(ColorMap):
    # TODO: Maybe make list-like for access to `colors`.
    def __init__(
        self                                                             ,
        colors            : list[Union[list[int], tuple[int, ...]]]      ,
        qualitative       : bool                                         ,
        label             : str                                    = None,
        user_data         : Any                                    = None,
        use_internal_label: bool                                   = True,
        show              : bool                                   = True,
        parent            : Union[int, str]                        = 14  ,
        **kwargs                                                         ,
    ) -> None:
        super().__init__(
            colors=colors,
            qualitative=qualitative,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            show=show,
            parent=parent,
            **kwargs,
        )

    def get_color_at_value(self, value: float) -> Union[list[float], tuple[float, ...]]:
        """Return the normalized values of a color from the ColorMap at <value>.
        Up to four values can be returned in the sequence: red, green, blue, alpha.

        Args:
            * value (float): Value of the colormap to sample. Minimum value is 0.0,
            maximum value is 1.0.
        """
        return dearpygui.sample_colormap(self._tag, value)

    def get_color_at_index(self, index: int) -> Union[list[float], tuple[float, ...]]:
        """Return the normalized values of a color from the ColorMap at <index>. For example,
        `index=0` vould return the first color in ColorMap's list of colors (`colors` argument
        used to create this item). Modulo will be performed against the number of items in the
        color list. Up to four values can be returned in the sequence: red, green, blue, alpha.

        Args:
            index (int): Position of the color in the ColorMap's list of colors to quiey.
        """
        return dearpygui.get_colormap_color(self._tag, index)