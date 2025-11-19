"""Abstract base classes for Foreign discipline API."""

import logging
from json.decoder import JSONDecodeError

from injector import inject

from wse.api.foreign import schemas
from wse.config.api import APIConfigV1
from wse.core.http import auth_schema, client

from . import WordStudyPresentationApiABC
from .responses import WordStudyPresentationResponse

log = logging.getLogger(__name__)
audit = logging.getLogger('audit')


class WordStudyPresentationApi(WordStudyPresentationApiABC):
    """Word study presentation API."""

    @inject
    def __init__(
        self,
        http_client: client.HttpClient,
        auth_scheme: auth_schema.AuthSchema,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the API."""
        self._http_client = http_client
        self._auth_scheme = auth_scheme
        self._api_config = api_config

    def fetch_presentation(
        self,
        payload: schemas.PresentationParams,
    ) -> schemas.PresentationCase:
        """Fetch presentation."""
        response = self._http_client.post(
            url=self._api_config.word_presentation,
            auth=self._auth_scheme,
            json=payload.to_dict(),
        )

        try:
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
