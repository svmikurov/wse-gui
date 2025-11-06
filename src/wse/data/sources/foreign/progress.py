"""Word study progress repo."""

import uuid

from injector import inject

from wse.api.foreign import WordStudyProgressApiABC

from . import WordStudyProgressNetworkSourceABC


class WordStudyProgressNetworkSource(WordStudyProgressNetworkSourceABC):
    """Word study progress Network Source."""

    @inject
    def __init__(self, api_client: WordStudyProgressApiABC) -> None:
        """Construct the source."""
        self._api_client = api_client

    def increment_progress(self, case_uuid: uuid.UUID) -> None:
        """Increment Word study progress."""
        self._api_client.increment_progress(case_uuid)

    def decrement_progress(self, case_uuid: uuid.UUID) -> None:
        """Decrement Word study progress."""
        self._api_client.decrement_progress(case_uuid)
