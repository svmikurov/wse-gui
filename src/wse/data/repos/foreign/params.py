"""Word study params repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.sources.foreign import (
    WordParamsLocaleSourceABC,
    WordParamsNetworkSourceABC,
    WordParamsNotifyABC,
)

from . import (
    WordParamsMapperABC,
    WordParamsRepoABC,
)


@inject
@dataclass
class WordParamsRepo(
    WordParamsRepoABC,
):
    """Word study params repository."""

    _network_params_source: WordParamsNetworkSourceABC
    _local_params_source: WordParamsLocaleSourceABC

    @override
    def refresh_initial_params(self) -> None:
        """Set available params, default for Word study params."""
        params = self._network_params_source.fetch_initial_params()
        self._local_params_source.set_initial_params(params)


@inject
@dataclass
class WordParamsMapper(WordParamsMapperABC):
    """Word study params Source mapper."""

    _local_params_source: WordParamsLocaleSourceABC

    @override
    def subscribe(self, observer: WordParamsNotifyABC) -> None:
        """Subscribe observer to Word params source notifications."""
        self._local_params_source.add_observer(observer)

    @override
    def unsubscribe(self, observer: WordParamsNotifyABC) -> None:
        """Unsubscribe observer to Word params source notifications."""
        self._local_params_source.remove_observer(observer)
