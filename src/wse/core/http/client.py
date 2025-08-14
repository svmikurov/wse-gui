"""Defines HTTP client."""

import logging
from typing import Any

import httpx
from injector import inject
from typing_extensions import override

from wse.config.settings import APIConfigV1

from ..interfaces.iapi import IAuthScheme
from ._iabc.client import BaseHttpClient

logger = logging.getLogger(__name__)


class HttpClient(BaseHttpClient):
    """Http client."""

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        # Set base url to client
        self._http_client.base_url = api_config.base_url

    @override
    def get(
        self,
        url: httpx.URL | str,
        auth: IAuthScheme | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""
        return self._request('get', url, auth=auth)

    @override
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: IAuthScheme | None = None,
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
        auth: IAuthScheme | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""
        return self._request('patch', url, json=json, auth=auth)

    def _request(
        self,
        method: str,
        url: httpx.URL | str,
        auth: IAuthScheme | None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        try:
            response = self._http_client.request(
                method,
                url,
                json=json,
                auth=auth,  # type: ignore[arg-type]
                headers=headers,
            )
            response.raise_for_status()

        except httpx.ConnectError:
            logger.error('Error connecting to server')
            raise

        except httpx.HTTPStatusError as e:
            logger.error(f'HTTP error {e.response.status_code}: {e}')
            raise

        except Exception as e:
            logger.error(f'Unexpected error: {e}')
            raise

        else:
            return response
