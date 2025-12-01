"""Foreign discipline repositories."""

__all__ = [
    'RefreshWordParametersRepositoryABC',
    'WordPresentationRepoABC',
    'SetWordParametersRepoABC',
    'WordParametersRepoABC',
    'WordParametersSubscriberABC',
    'WordProgressRepoABC',
    'WordParametersRepo',
    'WordPresentationRepo',
]

from .abc import (
    RefreshWordParametersRepositoryABC,
    SetWordParametersRepoABC,
    WordParametersRepoABC,
    WordParametersSubscriberABC,
    WordPresentationRepoABC,
    WordProgressRepoABC,
)
from .params import WordParametersRepo
from .study import WordPresentationRepo
