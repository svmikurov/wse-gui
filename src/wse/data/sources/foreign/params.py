"""Word study params Source."""

import logging
from dataclasses import asdict, dataclass, field, fields, replace
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
    marks: list[requests.IdName] = field(default_factory=list)
    sources: list[requests.IdName] = field(default_factory=list)
    periods: list[requests.IdName] = field(default_factory=list)

    category: requests.IdName | None = None
    mark: requests.IdName | None = None
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
    def fetch_params(self) -> requests.PresentationParamsDTO:
        """Fetch Word study params."""
        try:
            schema = self._api_client.fetch_params()
        except Exception:
            log.error('Fetch Word study params error')
            raise

        data = self._convert_schema(schema)
        return data

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

    # Helpers
    # -------

    def _convert_schema(
        self,
        schema: schemas.PresentationParams,
    ) -> requests.PresentationParamsDTO:
        """Convert Word study Presentation params schema to DTO."""
        # Convert a schema, including nested schemas,
        # into a dictionary.
        schema_data = schema.to_dict()

        # `PresentationParamsDTO` is a derived class from
        # `InitialParams`, `ParamsChoice`, `Settings`,
        # and therefore contains fields of the same name.
        initial_fields = [f.name for f in fields(requests.InitialParams)]
        choices_fields = [f.name for f in fields(requests.ParamsChoices)]
        settings_fields = [f.name for f in fields(requests.Settings)]

        initial = {
            field: requests.IdName(**schema_data[field])
            if schema_data.get(field)
            else None
            for field in initial_fields
        }
        choices = {
            field: [requests.IdName(**item) for item in schema_data[field]]
            for field in choices_fields
        }
        settings = {field: schema_data.get(field) for field in settings_fields}

        data = requests.PresentationParamsDTO(
            **initial,  # type: ignore[arg-type]
            **choices,  # type: ignore[arg-type]
            **settings,  # type: ignore[arg-type]
        )
        return data


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
            mark=(self._data.mark or self._data.mark),
        )

    @decorators.log_unimplemented_call
    @override
    def update_initial_params(self, data: object) -> None:
        """Save initial Word study params."""
