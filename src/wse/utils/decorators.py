"""Defines decorators for logging and other purposes."""

import functools
from typing import Any, Callable, TypeVar

T = TypeVar('T', bound=Callable[..., Any])


def log_function_signature(func: T) -> T:
    """Log function calls with args and return values."""

    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        # Logging the function name and arguments
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling a function: {func.__name__}({signature})')

        # Call the function and get the result
        result = func(*args, **kwargs)

        # Logging the return value
        print(f'Function `{func.__name__}()` returned: {result!r}')
        return result

    return wrapper
