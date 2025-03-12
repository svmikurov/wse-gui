"""Defines a Dependency Injection containers."""

from dependency_injector import containers, providers

from wse.core.auth.auth import AuthService
from wse.config.config import Settings


class CoreContainer(containers.DeclarativeContainer):
    """Core dependencies container."""

    settings = providers.Singleton(
        Settings,
    )
    endpoints = providers.Configuration(
        yaml_files=[
            settings().PROJECT_PATH
            / 'src'
            / 'wse'
            / 'config'
            / 'endpoints.yml'
        ]
    )


class ServicesContainer(containers.DeclarativeContainer):
    """Services dependencies container."""

    settings = providers.Dependency()
    endpoints = providers.Dependency()

    auth = providers.Singleton(
        AuthService,
        settings=settings,
        endpoints=endpoints,
    )
