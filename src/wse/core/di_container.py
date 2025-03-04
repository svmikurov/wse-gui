"""Dependency Injector container."""

from dependency_injector import containers, providers

from wse.core.app import WSE
from wse.core.auth.auth import AuthService
from wse.core.config import Settings


class DIContainer(containers.DeclarativeContainer):
    """Dependency Injector container."""

    settings = providers.Singleton(Settings)

    auth_service = providers.Factory(AuthService)

    app = providers.Factory(
        WSE,
        settings=settings,
        auth_service=auth_service,
    )
