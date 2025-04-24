"""Provides a client for making API requests."""

from urllib.parse import urljoin

import httpx
from httpx import Response

from wse.core.auth.service import AuthService


class ApiClient:
    """Manages authentication-related API requests by method."""

    def __init__(self, auth_service: AuthService, base_url: str) -> None:
        """Construct the client."""
        self._auth_service = auth_service
        self._base_url = base_url
        self._client = httpx.Client()

    def request(self,
        method: str,
        endpoint: str,
        **kwargs: dict[str | str],
    ) -> Response:
        """Request by method."""
        # Request method of httpx.Client
        request_method = getattr(self._client, method)
        # Url
        url = urljoin(self._base_url, endpoint)
        # Token
        token = self._auth_service.get_token()
        headers = kwargs.get('headers', {})
        headers['Authorization'] = f'Token {token}'
        # Request
        return request_method(url, headers=headers, **kwargs)

    def get(self, endpoint: str, **kwargs: dict[str | str]) -> Response:
        """Send a GET request to the specified endpoint."""
        return self.request('get', endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: dict[str | str]) -> Response:
        """Send a POST request to the specified endpoint."""
        return self.request('post', endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: dict[str | str]) -> Response:
        """Send a PUT request to the specified endpoint."""
        return self.request('put', endpoint, **kwargs)

    def patch(self, endpoint: str, **kwargs: dict[str | str]) -> Response:
        """Send a PATCH request to the specified endpoint."""
        return self.request('patch', endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: dict[str | str]) -> Response:
        """Send a DELETE request to the specified endpoint."""
        return self.request('delete', endpoint, **kwargs)
