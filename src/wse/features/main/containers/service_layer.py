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
        api_client: ApiClient,
        subject: Subject | None = None,
        context: Context | None = None,
    ) -> None:
        """Construct the service layer."""
        self._api_client = api_client
        self._subject = subject if subject is not None else Subject()
        self._context = context if context is not None else Context()

    def _get_data(self) -> httpx.Response:
        response = self._api_client.get(self.user_data_path)
        return response

    def _get_text(self) -> None:
        response = self._get_data()
        logger.info(f'Gets response data: {response = }')

    def get_response_data(self) -> None:
        """Get response data."""
        self._get_text()
