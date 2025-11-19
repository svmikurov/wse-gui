"""HTTP client."""

import json
import logging
from typing import Any, Literal, override

import httpx
from injector import inject

from wse.config.api import APIConfigV1

from .abc import AuthSchemaABC, HttpClientABC

log = logging.getLogger(__name__)
audit = logging.getLogger('audit')


class HttpClient(HttpClientABC):
    """Http client.

    Do not use for sensitive data, may log it.
    """

    @inject
    def __init__(
        self,
        http_client: httpx.Client,
        api_config: APIConfigV1,
    ) -> None:
        """Construct the client."""
        self._http_client = http_client
        self._http_client.base_url = api_config.base_url

    def _request(
        self,
        method: Literal['get', 'post', 'patch', 'put'],
        url: httpx.URL | str,
        auth: AuthSchemaABC | None,
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

        except httpx.HTTPStatusError as exc:
            self._handle_http_status_error(exc, json)
            raise

        except httpx.ConnectError as exc:
            log.error(f'Error connecting to {exc.request.url}')
            raise

        except httpx.HTTPError as exc:
            log.error(f'HTTP Exception for {exc.request.url} - {exc}')
            raise

        except TypeError as exc:
            log.error(f'Send request error: {exc}.\nRequest payload: {json}')
            raise

        self._audit_request(url, json)
        self._audit_response(response)
        return response

    # HTTP methods
    # ------------

    @override
    def get(
        self,
        url: httpx.URL | str,
        auth: AuthSchemaABC | None = None,
    ) -> httpx.Response:
        """Send a GET request."""
        return self._request('get', url, auth=auth)

    @override
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: AuthSchemaABC | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a POST request."""
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
        auth: AuthSchemaABC | None = None,
    ) -> httpx.Response:
        """Send a PATCH request."""
        return self._request('patch', url, json=json, auth=auth)

    @override
    def put(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: AuthSchemaABC | None = None,
    ) -> httpx.Response:
        """Send a PUT request."""
        return self._request('put', url, json=json, auth=auth)

    # Error handling
    # --------------

    @staticmethod
    def _handle_http_status_error(
        exc: httpx.HTTPStatusError,
        json_data: dict[str, Any] | None,
    ) -> None:
        response = exc.response
        status = response.status_code
        reason = response.reason_phrase

        try:
            response_data: dict[str, Any] = response.json()
        except json.JSONDecodeError:
            response_data = {}

        log.error(
            f'HTTP status error {status} for {exc.request.url} - {reason}\n'
            f'with request data {json_data!r}\n'
            f'got response_data {response_data!r}'
        )

    # Utility methods
    # ---------------

    @staticmethod
    def _audit_request(
        url: httpx.URL | str,
        json: dict[str, Any] | None,
    ) -> None:
        data = json or {}
        audit.info("Sent request to '%s' with payload: %r", url, data)

    @staticmethod
    def _audit_response(response: httpx.Response) -> None:
        try:
            audit.info(f'Got response payload: {response.json()}')
        except json.JSONDecodeError:
            audit.info(
                'Got response without payload, code: {response.status_code}'
            )
        pass
