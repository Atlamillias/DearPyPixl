"""Contains a simple application runtime in the form of
the :py:class:`Runtime` class and a few signals. It
features a task queue for running updates directly in the
event loop and framerate management.

Starting the runtime starts the DearPyGui event loop. This:
```python
from dearpypixl.runtime import Runtime

Runtime().start()
```

Is similar to this:
```python
import dearpygui.dearpygui as dpg

dpg.create_context()

# NOTE: the following are only called if they have not been ran already
dpg.setup_dearpygui()
dpg.create_viewport()
dpg.show_viewport()

dpg.start_dearpygui()
```
"""
from typing import *
from collections import deque


__all__ = ("Runtime",)




class Signal(StopIteration):
    """Base class for :py:class:`Runtime` signals. Receives the
    runtime object and executes a subroutine. The runtime is paused
    until the signal returns.

    Subclasses must implement `__call__()`.
    """
    def __call__(self, runtime: Runtime, /) -> Any: ...

@final
class PAUSE(Signal):
    """A signal processed by a :py:class:`Runtime` object. When
    processed, the runtime will halt until it receives another
    signal.
    """

@final
class RESUME(Signal):
    """A signal processed by a :py:class:`Runtime` object. When
    processed, the runtime will resume running if paused."""

@final
class STOP(Signal):
    """A signal processed by a :py:class:`Runtime` object. When
    processed, the runtime will stop. A runtime stopped via this
    signal cannot be resumed via the :py:class:`RESUME` signal,
    but does not destroy the application context or runtime state.

    This signal cannot be subclassed, but a user-implemented
    signal can reproduce its behavior by having their signal raise
    :py:class:`RuntimeExit`.
    """


class RuntimeExit(StopIteration):
    """The result of processing the :py:class:`STOP` signal.

    This exception is managed by the :py:class:`Runtime` object
    that receives the signal. The error is not propegated beyond
    the running event loop.
    """


