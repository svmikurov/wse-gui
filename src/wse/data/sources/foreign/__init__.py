"""Foreign discipline sources."""

__all__ = [
    'WordParamsNetworkSourceABC',
    'WordParamsLocaleSourceABC',
    'ParamsNotifyT',
    'WordParamsNotifyABC',
    'WordStudySettingsLocaleSourceABC',
    'WordStudyPresentationNetworkSourceABC',
]

from .abc import (
    ParamsNotifyT,
    WordParamsLocaleSourceABC,
    WordParamsNetworkSourceABC,
    WordParamsNotifyABC,
    WordStudyPresentationNetworkSourceABC,
    WordStudySettingsLocaleSourceABC,
)
