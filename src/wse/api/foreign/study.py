"""Abstract base classes for Foreign discipline API."""

import logging
from dataclasses import asdict, dataclass
from json.decoder import JSONDecodeError

from injector import inject

from wse.api.foreign import requests, schemas
from wse.config.api import APIConfigV1
from wse.core.http import auth_schema, client

from . import WordStudyPresentationApiABC
from .responses import WordStudyPresentationResponse

log = logging.getLogger(__name__)
audit = logging.getLogger('audit')


@inject
@dataclass
class WordStudyPresentationApi(WordStudyPresentationApiABC):
    """Word study presentation API."""

    _http_client: client.HttpClient
    _auth_scheme: auth_schema.AuthSchema
    _api_config: APIConfigV1

    def fetch_presentation(
        self,
        payload: requests.SelectedParameters,
    ) -> schemas.PresentationCase:
        """Fetch presentation."""
        response = self._http_client.post(
            url=self._api_config.word_presentation,
            auth=self._auth_scheme,
            json=asdict(payload),
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
