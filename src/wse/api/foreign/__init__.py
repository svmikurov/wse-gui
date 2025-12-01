"""Foreign discipline API schemas."""

__all__ = [
    # Abstract base classes
    'WordParametersApiABC',
    'WordProgressApiABC',
    'WordPresentationApiABC',
    # Implementation
    'WordPresentationApi',
    'WordParametersApi',
]

from .abc import (
    WordParametersApiABC,
    WordPresentationApiABC,
    WordProgressApiABC,
)
from .params import WordParametersApi
from .presentation import WordPresentationApi
