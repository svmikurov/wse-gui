"""Foreign discipline API schemas."""

__all__ = [
    # Abstract base classes
    'WordParametersApiABC',
    'WordProgressApiABC',
    'WordPresentationApiABC',
    # Implementation
    'WordPresentationApi',
    'WordParametersApi',
    'WordStudyProgressApi',
    # Payload types
    'UpdateProgressPayload',
]

from .abc import (
    UpdateProgressPayload,
    WordParametersApiABC,
    WordPresentationApiABC,
    WordProgressApiABC,
)
from .params import WordParametersApi
from .presentation import WordPresentationApi
from .progress import WordStudyProgressApi
