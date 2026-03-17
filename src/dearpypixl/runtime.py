import typing
import sys
import time
import collections

from dearpygui import dearpygui, _dearpygui

from dearpypixl.core import management


__all__ = ("Runtime",)




class RuntimeExit(StopIteration):
    __slots__ = ()


class Signal(StopIteration):
    __slots__ = ()

    def __call__(self, runtime: Runtime, /) -> typing.Any:
        pass

@typing.final
class RESUME(Signal):
    __slots__ = ()

@typing.final
class STOP(Signal):
    __slots__ = ()

    def __call__(self, runtime: Runtime, /) -> None:
        raise RuntimeExit

@typing.final
class PAUSE(Signal):
    __slots__ = ()

    def __call__(self, runtime: Runtime, /) -> None:
        while True:
            time.sleep(0)
            try:
                runtime._emit_signal()
            except Signal as signal:
                runtime.signal(signal)
                return


def _debug_process_callbacks(*, _get_callbacks=_dearpygui.get_callback_queue, _run_callbacks=dearpygui.run_callbacks) -> None:
    _run_callbacks(_get_callbacks())

def _do_nothing() -> None: pass

class Runtime[T: typing.Callable]:
    def __init__(self, /, *, frame_rate_limit: int = 0, update_interval: float = 2.0) -> None:
        self.queue = collections.deque[T]()
        self.ts_last_update = 0
        self.ts_last_render = 0

        self.frame_rate_limit = frame_rate_limit
        self.update_interval = update_interval

        self._is_running = False
        self._emit_signal = _do_nothing
        self._dpg_queue_processor = _do_nothing

    @property
    def frame_rate_limit(self) -> int:
        return self._frame_rate_limit
    @frame_rate_limit.setter
    def frame_rate_limit(self, value: int, /) -> None:
        if value < 1:
            self._frame_rate_limit = self._render_interval = 0
        else:
            self._frame_rate_limit, self._render_interval = value, int(1_000_000_000 // value)

    @property
    def update_interval(self, /) -> float:
        return self._update_interval / 1_000_000
    @update_interval.setter
    def update_interval(self, value: float, /) -> None:
        # convert to nanoseconds
        if value < 0.1:
            self._update_interval = 100_000
        else:
            self._update_interval = int(value * 1_000_000)

    @typing.overload
    def configure(self, /, *, frame_rate_limit: int = ..., update_interval: float = ...) -> None: ...  # type: ignore
    def configure(self, /, *, frame_rate_limit: int | None = None, update_interval: float | None = None):
        if frame_rate_limit is not None:
            self.frame_rate_limit = frame_rate_limit
        if update_interval is not None:
            self.update_interval = update_interval

    def configuration(self, /) -> dict[str, typing.Any]:
        return {"frame_rate_limit": self.frame_rate_limit, "update_interval": self.update_interval}

    @property
    def frame_rate(self, /) -> float:
        return _dearpygui.get_frame_rate()

    @property
    def frame_count(self, /) -> int:
        return _dearpygui.get_frame_count()

    @property
    def time_elapsed(self, /) -> float:
        return _dearpygui.get_total_time()

    def update(self, /) -> None:
        try:
            task = self.queue.popleft()
        except IndexError:
            # This implementation does not "look" before popping the queue. This
            # makes task-heavy applications more performant overall, but task-light
            # applications take a performance hit from repeatedly handling
            # `IndexError`. This function helps limit the latter by ensuring there's
            # always a task to pop.
            def _internal_runtime_task(*, __queue=self.queue):
                __queue.append(_internal_runtime_task)  # type: ignore
            _internal_runtime_task.__name__ = "_internal_runtime_task"

            self.queue.append(_internal_runtime_task)  # type: ignore

            return
        task()

    # native C Python functions don't support the descriptor protocol,
    # so they'll always be "static" (although the type checker doesn't
    # know that)
    render = typing.cast(staticmethod, _dearpygui.render_dearpygui_frame)

    def is_running(self, /) -> bool:
        return self._is_running

    def run(self, /) -> None:
        self._is_running = True

        try:
            timer  = time.perf_counter_ns
            render = self.render
            update = self.update
            process_backend_queue = self._dpg_queue_processor

            tb_updates = 0
            tb_idle    = 0

            self.ts_last_update = self.ts_last_render = timer()
            render()

            while True:

                while True:
                    try:
                        self._emit_signal()
                    except Signal as e:
                        signal = e
                        break

                    process_backend_queue()

                    ts_this_update      = timer() - tb_idle
                    tb_updates          = tb_updates + ts_this_update - self.ts_last_update
                    self.ts_last_update = ts_this_update

                    update_interval = self._update_interval
                    while tb_updates >= update_interval:
                        update()
                        tb_updates -= update_interval

                    ts_this_render = timer()
                    if ts_this_render - self.ts_last_render >= self._render_interval:
                        self.ts_last_render = ts_this_render
                        render()

                ts_idle = timer()
                try:
                    signal(self)
                except RuntimeExit:
                    break
                finally:
                    tb_idle += timer() - ts_idle

        finally:
            self._is_running = False

    PAUSE  = PAUSE
    RESUME = RESUME
    STOP   = STOP

    def signal(self, signal: type[Signal] | Signal, /) -> None:
        def emitter():
            try:
                raise signal
            finally:
                self._emit_signal = _do_nothing

        self._emit_signal = emitter

    @management.initializer
    def start(self, *, debug: bool | None = False):
        if self._is_running:  # not a thread-safe check
            return self.signal(self.RESUME)

        if (
            (debug or dearpygui.get_app_configuration()["manual_callback_management"]) or
            debug is None and sys.gettrace() is not None
        ):
            processor = _debug_process_callbacks
            dearpygui.configure_app(manual_callback_management=True)
        else:
            processor = _do_nothing

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

        self._dpg_queue_processor = processor
        self._emit_signal = _do_nothing

        self.run()

    def pause(self, /) -> None:
        self.signal(self.PAUSE)

    def stop(self, /) -> None:
        self.signal(self.STOP)
