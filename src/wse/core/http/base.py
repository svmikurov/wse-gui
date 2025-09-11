"""Protocols and ABC for HTTP client."""

from abc import ABC, abstractmethod
from typing import Any

import httpx

from .protocol import AuthSchemeProto


class HttpClientABC(ABC):
    """Abstract base class for Http client."""

    @abstractmethod
    def get(
        self,
        url: httpx.URL | str,
        auth: AuthSchemeProto | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""

    @abstractmethod
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: AuthSchemeProto | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""

    @abstractmethod
    def patch(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: AuthSchemeProto | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""

    @abstractmethod
    def _request(
        self,
        method: str,
        url: httpx.URL | str,
        auth: AuthSchemeProto | None,
        json: dict[str, Any] | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response: ...
