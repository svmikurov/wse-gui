"""Defines dependency injection container for core package."""

import httpx
from dependency_injector import containers, providers

from wse.config.settings import Settings
from wse.core.api.auth import AuthAPI
from wse.core.auth.service import AuthService
from wse.core.navigation.navigator import Navigator
from wse.core.storage.token import TokenStorage


class CoreContainer(containers.DeclarativeContainer):
    """Core package container for dependency injection."""

    settings_provider = providers.Configuration(pydantic_settings=[Settings()])
    settings = settings_provider.get_pydantic_settings()[0]

    endpoints = providers.Configuration(yaml_files=[settings.ENDPOINTS_PATH])

    # Services
    navigator = providers.Singleton(
        Navigator,
    )
    api_client = providers.Singleton(
        httpx.Client,
    )
    auth_api = providers.Singleton(
        AuthAPI,
        base_url=settings.base_url,
        api_client=api_client,
        endpoints=endpoints,
    )
    token_storage = providers.Singleton(
        TokenStorage,
        token_path=settings.storage_config.token_path,
        encryption_key=settings.storage_config.encryption_key,
    )
    auth_service = providers.Singleton(
        AuthService,
        auth_api=auth_api,
        token_storage=token_storage,
    )
