import dearpypixl.appitems.plotting
from dearpypixl.appitems.plotting import *

from typing import Any, Callable
from dearpygui import dearpygui as dpg


__all__ = [
    *dearpypixl.appitems.plotting.__all__,
    "PlotAxisX",
    "PlotAxisY",
]


class PlotAxis(PlotAxis):
    @property
    def axis_limits(self) -> tuple[float, float]:
        return dpg.get_axis_limits(self._tag)
    @axis_limits.setter
    def axis_limits(self, value: tuple[float, float]) -> None:
        self.set_limits(*value)

    def get_limits(self) -> tuple[float, float]:
        """Return the current axis limits (ymin, ymax).
        """
        return dpg.get_axis_limits(self._tag)

    def set_limits(self, ymin: float | int = None, ymax: float | int = None, **kwargs) -> None:
        """Sets zoom and pan limits for the axis (ymin, ymax).

        Args:
            * ymin (float | int, optional):
            * ymax (float | int, optional):
        """
        try:
            dpg.set_axis_limits(self.tag, ymin, ymax, **kwargs)
        except SystemError:
            self._err_if_existential_crisis()
            raise

    def set_limits_fit_data(self, **kwargs) -> None:
        """Set the axis limits (ymin, ymax) to fit the largest set of data parented by the axis.
        """
        try:
            dpg.fit_axis_data()
        except SystemError:
            self._err_if_existential_crisis()
            raise

    def set_ticks(self, label_pairs: tuple[tuple[str, float | int], ...], **kwargs) -> None:
        """Replace the default axis ticks with <label_pairs>.

        Args:
            * label_pairs (tuple[tuple[str, float | int], ...]): A sequence of 2-item tuples.
            The first item of each inner tuple is the tick label, while the second is the value
            at which to set the tick.
        """
        return dpg.set_axis_ticks(self.tag, label_pairs)

    def reset_limits(self, **kwargs) -> None:
        """Remove any manually-set axis limits, and apply the default limits.
        """
        return dpg.set_axis_limits_auto(self.tag)

    def reset_ticks(self, **kwargs) -> None:
        """Remove any manually-set axis ticks, and apply the default ticks.
        """
        return dpg.reset_axis_ticks(self.tag)


class PlotAxisX(PlotAxis):
    """Adds an X axis to a plot.
    
        Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (int | str, optional): Parent to add this item to. (runtime adding)
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            no_gridlines (bool, optional): 
            no_tick_marks (bool, optional): 
            no_tick_labels (bool, optional): 
            log_scale (bool, optional): 
            invert (bool, optional): 
            lock_min (bool, optional): 
            lock_max (bool, optional): 
            time (bool, optional): 
    """
    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        parent            : int | str       = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        no_gridlines      : bool            = False          ,
        no_tick_marks     : bool            = False          ,
        no_tick_labels    : bool            = False          ,
        log_scale         : bool            = False          ,
        invert            : bool            = False          ,
        lock_min          : bool            = False          ,
        lock_max          : bool            = False          ,
        time              : bool            = False          ,
        **kwargs                                             ,
    ) -> None:
        super().__init__(
            axis=0,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            no_gridlines=no_gridlines,
            no_tick_marks=no_tick_marks,
            no_tick_labels=no_tick_labels,
            log_scale=log_scale,
            invert=invert,
            lock_min=lock_min,
            lock_max=lock_max,
            time=time,
            **kwargs,
        )


class PlotAxisY(PlotAxis):
    """Adds an Y axis to a plot.
    
        Args:
            label (str, optional): Overrides 'name' as label.
            user_data (Any, optional): User data for callbacks
            use_internal_label (bool, optional): Use generated internal label instead of user specified (appends ### uuid).
            tag (int | str, optional): Unique id used to programmatically refer to the item.If label is unused this will be the label.
            parent (int | str, optional): Parent to add this item to. (runtime adding)
            payload_type (str, optional): Sender string type must be the same as the target for the target to run the payload_callback.
            drop_callback (Callable, optional): Registers a drop callback for drag and drop.
            show (bool, optional): Attempt to render widget.
            no_gridlines (bool, optional): 
            no_tick_marks (bool, optional): 
            no_tick_labels (bool, optional): 
            log_scale (bool, optional): 
            invert (bool, optional): 
            lock_min (bool, optional): 
            lock_max (bool, optional): 
            time (bool, optional): 
    """
    def __init__(
        self                                                 ,
        label             : str             = None           ,
        user_data         : Any             = None           ,
        use_internal_label: bool            = True           ,
        parent            : int | str       = 0              ,
        payload_type      : str             = '$$DPG_PAYLOAD',
        drop_callback     : Callable        = None           ,
        show              : bool            = True           ,
        no_gridlines      : bool            = False          ,
        no_tick_marks     : bool            = False          ,
        no_tick_labels    : bool            = False          ,
        log_scale         : bool            = False          ,
        invert            : bool            = False          ,
        lock_min          : bool            = False          ,
        lock_max          : bool            = False          ,
        time              : bool            = False          ,
        **kwargs                                             ,
    ) -> None:
        super().__init__(
            axis=1,
            label=label,
            user_data=user_data,
            use_internal_label=use_internal_label,
            parent=parent,
            payload_type=payload_type,
            drop_callback=drop_callback,
            show=show,
            no_gridlines=no_gridlines,
            no_tick_marks=no_tick_marks,
            no_tick_labels=no_tick_labels,
            log_scale=log_scale,
            invert=invert,
            lock_min=lock_min,
            lock_max=lock_max,
            time=time,
            **kwargs,
        )
