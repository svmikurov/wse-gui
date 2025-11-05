"""Foreign discipline repositories."""

__all__ = [
    'RefreshWordParamsRepoABC',
    'GetWordStudyRepoABC',
    'SetWordParamsRepoABC',
    'WordParamsRepoABC',
    'WordParamsMapperABC',
    'WordStudySettingsRepoABC',
    'WordStudyProgressRepoABC',
]

from .abc import (
    GetWordStudyRepoABC,
    RefreshWordParamsRepoABC,
    SetWordParamsRepoABC,
    WordParamsMapperABC,
    WordParamsRepoABC,
    WordStudyProgressRepoABC,
    WordStudySettingsRepoABC,
)
