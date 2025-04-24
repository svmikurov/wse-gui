"""Defines Practice page model."""

import logging

import httpx

from wse.core.api.client import ApiClient
from wse.features.base.mvc import BaseModel

logger = logging.getLogger(__name__)


class ServiceLayer:
    """Encapsulates the logic for receiving and preparing data."""

    user_data_path = '/api/v1/auth/users/me/'

    def __init__(self, api_client: ApiClient) -> None:
        """Construct the service layer."""
        self._api_client = api_client

    def _get_data(self) -> httpx.Response:
        response = self._api_client.get(self.user_data_path)
        return response

    def _get_text(self) -> None:
        response = self._get_data()
        logger.info(f'{response = }')

    def get_response_data(self) -> None:
        """Get response data."""
        self._get_text()


class PracticeModel(BaseModel):
    """Practice base model."""

    def _set_context(self) -> None:
        """Set view context for render into view."""

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""
