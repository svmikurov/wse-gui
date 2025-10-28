"""Foreign discipline repositories."""

__all__ = [
    'RefreshWordParamsRepoABC',
    'GetWordStudyRepoABC',
    'SetWordParamsRepoABC',
    'WordParamsRepoABC',
    'WordParamsMapperABC',
]

from .abc import (
    GetWordStudyRepoABC,
    RefreshWordParamsRepoABC,
    SetWordParamsRepoABC,
    WordParamsMapperABC,
    WordParamsRepoABC,
)
