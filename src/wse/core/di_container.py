"""Defines dependency injection container for core package."""

from dependency_injector import containers, providers

from wse.config.settings import Settings
from wse.core.api.auth import AuthAPI
from wse.core.auth.service import AuthService
from wse.core.navigation.navigator import Navigator


class CoreContainer(containers.DeclarativeContainer):
    """Core package container for dependency injection."""

    settings = providers.Singleton(Settings)

    # Services
    navigator = providers.Singleton(
        Navigator,
    )
    auth_api = providers.Factory(
        AuthAPI,
    )
    auth_service = providers.Singleton(
        AuthService,
        auth_api=auth_api,
    )

    # Configuration data
    endpoints = providers.Configuration(
        yaml_files=[
            settings().PROJECT_PATH
            / 'src'
            / 'wse'
            / 'config'
            / 'endpoints.yml'
        ]
    )
