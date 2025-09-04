"""Defines protocol for HTTP client interface."""

from typing import Any, AsyncGenerator, Generator, Protocol

import httpx
from httpx import Request, Response


class AuthSchemeProto(Protocol):
    """Protocol for authentication schema interface."""

    def auth_flow(
        self,
        request: httpx.Request,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        """Execute the authentication flow."""

    def sync_auth_flow(
        self,
        request: httpx.Request,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        """Execute the authentication flow synchronously."""

    async def async_auth_flow(
        self,
        request: Request,
    ) -> AsyncGenerator[Request, Response]:
        """Execute the authentication flow asynchronously."""


class HttpClientProto(Protocol):
    """Protocol for http client interface."""

    def get(
        self,
        url: httpx.URL | str,
        auth: AuthSchemeProto | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""

    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: AuthSchemeProto | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""

    def patch(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: AuthSchemeProto | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""
