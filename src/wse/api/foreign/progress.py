"""Word study progress API client."""

from injector import inject

from wse.config.api import APIConfigV1
from wse.core.http import HttpClientABC

from . import WordStudyProgressApiABC


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
        api_config: APIConfigV1,
    ) -> None:
        """Construct the api."""
        self._http_client = http_client
        self._api_config = api_config

    def increment_progress(self) -> None:
        """Send API request to increment Word study progress."""
        self._http_client.post(self._api_config.word_progress_update)

    def decrement_progress(self) -> None:
        """Send API request to decrement Word study progress."""
        self._http_client.post(self._api_config.word_progress_update)
