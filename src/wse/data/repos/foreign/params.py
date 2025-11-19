"""Word study params repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.api.foreign import schemas
from wse.data.sources import foreign as sources

from . import WordParamsMapperABC, WordParamsRepoABC


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
        data = self._network_params_source.fetch_initial_params()
        self._local_params_source.set_initial_params(data)

    @override
    def get_params(self) -> schemas.PresentationParams:
        """Get Word study presentation params."""
        return self._local_params_source.get_params()

    @override
    def save_params(self, data: object) -> None:
        """Save Word study presentation params."""
        self._local_params_source.update_initial_params(data)
        self._network_params_source.save_initial_params(data)


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
