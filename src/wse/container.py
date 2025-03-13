"""Defines a Dependency Injection container for the application."""

from dependency_injector import containers, providers

from wse.core.app import WSE
from wse.core.container import CoreContainer, ServicesContainer
from wse.features.container import FeaturesContainer


class ApplicationContainer(containers.DeclarativeContainer):
    """Dependency injection container for the application."""

    # Core
    core = providers.Container(
        CoreContainer,
    )

    # Services
    services = providers.Container(
        ServicesContainer,
        settings=core.settings,
        endpoints=core.endpoints,
    )

    # Features
    features = providers.Container(
        FeaturesContainer,
        settings=core.settings,
        auth_service=services.auth,
        i18n_service=services.i18n,
    )

    # Application
    app = providers.Singleton(
        WSE,
        settings=core.settings,
        auth_service=services.auth,
        navigator=features.navigator,
    )
