"""Defines HTTP client."""

import logging
from typing import Any

import httpx
from injector import inject
from typing_extensions import override

from wse.config.api import APIConfigV1

from .base import HttpClientABC
from .protocol import AuthSchemaProto

log = logging.getLogger(__name__)
audit = logging.getLogger('audit')


class HttpClient(HttpClientABC):
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
        auth: AuthSchemaProto | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""
        return self._request('get', url, auth=auth)

    @override
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: AuthSchemaProto | None = None,
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
        auth: AuthSchemaProto | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""
        return self._request('patch', url, json=json, auth=auth)

    @override
    def _request(
        self,
        method: str,
        url: httpx.URL | str,
        auth: AuthSchemaProto | None,
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

        except httpx.ConnectError as err:
            log.error('Error connecting to server %s', err.request.url)
            raise

        except httpx.HTTPStatusError as err:
            log.error(f'HTTP error {err.response.status_code}')
            raise

        else:
            return response
