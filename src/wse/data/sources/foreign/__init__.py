"""Foreign discipline sources."""

__all__ = [
    'WordParamsNetworkSourceABC',
    'WordParamsLocaleSourceABC',
    'ParamsNotifyT',
    'WordParamsNotifyABC',
    'WordStudySettingsLocaleSourceABC',
    'WordStudyPresentationNetworkSourceABC',
    'WordStudyProgressNetworkSourceABC',
]

from .abc import (
    ParamsNotifyT,
    WordParamsLocaleSourceABC,
    WordParamsNetworkSourceABC,
    WordParamsNotifyABC,
    WordStudyPresentationNetworkSourceABC,
    WordStudyProgressNetworkSourceABC,
    WordStudySettingsLocaleSourceABC,
)
