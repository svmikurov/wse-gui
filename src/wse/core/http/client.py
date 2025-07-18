"""Defines HTTP client."""

import logging
from typing import Any

import httpx
from injector import inject
from typing_extensions import override

from wse.config.settings import APIConfigV1

from ._iabc.client import BaseHttpClient
from ._iabc.inspector import IAccountStateInspector

logger = logging.getLogger(__name__)


class HttpClient(BaseHttpClient):
    """Http client."""

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        api_config: APIConfigV1,
        account_state_inspector: IAccountStateInspector,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        self._http_client.base_url = api_config.base_url
        self._account_state_inspector = account_state_inspector

    @override
    def get(
        self,
        url: httpx.URL | str,
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""
        return self._request('post', url, auth=auth)

    @override
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: httpx.Auth | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""
        return self._request(
            'post',
            url,
            json=json,
            auth=auth,
            headers=headers,
        )

    @override
    def patch(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""
        return self._request('patch', url, json=json, auth=auth)

    def _request(
        self,
        method: str,
        url: httpx.URL | str,
        auth: httpx.Auth | None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        try:
            response = self._http_client.request(
                method,
                url,
                json=json,
                auth=auth,
                headers=headers,
            )
            response.raise_for_status()

        except httpx.HTTPStatusError as e:
            logger.error(f'HTTP error {e.response.status_code}: {e}')
            raise

        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            raise

        else:
            self._inspect_account_state(response.json())
            return response

    def _inspect_account_state(self, data: dict[str, Any]) -> None:
        """Inspect the account state."""
        self._account_state_inspector.inspect(data)
