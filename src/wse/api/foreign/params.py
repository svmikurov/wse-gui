"""Word study params API client."""

import logging
from dataclasses import asdict, dataclass
from json.decoder import JSONDecodeError
from typing import override

from injector import inject

from wse.api.foreign import schemas
from wse.config.api import APIConfigV1
from wse.core.http import HttpClientABC, auth_schema

from . import WordParamsApiABC, requests, responses

log = logging.getLogger(__name__)


@inject
@dataclass
class WordParamsApi(WordParamsApiABC):
    """Word study params API client."""

    _http_client: HttpClientABC
    _auth_scheme: auth_schema.AuthSchema
    _api_config: APIConfigV1

    @override
    def fetch_params(
        self,
    ) -> schemas.PresentationParams:
        """Fetch presentation."""
        try:
            response = self._http_client.get(
                url=self._api_config.word_params,
                auth=self._auth_scheme,
            )
            response.raise_for_status()

        except Exception:
            log.error('Request Word study params HTTP error')
            raise

        try:
            response_schema = responses.WordStudyParamsResponse(
                **response.json()
            )

        except JSONDecodeError:
            log.error(
                'Request Word study params error: '
                'response does not contains JSON data\n'
            )
            raise

        except ValueError as err:
            log.error(
                f'Word study params response validate error:\n'
                f'{str(err)}\n'
                f'Got response JSON: {response.json()}'
            )
            raise

        return response_schema.data

    # TODO: Add exception handling, fix type ignore
    @override
    def save_initial_params(
        self,
        data: requests.InitialParams,
    ) -> None:
        """Save Word study params."""
        try:
            response = self._http_client.put(
                url=self._api_config.word_params_update,
                auth=self._auth_scheme,
                json=asdict(data),
            )
            response.raise_for_status()

        except Exception:
            log.error('Initial Word study params not updated')
            raise