class Runtime[T: Callable]:
    """Minimalistic event loop implementation for DearPyGui and
    DearPyPixl. Users can push tasks to run within the loop.
    Optionally, a limit can be set on the frame rate. Updates and
    renders run independently. The event loop is started via
    :py:meth:`Runtime.start()` and stopped via :py:meth:`Runtime.stop()`.

    A runtime can be created before initializing DearPyGui. It will
    fully initialize or finish initializing DearPyGui and the
    application state when the :py:meth:`Runtime.start()` method is
    called.

    Callables in :py:attr:`Runtime.queue` are executed within the event
    loop via the :py:meth:`Runtime.update()` method. By default, the
    queue itself is an instance of `collections.deque` — calling
    :py:meth:`Runtime.update()` pops and runs the left-most task e.g.
    `runtime.queue.popleft()()`. Both :py:attr:`Runtime.queue` and
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
    functions.

    :vartype PAUSE: `ClassVar[type[PAUSE]]`
    :var PAUSE: A built-in signal. Refer to :py:meth:`Runtime.signal()`
        and :py:class:`PAUSE` for more information.

    :vartype RESUME: `ClassVar[type[RESUME]]`
    :var RESUME: A built-in signal. Refer to :py:meth:`Runtime.signal()`
        and :py:class:`RESUME` for more information.

    :vartype STOP: `ClassVar[type[STOP]]`
    :var STOP: A built-in signal. Refer to :py:meth:`Runtime.signal()`
        and :py:class:`STOP` for more information.

    :vartype frame_rate_limit: `int`
    :var frame_rate_limit: The upper limit of frames to render per
        second. Clamp is disabled when this value is less than 1.

    :vartype update_interval: `float`
    :var update_interval: The time step used by the runtime, or the minimum
        number of milliseconds each update will "consume" (min. `0.1`).
        Serves as the upper limit for updates churned over a length of time.

    :vartype queue: `deque[Callable]`
    :var queue: Contains updates to be processed by the runtime.
        Internally, it is only referenced by :py:meth:`Runtime.update()`.
        It is safe to reassign this to a different object type if
        :py:meth:`Runtime.update()` is also reassigned or overridden
        to work with the new queue type.

    :vartype ts_last_update: `float`
    :var ts_last_update: Set by the running event loop indicating when
        the runtime last "ticked" or updated. It is the result of
        `time.perf_counter_ns()` but in fractional milliseconds. Note
        that this attribute is only updated once per event loop iteration
        after running the last update for that iteration.

    :vartype ts_last_render: `float`
    :var ts_last_render: Set by the running event loop indicating when
        the runtime last rendered a frame. It is the result of
        `time.perf_counter_ns()` but in fractional milliseconds.
    """
    PAUSE: ClassVar[type[PAUSE]]
    RESUME: ClassVar[type[RESUME]]
    STOP: ClassVar[type[STOP]]
    queue: deque[T]
    ts_last_update: float
    ts_last_render: float
    def __init__(self, /, *, frame_rate_limit: int = 0, update_interval: float = 2.0) -> None: ...
    @property
    def frame_rate_limit(self) -> int:
        """[**get**, **set**] the upper limit of frames to render per second.
        Clamp is disabled when this value is less than 1."""
    @frame_rate_limit.setter
    def frame_rate_limit(self, value: int, /) -> None: ...
    @property
    def update_interval(self, /) -> float:
        """[**get**, **set**] the minimum number of milliseconds each update
        will "consume". Serves as the upper limit for updates churned over a
        window of time."""
    @update_interval.setter
    def update_interval(self, value: float, /) -> None: ...
    def configure(self, /, *, frame_rate_limit: int = ..., update_interval: float = ...) -> None: ...
    def configuration(self, /) -> dict[Literal["frame_rate_limit", "update_interval"], Any]: ...
    @property
    def frame_rate(self, /) -> float:
        """[**get**] the average frame rate across 120 frames."""
    @property
    def frame_count(self, /) -> int:
        """[**get**] the number of frames rendered."""
    @property
    def time_elapsed(self, /) -> float:
        """[**get**] the number of fractional seconds elapsed since the
        runtime was started. By default, this returns the result of
        `dearpygui.get_total_time()`.
        """
    def update(self, /) -> None:
        """"Tick" the runtime, processing one update.

        The default implementation expects the runtime queue to be an
        instance of `collections.deque` and calls the result of its
        `popleft()` method.
        """
    def render() -> None:
        """Renders one frame."""
    def is_running() -> bool:
        """Return `True` if the runtime's event loop is running."""
    def run(self, /) -> None:
        """Event loop implementation. Calling this method starts the loop.

        You shouldn't call this method directly — use :py:meth:`Runtime.start()`
        instead.
        """
    def start(self, *, debug: bool | None = False):
        """Finishes DearPyGui's initialization and runs the event loop,
        or resumes the event loop if paused.

        :type debug: `bool | None`
        :param debug: If `True`, enable DearPyGui's manual callback
            management setting and process those callbacks in the
            event loop (separate from the runtime's updates). If
            `None`, enable manual callback management only when a
            debugging trace is set. Defaults to `False`.
        """
    def signal(self, signal: type[Signal] | Signal, /) -> None:
        """Briefly halt the event loop and execute a subroutine.

        Signals (or interrupts) are special events that run outside
        of the primary event loop. They are similar to regular queued
        updates, except:
        - they are not bound to the runtime's update interval
        - they are handled in-between several ticks
        - only one signal can be set at a time — a new signal will
        overwrite an older signal still pending
        - they are more performant than the former when used in moderation

        There are three built-in signals:
        - :py:class:`PAUSE`: Temporarily suspends the loop.
        - :py:class:`RESUME`: Clears a pending signal and/or resumes the
            suspended loop.
        - :py:class:`STOP`: Terminates the loop.
        """
    def pause(self, /) -> None:
        """Temporarily suspends the running event loop."""
    def stop(self, /) -> None:
        """Terminates the running event loop."""
