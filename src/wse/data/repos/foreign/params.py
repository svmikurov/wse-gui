"""Word study params repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.sources import foreign as sources
from wse.data.sources.foreign import schemas

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

    _network_params_source: sources.WordParamsNetworkSourceABC
    _local_params_source: sources.WordParamsLocaleSourceABC

    @override
    def refresh_initial_params(self) -> None:
        """Set available params, default for Word study params."""
        params = self._network_params_source.fetch_initial_params()
        self._local_params_source.set_initial_params(params)

    def get_params(self) -> schemas.PresentationParams:
        """Get Word study presentation params."""
        return self._local_params_source.get_params()


@inject
@dataclass
class WordParamsMapper(WordParamsMapperABC):
    """Word study params Source mapper."""

    _local_params_source: sources.WordParamsLocaleSourceABC

    @override
    def subscribe(self, observer: sources.WordParamsNotifyABC) -> None:
        """Subscribe observer to Word params source notifications."""
        self._local_params_source.add_observer(observer)

    @override
    def unsubscribe(self, observer: sources.WordParamsNotifyABC) -> None:
        """Unsubscribe observer to Word params source notifications."""
        self._local_params_source.remove_observer(observer)
