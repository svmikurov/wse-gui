"""Word study parameters Source."""

import logging
from dataclasses import asdict, dataclass, replace
from typing import override

from injector import inject

from wse.api.foreign import WordParametersApiABC
from wse.data.dto import foreign as dto
from wse.data.schemas import foreign as schemas
from wse.data.sources import foreign as base
from wse.feature.observer import mixins as observer

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class WordParametersData(
    dto.PresentationParameters,
):
    """Word study parameters Source data."""


@inject
@dataclass
class WordParametersNetworkSource(
    base.WordParametersNetworkSourceABC,
):
    """Word study parameters Network source."""

    _api_client: WordParametersApiABC

    @override
    def fetch(self) -> dto.PresentationParameters:
        """Fetch Word study parameters."""
        try:
            schema = self._api_client.fetch()
        except Exception:
            log.error('Fetch Word study parameters error')
            raise

        return schema.to_dto()

    @override
    def save(
        self,
        data: dto.InitialParameters,
    ) -> dto.PresentationParameters:
        """Save Word study parameters."""
        try:
            schema = schemas.InitialParameters(**asdict(data))
        except Exception:
            log.error('Save parameters validation error')
            raise

        try:
            updated = self._api_client.save(schema)
        except Exception:
            log.error('Update parameters api client error')
            raise

        return updated.to_dto()


@inject
@dataclass
class WordParametersLocaleSource(
    observer.ObserverManagerGen[base.WordParametersNotifyABC],
    observer.NotifyGen[base.ParamsNotifyT],
    base.WordParametersLocaleSourceABC,
):
    """Word study parameters Network source."""

    _data: WordParametersData

    @override
    def update(
        self,
        data: dto.PresentationParameters | dto.InitialParameters,
    ) -> None:
        """Update parameters."""
        self._update(data)
        self.notify('params_updated', params=self._data)

    @override
    def set_initial(
        self,
        data: dto.InitialParameters,
    ) -> None:
        """Set initial parameters."""
        self._update(data)

    @override
    def get_initial(self) -> dto.InitialParameters:
        """Get initial parameters."""
        return self._data.initial

    @override
    def refresh_initial(self) -> None:
        """Refresh observers data with initial parameters."""
        self.notify('initial_updated', params=self._data.initial)

    def _update(
        self,
        from_dto: dto.PresentationParameters | dto.InitialParameters,
    ) -> None:
        """Update source data."""
        self._data = replace(self._data, **vars(from_dto))
