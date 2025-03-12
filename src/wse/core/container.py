"""Defines a Dependency Injection containers."""

from dependency_injector import containers, providers

from wse.core.auth.auth import AuthService
from wse.core.config import Settings


class CoreContainer(containers.DeclarativeContainer):
    """Core dependencies container."""

    settings = providers.Singleton(
        Settings,
    )


class ServicesContainer(containers.DeclarativeContainer):
    """Services dependencies container."""

    settings = providers.Dependency()

    auth = providers.Singleton(
        AuthService,
        settings=settings,
    )
