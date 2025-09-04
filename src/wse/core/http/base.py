"""Protocols and ABC for HTTP client."""

from abc import ABC, abstractmethod
from typing import Any

import httpx
from typing_extensions import override

from .protocol import AuthSchemeProto, HttpClientProto


class BaseHttpClient(ABC, HttpClientProto):
    """Abstract base class for Http client."""

    @abstractmethod
    @override
    def get(
        self,
        url: httpx.URL | str,
        auth: AuthSchemeProto | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""

    @abstractmethod
    @override
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: AuthSchemeProto | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""

    @abstractmethod
    @override
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
