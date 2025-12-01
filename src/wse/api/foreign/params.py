"""Word study Parameters API client."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from json.decoder import JSONDecodeError
from typing import TYPE_CHECKING, override

from injector import inject

from wse.config.api import APIConfigV1
from wse.core.http import HttpClientABC, auth_schema
from wse.data.schemas import foreign

from . import WordParametersApiABC, responses

if TYPE_CHECKING:
    import httpx

log = logging.getLogger(__name__)


@inject
@dataclass
class WordParametersApi(WordParametersApiABC):
    """Word study parameters API client."""

    _http_client: HttpClientABC
    _auth_scheme: auth_schema.AuthSchema
    _api_config: APIConfigV1

    @override
    def fetch(self) -> foreign.PresentationParameters:
        """Fetch Word study parameters."""
        try:
            response = self._http_client.get(
                url=self._api_config.word_params,
                auth=self._auth_scheme,
            )
            response.raise_for_status()

        except Exception:
            log.error('Request Word study parameters HTTP error')
            raise

        schema = self._validate_response(response)
        return schema.data

    # TODO: Add exception handling
    @override
    def save(
        self,
        data: foreign.InitialParameters,
    ) -> foreign.PresentationParameters:
        """Save Word study parameters."""
        try:
            response = self._http_client.put(
                url=self._api_config.word_params_update,
                auth=self._auth_scheme,
                json=data.to_dict(),
            )
            response.raise_for_status()

        except Exception:
            log.exception('Initial Word study parameters not updated')
            raise

        schema = self._validate_response(response)
        return schema.data

    def _validate_response(
        self,
        response: httpx.Response,
    ) -> responses.WordStudyParametersResponse:
        try:
            return responses.WordStudyParametersResponse(**response.json())

        except JSONDecodeError:
            log.error(
                'Request Word study parameters error: '
                'response does not contains JSON data\n'
            )
            raise

        except ValueError as err:
            log.error(
                f'Word study parameters response validate error:\n'
                f'{str(err)}\n'
                f'Got response JSON: {response.json()}'
            )
            raise
