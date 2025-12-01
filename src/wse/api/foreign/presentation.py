"""Abstract base classes for Foreign discipline API client."""

import logging
from dataclasses import dataclass
from json.decoder import JSONDecodeError
from typing import override

from injector import inject

from wse.config.api import APIConfigV1
from wse.core.http import auth_schema, client
from wse.data.schemas import foreign as schemas

from . import WordPresentationApiABC
from .responses import WordStudyPresentationResponse

log = logging.getLogger(__name__)


@inject
@dataclass
class WordPresentationApi(WordPresentationApiABC):
    """Word study presentation API client."""

    _http_client: client.HttpClient
    _auth_scheme: auth_schema.AuthSchema
    _api_config: APIConfigV1

    @override
    def fetch(
        self,
        payload: schemas.RequestPresentation,
    ) -> schemas.PresentationCase:
        """Fetch Word study presentation."""
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
