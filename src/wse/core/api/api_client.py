"""API client."""

import logging
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import httpx

from wse.core.api.exceptions import APIError
from wse.core.config import Settings
from wse.interfaces.iapi import IApiClient

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s -%(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


class ApiClient(IApiClient):
    """API client."""

    def __init__(
        self,
        settings: Settings,
    ) -> None:
        """Construct the client."""
        self.settings = settings
        self._access_token: Optional[str] = None

    async def _request(
        self,
        method: str,
        endpoint: str,
        **kwargs: Dict[str, Any],
    ) -> httpx.Response:
        """Send an HTTP request to the API."""
        url = urljoin(self.settings.api_config.base_url, endpoint)
        timeout = self.settings.api_config.request_timeout
        headers: Dict = kwargs.get('headers', {})

        if self._access_token:
            headers['Authorization'] = f'Token {self._access_token}'

        try:
            async with httpx.AsyncClient(timeout=timeout) as client:
                response = await client.request(
                    method,
                    url,
                    headers=headers,
                    **kwargs,
                )
                response.raise_for_status()
                return response

        except httpx.HTTPStatusError as e:
            logger.error(f'HTTP error {e.response.status_code}: {e}')
            if e.response.status_code == 401:
                await self._handle_unauthorized_error(e)
            raise APIError(f'API request failed: {e}') from e

        except httpx.RequestError as e:
            logger.error(f'Request error: {e}')
            raise APIError(f'API request failed: {e}') from e

    async def _handle_unauthorized_error(
        self,
        error: httpx.HTTPStatusError,
    ) -> None:
        """Handle 401 Unauthorized errors."""
        logger.info('Attempting token refresh due to 401 error')
        ...
