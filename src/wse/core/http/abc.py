"""Abstract base class for HTTP client."""

from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Generator

import httpx
from httpx import Request, Response

# TODO: Update protocols to ABC?


class AuthSchemaABC(ABC):
    """ABC for authentication schema."""

    @abstractmethod
    def auth_flow(
        self,
        request: httpx.Request,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        """Execute the authentication flow."""

    @abstractmethod
    def sync_auth_flow(
        self,
        request: httpx.Request,
    ) -> Generator[httpx.Request, httpx.Response, None]:
        """Execute the authentication flow synchronously."""

    @abstractmethod
    async def async_auth_flow(
        self,
        request: Request,
    ) -> AsyncGenerator[Request, Response]:
        """Execute the authentication flow asynchronously."""


class HttpClientABC(ABC):
    """ABC for http client."""

    @abstractmethod
    def get(
        self,
        url: httpx.URL | str,
        auth: AuthSchemaABC | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""

    @abstractmethod
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: AuthSchemaABC | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""

    @abstractmethod
    def patch(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: AuthSchemaABC | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""

    @abstractmethod
    def put(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: AuthSchemaABC | None = None,
    ) -> httpx.Response:
        """Send a PUT request."""
