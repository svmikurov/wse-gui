"""Defines practice model service layer."""

import logging

import httpx

from wse.core.api.client import ApiClient
from wse.features.base.context import Context
from wse.features.shared.observer import Subject

logger = logging.getLogger(__name__)


class ServiceLayer:
    """Encapsulates the logic for receiving and preparing data."""

    user_data_path: str = '/api/v1/auth/users/me/'

    def __init__(
        self,
        api_client: ApiClient | None = None,
        subject: Subject | None = None,
        context: Context | None = None,
    ) -> None:
        """Construct the service layer."""
        self._api_client = api_client
        self._subject = subject if subject is not None else Subject()
        self._context = context if context is not None else Context()

    @property
    def subject(self) -> Subject:
        """The observed object."""
        return self._subject

    # Info retrieve
    def request_http(self) -> httpx.Response:
        return self._api_client.get(self.user_data_path)

    # Prepare data
    def prepare_response(self) -> None:
        response = self.request_http()
        self._notify_display_panel(response.json())

    # Controller requests
    def request_text(self) -> None:
        """Get response data."""
        self.prepare_response()

    # Notifications
    def _notify_display_panel(self, text) -> None:
        self._subject.notify('display_on_panel', text=text)
