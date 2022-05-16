import functools
from typing import Callable, Sequence
from abc import ABC, abstractmethod



class TypeGuard:
    def __init__(self, types: tuple[type | object, ...] = None, callback: Callable = None, type_err_msg: str = None, value_err_msg: str = None):
        """Creates a callable validator object for checking argument(s) against certain
        criteria.

        Args:
            * types (type | object, ...], optional): A tuple of types that will be passed
            as the second argument of `isinstance`; raises TypeError if <argument> are not
            instances of <types>. Defaults to None (no error).
            * callback (Callable, optional): Raises ValueError if the result of
            `callback(argument)` is falsey. Defaults to None (no error).
        """
        self._types    = types or (object,)
        self._callback = callback or (lambda x: True)

        if not type_err_msg:
            if not types or len(self._types) == 1:
                type_err_msg = f"Value must be an instance of {self._types[0].__qualname__!r} (got {{}})."
            else:
                _qualnames = []
                for t in self._types:
                    try:
                        _qualnames.append(t.__qualname__)
                    except AttributeError:
                        _qualnames.append(t)
                type_err_msg = f"Value must be an instance of {', '.join(name for name in _qualnames[:-1])!r} or {_qualnames[-1]!r} (got {{}})."
        if not value_err_msg:
            value_err_msg = f"Result of `{self._callback.__qualname__}(<argument>)` is falsey (got type {{cls}} value {{value}})."

        self._type_err_msg = type_err_msg
        self._val_err_msg  = value_err_msg

    def __call__(self, argument: Sequence[object] | object):  # NOTE: won't work for mapping values)
        """Raise TypeError if the argument (or any argument in a sequence of arguments) is
        not an instance of <types>, or ValueError if `callback(argument)` does not return True.

        Args:
            * argument (Sequence[object] | object): The object to check. If the object is
            a sequence, all objects within that sequence are checked (the sequence itself 
            will not be checked).

        """
        types    = self._types
        callback = self._callback
        if not isinstance(argument, Sequence):
            argument = (argument,)
        for arg in argument:
            if not isinstance(arg, types):
                err_msg = self._type_err_msg.format(repr(arg))
                raise TypeError(err_msg)
            if not callback(arg):
                err_msg = self._val_err_msg.format(cls=repr(type(arg).__qualname__), value=repr(arg))
                raise ValueError(err_msg)

    def wraps(self, func: Callable = None, target_idx: int = 0):
        """(Decorator) Validate an argument of <func> before it is called.

        Args:
            * func (callable): Any callable object.
            * target_idx (int, optional): Used to index <func>'s sequence of 
            arguments. The result will be validated.
        """
        @functools.wraps(func)
        def wrapper(func: Callable):
            def callable_object(*args):
                self(args[target_idx])
                return func(*args)
            return callable_object
        if func:
            return wrapper(func)
        return wrapper


