"""Word study progress repo."""

from injector import inject

from wse.api.foreign import WordProgressApiABC

from . import WordStudyProgressNetworkSourceABC


class WordStudyProgressNetworkSource(WordStudyProgressNetworkSourceABC):
    """Word study progress Network Source."""

    @inject
    def __init__(self, api_client: WordProgressApiABC) -> None:
        """Construct the source."""
        self._api_client = api_client

    def increment_progress(self, case_uuid: str) -> None:
        """Increment Word study progress."""
        self._api_client.increment_progress(case_uuid)

    def decrement_progress(self, case_uuid: str) -> None:
        """Decrement Word study progress."""
        self._api_client.decrement_progress(case_uuid)
