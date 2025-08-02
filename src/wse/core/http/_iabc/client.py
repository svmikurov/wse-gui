"""Defines protocol and abc for http client."""

from abc import ABC, abstractmethod
from typing import Any, Protocol

import httpx
from typing_extensions import override


class IHttpClient(Protocol):
    """Protocol for http client interface."""

    def get(
        self,
        url: httpx.URL | str,
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""

    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: httpx.Auth | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""

    def patch(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""


class BaseHttpClient(ABC, IHttpClient):
    """Base class for Http client."""

    @abstractmethod
    @override
    def get(
        self,
        url: httpx.URL | str,
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `GET` request."""

    @abstractmethod
    @override
    def post(
        self,
        url: httpx.URL | str,
        json: dict[str, Any] | None = None,
        auth: httpx.Auth | None = None,
        headers: dict[str, str] | None = None,
    ) -> httpx.Response:
        """Send a `POST` request."""

    @abstractmethod
    @override
    def patch(
        self,
        url: httpx.URL | str,
        json: dict[str, Any],
        auth: httpx.Auth | None = None,
    ) -> httpx.Response:
        """Send a `PATCH` request."""
