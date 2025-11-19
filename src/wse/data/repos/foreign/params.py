"""Word study params repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.api.foreign import requests, schemas
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
        schema = self._network_params_source.fetch_initial_params()
        data = self._convert_schema(schema)
        self._local_params_source.set_initial_params(data)

    @override
    def get_params(self) -> requests.InitialParams:
        """Get Word study presentation params."""
        return self._local_params_source.get_params()

    @override
    def save_params(self, data: requests.InitialParams) -> None:
        """Save Word study presentation params."""
        self._local_params_source.update_initial_params(data)
        self._network_params_source.save_initial_params(data)

    # Helpers
    # -------

    # TODO: Refactor
    def _convert_schema(
        self,
        schema: schemas.PresentationParams,
    ) -> requests.InitialParams:
        """Convert Word study Presentation params schema to DTO."""
        data = schema.to_dict()
        return requests.PresentationParamsDTO(
            # Values
            category=data.get('category'),
            label=data.get('label'),
            word_source=data.get('word_source'),
            order=data.get('order'),
            start_period=data.get('start_period'),
            end_period=data.get('end_period'),
            # Choices
            categories=[
                requests.IdName(**items)
                for items in data.get('categories', [])
            ],
            labels=[
                requests.IdName(**items) for items in data.get('labels', [])
            ],
        )


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
