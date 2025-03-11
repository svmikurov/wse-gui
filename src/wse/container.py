"""Defines a Dependency Injection container for the application."""

from dependency_injector import containers, providers

from wse.core.app import WSE
from wse.core.container import (
    CoreContainer,
    FeaturesContainer,
    ServicesContainer,
)


class ApplicationContainer(containers.DeclarativeContainer):
    """Dependency injection container for the application."""

    core = providers.Container(
        CoreContainer,
    )
    services = providers.Container(
        ServicesContainer,
        settings=core.settings,
    )
    features = providers.Container(
        FeaturesContainer,
        auth_service=services.auth,
        user_model=core.user_model,
    )

    # Application
    app = providers.Singleton(
        WSE,
        settings=core.settings,
        auth_service=services.auth,
        navigator=features.navigator,
    )
