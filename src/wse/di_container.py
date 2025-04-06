"""Defines dependency injection containers."""

from dependency_injector import containers, providers

from wse.core.di_container import CoreContainer
from wse.features.di_container import FeatureContainer


class AppContainer(containers.DeclarativeContainer):
    """Main container."""

    core = providers.Container(CoreContainer)
    features = providers.Container(FeatureContainer)

    # API
    navigator = core.navigator
    routes = providers.Dict(
        {
            **features.main.routes(),
            **features.foreign.routes(),
        }
    )
