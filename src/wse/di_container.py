"""Defines dependency injection containers."""

from dependency_injector import containers, providers

from wse.core.di_container import CoreContainer
from wse.features.di_container import FeatureContainer


class AppContainer(containers.DeclarativeContainer):
    """Main container."""

    _core_container = providers.Container(CoreContainer)
    _features_container = providers.Container(FeatureContainer)

    # API
    navigator = _core_container.navigator
    routes = providers.Dict(
        {
            **_features_container.main.routes(),
            **_features_container.foreign.routes(),
        }
    )
