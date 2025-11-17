"""Word study progress API client."""

import logging
from typing import TypedDict

import httpx
from injector import inject

from wse.config.api import APIConfigV1
from wse.core.http import HttpClientABC
from wse.core.http.auth_schema import AuthSchema

from . import WordStudyProgressApiABC

log = logging.getLogger(__name__)


class PayloadType(TypedDict):
    """Payload typed dict."""

    case_uuid: str
    progress_type: str


class WordStudyProgressApi(WordStudyProgressApiABC):
    """Word study progress API."""

    # TODO: Fix double access to api config?
    # Access:
    #  - api config injection into http client constructor
    #  - api config injection into `WordStudyProgressApi` constructor

    @inject
    def __init__(
        self,
        http_client: HttpClientABC,
        auth_scheme: AuthSchema,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the api."""
        self._http_client = http_client
        self._auth = auth_scheme
        self._api_config = api_config

    def increment_progress(self, case_uuid: str) -> None:
        """Send API request to increment Word study progress."""
        payload: PayloadType = {
            'case_uuid': case_uuid,
            'progress_type': 'known',
        }
        self._update_progress(payload)

    def decrement_progress(self, case_uuid: str) -> None:
        """Send API request to decrement Word study progress."""
        payload: PayloadType = {
            'case_uuid': case_uuid,
            'progress_type': 'unknown',
        }
        self._update_progress(payload)

    def _update_progress(self, payload: PayloadType) -> None:
        try:
            self._http_client.post(
                self._api_config.word_progress_update,
                json=dict(payload),
                auth=self._auth,
            )
        except httpx.HTTPStatusError as exc:
            log.error(
                f'Word study progress update HTTP client error: '
                f'{str(exc.response.reason_phrase)}'
            )
        except Exception as exc:
            log.error('Word study progress update unexpected error:\n%s', exc)
