import typing
import sys
import time
import inspect
import collections
import threading

from dearpygui import dearpygui, _dearpygui

from dearpypixl.core import management
from dearpypixl.core.protocols import property, ItemCallback
from dearpypixl.core.parsing import DEARPYGUI_VERSION




# [ Runtime ]

@typing.overload
def _trunc(f: float, prec: int = 3, /) -> float: ...  # pyright: ignore[reportInconsistentOverload]
def _trunc(f: float, prec: int = 3, /, *, _int=int) -> float:
    mod = 10 ** prec
    return _int(f * mod) / mod

@typing.overload
def _perf_counter_ms() -> float: ...  # pyright: ignore[reportInconsistentOverload]
def _perf_counter_ms(*, _counter=time.perf_counter) -> float:
    return 1000.0 * _counter()

@typing.overload
def _debug_process_callbacks() -> None: ...  # pyright: ignore[reportInconsistentOverload]
def _debug_process_callbacks(*, _get_callbacks=_dearpygui.get_callback_queue, _run_callbacks=dearpygui.run_callbacks) -> None:
    _run_callbacks(_get_callbacks())

def _do_nothing() -> None:
    pass



class Signal(Exception):
    __slots__ = ()

class PAUSE(Signal):
    __slots__ = ()

class RESUME(Signal):
    __slots__ = ()

class STOP(Signal):
    __slots__ = ()


