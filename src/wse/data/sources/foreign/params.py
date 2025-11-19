"""Word study params Source."""

import logging
from dataclasses import asdict, dataclass, field, replace
from decimal import Decimal
from typing import override

from injector import inject

from wse.api.foreign import WordParamsApiABC, requests, schemas
from wse.data.sources import foreign as base
from wse.feature.observer.mixins import NotifyGen, ObserverManagerGen
from wse.utils import decorators

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class WordParamsData:
    """Word params data."""

    categories: list[requests.IdName] = field(default_factory=list)
    labels: list[requests.IdName] = field(default_factory=list)

    category: requests.IdName | None = None
    label: requests.IdName | None = None
    word_source: requests.IdName | None = None
    order: requests.IdName | None = None
    start_period: requests.IdName | None = None
    end_period: requests.IdName | None = None

    word_count: Decimal | int | None = None
    question_timeout: Decimal | float | None = None
    answer_timeout: Decimal | float | None = None


@inject
@dataclass
class WordParamsNetworkSource(base.WordParamsNetworkSourceABC):
    """Word study params Network source."""

    _api_client: WordParamsApiABC

    @override
    def fetch_initial_params(self) -> schemas.PresentationParams:
        """Fetch Word study initial params."""
        params = self._api_client.fetch_initial_params()
        return params

    # TODO: Fix static types.
    @override
    def save_initial_params(self, data: requests.InitialParams) -> bool:
        """Save Word study initial params."""
        try:
            self._api_client.save_initial_params(data)

        except Exception:
            log.error('Initial Word study params not updated')
            return False

        else:
            return True


@inject
@dataclass
class WordParamsLocaleSource(
    ObserverManagerGen[base.WordParamsNotifyABC],
    NotifyGen[base.ParamsNotifyT],
    base.WordParamsLocaleSourceABC,
):
    """Word study params Network source."""

    _data: WordParamsData

    # TODO: Update `schemas.ParamsSchema` to `dataclass` DTO?
    @override
    def set_initial_params(self, data: requests.InitialParams) -> None:
        """Set Word study initial data."""
        self._data = replace(self._data, **asdict(data))
        self.notify('initial_params_updated', params=data)

    @override
    def get_params(self) -> requests.InitialParams:
        """Get Word study Presentation params."""
        return requests.InitialParams(
            category=(self._data.category or self._data.category),
            label=(self._data.label or self._data.label),
        )

    @decorators.log_unimplemented_call
    @override
    def update_initial_params(self, data: object) -> None:
        """Save initial Word study params."""
