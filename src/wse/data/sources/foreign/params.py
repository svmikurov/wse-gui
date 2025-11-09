"""Word study params Source."""

from dataclasses import dataclass, replace
from typing import override

from injector import inject

from wse.api.foreign import WordParamsApiABC
from wse.feature.observer.mixins import NotifyGen, ObserverManagerGen

from . import (
    ParamsNotifyT,
    WordParamsLocaleSourceABC,
    WordParamsNetworkSourceABC,
    WordParamsNotifyABC,
)
from .schema import (
    IdNameSchema,
    WordParamsSchema,
)


@dataclass
class WordParamsData:
    """Word params data."""

    categories: list[IdNameSchema] | None = None
    labels: list[IdNameSchema] | None = None

    default_category: IdNameSchema | None = None
    default_label: IdNameSchema | None = None

    selected_category: IdNameSchema | None = None
    selected_label: IdNameSchema | None = None


@inject
@dataclass
class WordParamsNetworkSource(WordParamsNetworkSourceABC):
    """Word study params Network source."""

    _api_client: WordParamsApiABC

    @override
    def fetch_initial_params(self) -> WordParamsSchema:
        """Fetch Word study initial params."""
        params = self._api_client.fetch_initial_params()
        return params


@inject
@dataclass
class WordParamsLocaleSource(
    ObserverManagerGen[WordParamsNotifyABC],
    NotifyGen[ParamsNotifyT],
    WordParamsLocaleSourceABC,
):
    """Word study params Network source."""

    _data: WordParamsData

    @override
    def set_initial_params(self, params: WordParamsSchema) -> None:
        """Set Word study initial data."""
        self._data = replace(self._data, **params.to_dict())
        updated_params = {k: v for k, v in self._data.__dict__.items()}
        updated_schema = WordParamsSchema.from_dict(updated_params)
        self.notify('initial_params_updated', params=updated_schema)
