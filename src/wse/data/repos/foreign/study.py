"""Foreign word study repository."""

from dataclasses import dataclass
from typing import override

from injector import inject

from wse.api.foreign import requests, schemas
from wse.data.repos import foreign as repos
from wse.data.sources import foreign as source


@inject
@dataclass
class WordStudyRepo(repos.WordStudyRepoABC):
    """Word study repository."""

    _locale_source: source.WordStudyLocaleSourceABC
    _network_source: source.WordStudyNetworkSourceABC
    _params_repo: repos.WordParamsRepoABC

    @override
    def get_word(self) -> schemas.PresentationSchema:
        """Get word to study."""
        params = self._get_params()

        try:
            case = self._network_source.fetch_presentation(params)
        except Exception:
            raise
        self._locale_source.set_case(case)
        return self._locale_source.get_presentation_data()

    def _get_params(self) -> requests.InitialParametersDTO:
        params = self._params_repo.get_params()
        return params
