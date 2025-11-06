"""Abstract base classes for Foreign discipline API."""

import logging
from json.decoder import JSONDecodeError

import httpx
from injector import inject

from wse.config.api import APIConfigV1
from wse.core.http.auth_schema import AuthSchema
from wse.data.sources.foreign.schemas import (
    WordStudyCaseSchema,
    WordStudyPresentationParamsSchema,
)

from .abc import WordStudyPresentationApiABC
from .responses import WordStudyPresentationResponse

log = logging.getLogger(__name__)
audit = logging.getLogger('audit')


class WordStudyPresentationApi(WordStudyPresentationApiABC):
    """Word study presentation API."""

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

    def fetch_presentation(
        self,
        payload: WordStudyPresentationParamsSchema,
    ) -> WordStudyCaseSchema:
        """Fetch presentation."""
        try:
            response = self._http_client.post(
                url=self._api_config.word_presentation,
                auth=self._auth_scheme,
                json=payload.to_dict(),
            )
            response.raise_for_status()

        except httpx.ConnectError:
            log.error('Server connect error')
            raise

        except httpx.HTTPError as e:
            log.error(
                f'Request Word study case HTTP error:\n'
                f'{str(e)}\n{e.response.json()}'  # type: ignore[attr-defined]
            )
            raise

        try:
            audit.info(f'Got response json data:\n{response.json()}')
            return WordStudyPresentationResponse(**response.json()).data

        except JSONDecodeError:
            log.error(
                'Request Word study presentation error: '
                'response does not contains JSON data\n'
            )
            raise

        except ValueError as err:
            log.error(
                f'Word study presentation response validate error:\n'
                f'{str(err)}\n'
                f'Got response JSON: {response.json()}'
            )
            raise
