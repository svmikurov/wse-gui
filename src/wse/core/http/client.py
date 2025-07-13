"""Defines HTTP client."""

import logging
from typing import Any

import httpx
from injector import inject

from wse.config.settings import APIConfigV1
from wse.core.interfaces.iapi import IHttpClient

logger = logging.getLogger(__name__)


class HttpClient(IHttpClient):
    """Http client."""

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        self._http_client.base_url = api_config.base_url

    def get(
        self,
        url: httpx.URL | str,
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""
        return self._request('post', url, auth=auth)

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
            r = self._http_client.request(
                method,
                url,
                json=json,
                auth=auth,
                headers=headers,
            )
            r.raise_for_status()
            return r

        except httpx.HTTPStatusError as e:
            logger.error(f'HTTP error {e.response.status_code}: {e}')
            raise e
