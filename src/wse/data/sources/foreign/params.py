"""Word study params Source."""

import logging
from dataclasses import dataclass, replace
from typing import override

from injector import inject

from wse.api.foreign import WordParamsApiABC
from wse.api.schemas.base import IdNameSchema
from wse.data.sources import foreign as base
from wse.feature.observer.mixins import NotifyGen, ObserverManagerGen
from wse.utils import decorators

from . import schemas

log = logging.getLogger(__name__)


@dataclass(frozen=True)
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
class WordParamsNetworkSource(base.WordParamsNetworkSourceABC):
    """Word study params Network source."""

    _api_client: WordParamsApiABC

    @override
    def fetch_initial_params(self) -> schemas.ParamsSchema:
        """Fetch Word study initial params."""
        params = self._api_client.fetch_initial_params()
        return params

    # TODO: Fix static types.
    @override
    def save_initial_params(self, data: object) -> bool:
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

    @override
    def set_initial_params(self, data: schemas.ParamsChoices) -> None:
        """Set Word study initial data."""
        self._data = replace(self._data, **data.to_dict())
        updated_params = {k: v for k, v in self._data.__dict__.items()}
        updated_schema = schemas.ParamsChoices.from_dict(updated_params)
        self.notify('initial_params_updated', params=updated_schema)

    @override
    def get_params(self) -> schemas.PresentationParams:
        """Get Word study Presentation params."""
        return schemas.PresentationParams(
            category=(
                self._data.selected_category or self._data.default_category
            ),
            label=(self._data.selected_label or self._data.default_label),
        )

    @decorators.log_unimplemented_call
    @override
    def update_initial_params(self, data: object) -> None:
        """Save initial Word study params."""
