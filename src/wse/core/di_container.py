"""Defines a Dependency Injection container for the application."""

from dependency_injector import containers, providers

from wse.core.app import WSE
from wse.core.auth.auth import AuthService
from wse.core.config import Settings


class DIContainer(containers.DeclarativeContainer):
    """Provides dependencies for the application."""

    settings = providers.Singleton(
        Settings,
    )
    auth_service = providers.Singleton(
        AuthService,
        settings=settings,
    )
    app = providers.Singleton(
        WSE,
        settings=settings,
        auth_service=auth_service,
    )
