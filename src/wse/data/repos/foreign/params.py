"""Word study params repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.api.foreign import requests
from wse.data.sources import foreign as source

from . import WordParamsMapperABC, WordParamsRepoABC


@inject
@dataclass
class WordParamsRepo(
    WordParamsRepoABC,
):
    """Word study params repository."""

    _network_source: source.WordParamsNetworkSourceABC
    _local_source: source.WordParamsLocaleSourceABC

    @override
    def fetch_params(self) -> None:
        """Set available params, default for Word study params."""
        data = self._network_source.fetch_params()
        self._local_source.set_initial_params(data)

    @override
    def get_params(self) -> requests.InitialParams:
        """Get Word study presentation params."""
        return self._local_source.get_params()

    @override
    def update_params(self, data: requests.InitialParams) -> None:
        """Update Word study presentation params."""
        try:
            updated_data = self._network_source.save_initial_params(data)
        except Exception:
            # TODO: Add log, user message
            self._local_source.update_initial_params(data)
        else:
            self._local_source.update_initial_params(updated_data)


@inject
@dataclass
class WordParamsMapper(WordParamsMapperABC):
    """Word study params Source mapper."""

    _local_params_source: source.WordParamsLocaleSourceABC

    @override
    def subscribe(self, observer: source.WordParamsNotifyABC) -> None:
        """Subscribe observer to Word params source notifications."""
        self._local_params_source.add_observer(observer)

    @override
    def unsubscribe(self, observer: source.WordParamsNotifyABC) -> None:
        """Unsubscribe observer to Word params source notifications."""
        self._local_params_source.remove_observer(observer)
