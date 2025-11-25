"""Word study params Source."""

import logging
from dataclasses import asdict, dataclass, field, fields, replace
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
    translation_orders: list[requests.CodeName] = field(default_factory=list)

    category: requests.IdName | None = None
    mark: requests.IdName | None = None
    word_source: requests.IdName | None = None
    translation_order: requests.CodeName | None = None
    start_period: requests.IdName | None = None
    end_period: requests.IdName | None = None

    word_count: int | None = None
    question_timeout: int | None = None
    answer_timeout: int | None = None


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

    @override
    def save_initial_params(self, data: requests.InitialParametersDTO) -> bool:
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
        # `SelectedParameters`, `ParameterOptions`, `SettingParameters`,
        # and therefore contains fields of the same name.
        initial_fields = [f.name for f in fields(requests.SelectedParameters)]
        options_fields = [f.name for f in fields(requests.ParameterOptions)]
        settings_fields = [f.name for f in fields(requests.SettingParameters)]

        initial: dict[str, requests.IdName | requests.CodeName] = {}
        for f in initial_fields:
            if schema_data.get(f) and 'id' in schema_data[f]:
                initial[f] = requests.IdName(**schema_data[f])
            elif schema_data.get(f) and 'code' in schema_data[f]:
                initial[f] = requests.CodeName(**schema_data[f])

        options: dict[
            str, list[requests.IdName] | list[requests.CodeName]
        ] = {}
        for f in options_fields:
            for item in schema_data[f]:
                if 'id' in item:
                    options[f] = [
                        requests.IdName(**item) for item in schema_data[f]
                    ]
                if 'code' in item:
                    options[f] = [
                        requests.CodeName(**item) for item in schema_data[f]
                    ]

        settings = {field: schema_data.get(field) for field in settings_fields}

        data = requests.PresentationParamsDTO(
            **initial,  # type: ignore[arg-type]
            **options,  # type: ignore[arg-type]
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
    def set_initial_params(self, data: requests.SelectedParameters) -> None:
        """Set Word study initial data."""
        self._data = replace(self._data, **asdict(data))
        self.notify('initial_params_updated', params=data)

    @override
    def get_params(self) -> requests.InitialParametersDTO:
        """Get Word study Presentation params."""
        return requests.InitialParametersDTO(
            category=(self._data.category or self._data.category),
            mark=(self._data.mark or self._data.mark),
        )

    @decorators.log_unimplemented_call
    @override
    def update_initial_params(self, data: object) -> None:
        """Save initial Word study params."""
