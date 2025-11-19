"""Word study params repository."""

from dataclasses import dataclass, fields
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

    def _convert_schema(
        self,
        schema: schemas.PresentationParams,
    ) -> requests.PresentationParamsDTO:
        """Convert Word study Presentation params schema to DTO."""
        # Convert a schema, including nested schemas,
        # into a dictionary.
        data = schema.to_dict()

        # `PresentationParamsDTO` is a derived class from
        # `InitialParams`, `ParamsChoice`, `Settings`,
        # and therefore contains fields of the same name.
        value_fields = [f.name for f in fields(requests.InitialParams)]
        choice_fields = [f.name for f in fields(requests.ParamsChoice)]
        setting_fields = [f.name for f in fields(requests.Settings)]

        values = {field: data.get(field) for field in value_fields}
        choices = {
            field: [requests.IdName(**item) for item in data[field]]
            for field in choice_fields
        }
        settings = {field: data.get(field) for field in setting_fields}

        return requests.PresentationParamsDTO(
            **values,  # type: ignore[arg-type]
            **choices,  # type: ignore[arg-type]
            **settings,  # type: ignore[arg-type]
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
