# pyright: reportNoOverloadImplementation=false, reportRedeclaration=false
import typing
import sys
import functools
import threading
import collections

from dearpygui import dearpygui, _dearpygui




class Pool:
    # BUG: TLDR - `generate_uuid()` is REALLY slow
    # <https://github.com/hoffstadt/DearPyGui/issues/2028>
    #
    # This module replaces the former solution - a simple counter
    # (`itertools.count()`). It was gimmicky because it required
    # patching nearly EVERY Dear PyGui function to keep it from
    # churning its own UUID registry in an attempt to avoid
    # collisions. This solution is unfortunately slower than the
    # former, but still magnitudes faster than `generate_uuid()`
    # and is completely stable.

    def __init__(self, /, size: int = 16, *, auto_prime: bool = False, min_size: int = -1, parent: int = 0) -> None:
        self._lock = threading.Lock()
        self._pool = collections.deque()
        self._pool2 = collections.deque()
        self._alloc = self._pool.popleft
        self._parent = parent
        self._min_size = max(min_size, 1)
        self.pool_size = size
        self.auto_prime = auto_prime

    def __del__(self) -> None:
        # prevents segfaults from C-extensions (dearpygui) during
        # interpreter shutdown
        if sys.is_finalizing():
            return
        try:
            pool, pool2 = self._pool, self._pool2
        except AttributeError:
            pass
        else:
            try:
                glbl_pool = _POOL
            except NameError:
                pass
            else:
                if self is not glbl_pool:
                    glbl_pool.free(pool)
                    glbl_pool.free(pool2)
            pool.clear()
            pool2.clear()

        try:
            parent = self._parent
        except AttributeError:
            pass
        else:
            try:
                _dearpygui.delete_item(parent, children_only=False, slot=-1)
            except:
                pass

        self.__dict__.clear()

    def get_pool_size(self, /) -> int:
        """Return the number of UUID's pooled during automatic
        primes."""
        return len(self._iter)

    def set_pool_size(self, size: int, /) -> None:
        """Set the number of UUID's reserved during automatic primes."""
        if size < 1:
            raise ValueError("'size' must be greater than zero")
        self._iter = tuple(0 for _ in range(size))

    pool_size = property(get_pool_size, set_pool_size)

    def count(self, /) -> int:
        """Return the number of UUID's ready for allocation."""
        return len(self._pool)

    def __len__(self, /) -> int:
        return self.count()

    def alloc(self, /) -> int:
        """Generate a unique, unused item UUID."""
        try:
            return self._alloc()
        except IndexError:
            pass

        with self._lock:
            # try once more, in case the registry was primed while
            # awaiting the lock
            try:
                return self._alloc()
            except IndexError:
                if not self.auto_prime:
                    raise BufferError("pool is empty") from None

            pool, pool2 = self._pool, self._pool2
            alloc = self._pool2.popleft

            self._prime(self._iter, pool2)
            uuid = alloc()

            self._pool, self._pool2, self._alloc = pool, pool2, alloc

        return uuid

    def free(self, uuid: int | typing.Iterable[int], /) -> None:
        """Recycle one or more UUIDs no longer used as item identifiers.
        Once recycled, that UUID may be returned by :py:func:`alloc()`.

        UUIDs do not need to be explicitly released when they are no longer
        used, but doing so has performance benefits when frequently creating
        and deleting large quantities of items.

        This function does not verify that UUIDs are unused. It is the user's
        responsibility to ensure that all UUIDs are not in-use as item
        identifiers.
        """
        if isinstance(uuid, int):
            self._pool.append(uuid)
        else:
            self._pool.extend(uuid)

    def prime(self, size: int | None = None, /) -> None:
        """Reserve additional UUID's in the registry, making them
        available for allocation.

        The pool is automatically primed when emptied. Priming
        before it empties can be more performant in some cases.

        Priming the pool holds Dear PyGui's mutex.
        """
        if size is None:
            iterator = self._iter
        elif size < self._min_size:
            raise ValueError(f"'size' must be greater than {self._min_size - 1}")
        else:
            iterator = range(size)

        with self._lock:
            self._prime(iterator)

    def _prime(
        self,
        iterator,
        pool = None,
        /, *,
        push_container_stack = _dearpygui.push_container_stack,
        pop_container_stack = _dearpygui.pop_container_stack,
        delete_item = _dearpygui.delete_item,
        lock_mutex = _dearpygui.lock_mutex,
        unlock_mutex = _dearpygui.unlock_mutex,
        add_item = _dearpygui.add_spacer,
    ):
        if pool is None:
            pool = self._pool

        parent = self._parent

        # XXX: using the container stack would be more faster, but
        # it's not thread-safe
        try:
            pool.extend([add_item(parent=parent) for _ in iterator])
        except SystemError:
            if not (parent or _dearpygui.does_item_exist(parent)):
                parent = self._parent = _dearpygui.add_stage(
                    label='', user_data=None, use_internal_label=True, tag=parent
                )
                pool.extend([add_item(parent=parent) for _ in iterator])
            else:
                raise
        delete_item(parent, children_only=True, slot=-1)


def _init_global_pool():
    global _POOL, _init_global_pool, count, alloc, free, prime, get_pool_size, set_pool_size

    _POOL = Pool(500, auto_prime=True, min_size=64, parent=_dearpygui.mvReservedUUID_10)

    alloc = _POOL.alloc
    free = _POOL.free
    prime = _POOL.prime
    count = _POOL.count
    get_pool_size = _POOL.get_pool_size
    set_pool_size = _POOL.set_pool_size

    @functools.wraps(dearpygui.generate_uuid)
    def generate_uuid(**kwargs) -> int:
        return alloc()

    dearpygui.generate_uuid = generate_uuid
    del _init_global_pool

_init_global_pool()
