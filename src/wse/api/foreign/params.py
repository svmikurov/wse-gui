"""Word study params API client."""

import logging
from json.decoder import JSONDecodeError

import httpx
from injector import inject

from wse.config.api import APIConfigV1
from wse.core.http.auth_schema import AuthSchema
from wse.data.sources.foreign import schemas

from . import WordParamsApiABC, responses

log = logging.getLogger(__name__)
audit = logging.getLogger('audit')


class WordParamsApi(WordParamsApiABC):
    """Word study params API client."""

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        auth_scheme: AuthSchema,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the API."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme
        self._api_config = api_config

    def fetch_initial_params(
        self,
    ) -> schemas.ParamsChoices:
        """Fetch presentation."""
        try:
            response = self._http_client.get(
                url=self._api_config.word_params,
                auth=self._auth_scheme,
            )
            response.raise_for_status()

        except httpx.ConnectError:
            log.error('Server connect error')
            raise

        except httpx.HTTPError:
            log.error('Request Word study presentation HTTP error')
            raise

        try:
            audit.info(f'Got response json data:\n{response.json()}')
            return responses.WordStudyParamsResponse(**response.json()).data

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
