"""Development utility decorators."""

import logging
from functools import wraps
from typing import Any, Callable, TypeVar

F = TypeVar('F', bound=Callable[..., Any])

audit = logging.getLogger('audit')


def log_unimplemented_call(func: F) -> F:
    """Log that called method is not implemented yet."""

    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        class_name = (
            args[0].__class__.__name__
            if args and hasattr(args[0], '__class__')
            else ''
        )
        method_name = (
            f'{class_name}.{func.__name__}' if class_name else func.__name__
        )
        audit.warning(f'Called unimplemented method: `{method_name}()`')
        return func(*args, **kwargs)

    return wrapper  # type: ignore[return-value]


def log_implementation(func: F) -> F:
    """Add logging to the wrapped function."""

    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        class_name = (
            args[0].__class__.__name__
            if args and hasattr(args[0], '__class__')
            else ''
        )
        method_name = (
            f'{class_name}.{func.__name__}' if class_name else func.__name__
        )
        audit.debug(f'Start method: `{method_name}()`')

        result = func(*args, **kwargs)

        audit.debug(f'End method: `{method_name}()`')
        return result

    return wrapper  # type: ignore[return-value]
