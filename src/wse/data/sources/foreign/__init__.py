"""Foreign discipline sources."""

__all__ = [
    'WordParametersNetworkSourceABC',
    'WordParametersLocaleSourceABC',
    'NotifyT',
    'WordParametersNotifyABC',
    'WordPresentationNetworkSourceABC',
    'WordPresentationLocaleSourceABC',
    'WordStudyProgressNetworkSourceABC',
    # Word study data parameters
    'WordParametersData',
    'WordParametersLocaleSource',
    'WordParametersNetworkSource',
    # Word study data
    'WordPresentationData',
    'WordPresentationLocaleSource',
    'WordPresentationNetworkSource',
]

from .abc import (
    NotifyT,
    WordParametersLocaleSourceABC,
    WordParametersNetworkSourceABC,
    WordParametersNotifyABC,
    WordPresentationLocaleSourceABC,
    WordPresentationNetworkSourceABC,
    WordStudyProgressNetworkSourceABC,
)
from .params import (
    WordParametersData,
    WordParametersLocaleSource,
    WordParametersNetworkSource,
)
from .study import (
    WordPresentationData,
    WordPresentationLocaleSource,
    WordPresentationNetworkSource,
)