class Runtime:
    """Minimalistic event loop implementation for Dear PyGui and
    Dear PyPixl. Users can push tasks to run within the loop.
    Optionally, a limit can be set on the frame rate. Updates and
    renders run independently.

    Starting the runtime starts the Dear PyGui event loop. This:
    ```python
    import dearpypixl as dpx

    dpx.Runtime().start()
    ```
    Is similar to this:
    ```python
    import dearpygui.dearpygui as dpg

    dpg.create_context()

    # NOTE: called in order & only as necessary i.e. hasn't been called yet
    dpg.setup_dearpygui()
    dpg.create_viewport()
    dpg.show_viewport()

    dpg.start_dearpygui()
    ```
    To stop the event loop, call the :py:meth:`Runtime.stop()` method
    or `dearpygui.stop_dearpygui()`.

    Callables in :py:attr:`Runtime.queue` are executed within the event
    loop via the :py:meth:`Runtime.update()` method. By default, the
    queue itself is an instance of `collections.deque`; calling
    :py:meth:`Runtime.update()` pops and runs the left-most task e.g.
    `queue.popleft()()`. Both :py:attr:`Runtime.queue` and
    :py:meth:`Runtime.update()` can be reassigned or overridden via
    subclassing as needed.

    The default implementation of the event loop uses a synchronized
    fixed time step (:py:attr:`Runtime.update_interval`). It represents
    the length of time of each tick/update in milliseconds, regardless of
    how long a specific task takes to run. For example, the default
    time step of `2.0` ensures that no more than 5 ticks will occur over
    10 milliseconds. The runtime may tick *less*, however, if it takes
    longer than 2 milliseconds per update on average. Therefore, updates
    should be small and numerous. If a specific task is blocking other
    updates or affecting frame rate, consider breaking it up into smaller
    functions (keep in mind that tasks can enqueue other tasks).

    :vartype frame_rate_limit: `int`
    :var frame_rate_limit: The upper limit of frames to render per
        second. Clamp is disabled when this value is less than 1.

    :vartype update_interval: `float`
    :var update_interval: The minimum number of milliseconds each update
        will "consume". Serves as the upper limit for updates churned
        over a length of time.

    :vartype queue: `deque`
    :var queue: Contains updates to be processed by the runtime.
        Internally, it is only referenced by :py:meth:`Runtime.update()`.
        It is safe to reassign this to a different object type if
        :py:meth:`Runtime.update()` is also reassigned or overridden
        to work with the new queue type.

    :vartype ts_last_update: `float`
    :var ts_last_update: The return value of `time.perf_counter()`
        in milliseconds representing when the runtime last "ticked".
        This is only updated once per event loop iteration, after running
        the last update for that iteration.

    :vartype ts_last_render: `float`
    :var ts_last_render: The return value of `time.perf_counter()`
        in milliseconds representing when the runtime last rendered a
        frame.
    """
    def __init__(self, /, *, frame_rate_limit: int = 0, update_interval: float = 2.0) -> None:
        self.queue = collections.deque()
        self.ts_last_update = 0.0
        self.ts_last_render = 0.0

        self.frame_rate_limit = frame_rate_limit
        self.update_interval = update_interval

        self._signal_hook = _do_nothing
        self._dpg_queue_processor = _do_nothing

    @property
    def frame_rate_limit(self) -> int:
        """[get, set] the upper limit of frames to render per second. Clamp is
        disabled when this value is less than 1."""
        return self._frame_rate_limit
    @frame_rate_limit.setter
    def frame_rate_limit(self, value: int, /) -> None:
        if value < 1:
            self._render_interval = self._frame_rate_limit = 0
        else:
            self._render_interval, self._frame_rate_limit = _trunc(value, 3), value

    @property
    def update_interval(self, /) -> float:
        """[get, set] the minimum number of milliseconds each update will
        "consume". Serves as the upper limit for updates churned over a
        length of time."""
        return self._update_interval
    @update_interval.setter
    def update_interval(self, value: float, /) -> None:
        if value < 0.1:
            self._update_interval = 0.1
        else:
            self._update_interval = _trunc(value, 3)

    @typing.overload
    def configure(self, /, *, frame_rate_limit: int = ..., update_interval: float = ...) -> None: ...  # type: ignore
    def configure(self, /, *, frame_rate_limit: int | None = None, update_interval: float | None = None):
        if frame_rate_limit is not None:
            self.frame_rate_limit = frame_rate_limit
        if update_interval is not None:
            self.update_interval = update_interval

    def configuration(self, /) -> dict[typing.Literal["frame_rate_limit", "update_interval"], typing.Any]:
        return {"frame_rate_limit": self.frame_rate_limit, "update_interval": self.update_interval}

    @property
    def frame_rate(self, /) -> float:
        """[get] the average frame rate across 120 frames."""
        return _dearpygui.get_frame_rate()

    @property
    def frame_count(self, /) -> int:
        """[get] the number of frames rendered."""
        return _dearpygui.get_frame_count()

    @property
    def time_elapsed(self, /) -> float:
        """[get] the number of fractional seconds elapsed since the
        runtime was started. By default, this returns the result of
        `dearpygui.get_total_time()`.
        """
        return _dearpygui.get_total_time()

    def update(self, /) -> None:
        """"Tick" the runtime, processing one update.

        The default implementation expects the runtime queue to be
        an instance of `collections.deque` and calls the result of
        its `popleft()` method.
        """
        try:
            if self.queue: self.queue.popleft()()
        except IndexError:
            pass

    # These casts are just to satisfy the type checker. C-functions
    # don't implement the descriptor interface (i.e. `__get__()`) and
    # therefore cannot be bound. The interpreter knows this and will
    # automatically unwrap them.
    # They *should* be wrapped in normal instance methods, but they're
    # unbound so they can be ran as fast as possible.
    @staticmethod
    def render() -> None:
        """Renders one frame."""
        ...
    render = _dearpygui.render_dearpygui_frame

    @staticmethod
    def is_running() -> bool:
        """Return `True` if Dear PyGui is running."""
        ...
    is_running = _dearpygui.is_dearpygui_running

    def run(self, /) -> None:
        """Event loop implementation. Calling this method starts
        the loop.

        NOTE: You want :py:meth:`Runtime.start()`.
        """
        trunc_6f = lambda x, int=int, mod=1_000_000: int(x * mod) / mod
        timer = _perf_counter_ms
        update = self.update
        render = self.render
        is_running = self.is_running
        process_backend_queue = self._dpg_queue_processor

        t_updates = 0.0  # time buffer
        ts_last_update = 0.0
        ts_last_render = 0.0

        try:
            while True:
                try:
                    while is_running():
                        process_backend_queue()

                        ts_this_update = timer()
                        t_updates = trunc_6f(t_updates + ts_this_update - ts_last_update)
                        ts_last_update = self.ts_last_update = ts_this_update

                        update_interval = self._update_interval
                        while t_updates >= update_interval:
                            update()
                            t_updates -= update_interval

                        ts_this_render = timer()
                        if ts_this_render - ts_last_render >= self._render_interval:
                            ts_last_render = self.ts_last_render = ts_this_render
                            render()

                        self._signal_hook()

                    break

                except RESUME:
                    continue

                except PAUSE:
                    sys.last_exc = sys.last_type = sys.last_traceback = None
                    while True:
                        time.sleep(0)
                        try:
                            self._signal_hook()
                        except RESUME:
                            break
                        except PAUSE:
                            pass

        except STOP:
            return

    @management.initializer
    def start(self, *, debug: bool | None = None):
        """Finishes Dear PyGui initialization and runs the event loop.

        :type debug: `bool | None`
        :param debug: If `True`, enable Dear PyGui's manual callback
            management setting and process those callbacks in the
            event loop (separate from the runtime's updates). If
            `None`, enable manual callback management only when a
            debugging trace is set.
        """
        if not dearpygui.is_viewport_ok():
            try:
                dearpygui.create_viewport()
            except SystemError:
                pass
            try:
                dearpygui.show_viewport()
            except SystemError:
                pass
            if not dearpygui.is_viewport_ok():
                raise RuntimeError("cannot create and/or initialize viewport")

        if (
            (debug or dearpygui.get_app_configuration()["manual_callback_management"]) or
            debug is None and sys.gettrace() is not None
        ):
            self._dpg_queue_processor = _debug_process_callbacks
            dearpygui.configure_app(manual_callback_management=True)
        else:
            self._dpg_queue_processor = _do_nothing

        self._signal_hook = _do_nothing

        self.run()

    PAUSE = PAUSE
    RESUME = RESUME
    STOP = STOP

    def signal(self, err_type: type[Signal], /) -> None:
        def signal_hook():
            try:
                raise err_type
            finally:
                self._signal_hook = _do_nothing

        self._signal_hook = signal_hook
