"""Defines core interfaces for the application."""

# ruff: noqa: D101, D102

from typing import Optional, Protocol

from httpx import Response

from wse.config.config import Languages
from wse.core.navigation.routes import Route


class IAuthService(Protocol):
    """Defines the interface for authentication services."""

    async def authenticate(self, username: str, password: str) -> None: ...
    async def is_authenticated(self) -> bool: ...


class IAuthAPI(Protocol):
    """Defines the interface for authentication-related API requests."""

    async def authenticate(self, username: str, password: str) -> str: ...
    async def validate_token(self, token: str) -> bool: ...


class IApiClient(Protocol):
    """Defines the interface for making API requests."""

    async def get(self, endpoint: str, **kwargs: object) -> Response: ...
    async def post(self, endpoint: str, **kwargs: object) -> Response: ...
    async def put(self, endpoint: str, **kwargs: object) -> Response: ...
    async def patch(self, endpoint: str, **kwargs: object) -> Response: ...
    async def delete(self, endpoint: str, **kwargs: object) -> Response: ...


class ITokenStorage(Protocol):
    """Defines the interface for token storage and retrieval."""

    def save_token(self, token: str) -> None: ...
    def load_token(self) -> Optional[str]: ...


class INavigator(Protocol):
    """Defines the interface for application navigation."""

    def navigate(self, route: Route) -> None: ...


class II18NService(Protocol):
    """Defines interface for internationalization service."""

    def gettext(self, text: str) -> str: ...
    def set_language(self, lang: Languages) -> bool: ...
    def change_language(self, lang: Languages) -> None: ...
    def get_current_language(self) -> str: ...
    def add_listener(self, listener: object) -> None: ...
