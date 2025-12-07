"""Word study progress repo."""

from typing import TypedDict

from injector import inject

from wse.api.foreign import UpdateProgressPayload, WordProgressApiABC

from . import WordStudyProgressNetworkSourceABC


class PayloadType(TypedDict):
    """Payload typed dict."""

    case_uuid: str
    is_known: bool


class WordStudyProgressNetworkSource(WordStudyProgressNetworkSourceABC):
    """Word study progress Network Source."""

    @inject
    def __init__(self, api_client: WordProgressApiABC) -> None:
        """Construct the source."""
        self._api_client = api_client

    def increment_progress(self, case_uuid: str) -> None:
        """Increment Word study progress."""
        payload: UpdateProgressPayload = {
            'case_uuid': case_uuid,
            'is_known': True,
        }
        self._api_client.update(payload)

    def decrement_progress(self, case_uuid: str) -> None:
        """Decrement Word study progress."""
        payload: UpdateProgressPayload = {
            'case_uuid': case_uuid,
            'is_known': False,
        }
        """Decrement Word study progress."""
        self._api_client.update(payload)
