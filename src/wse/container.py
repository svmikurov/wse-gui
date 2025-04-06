"""Defines dependency injection containers."""

from dependency_injector import containers, providers

from wse.core.container import CoreContainer
from wse.features.container import FeatureContainer
from wse.features.shared.button_text import ButtonText


class AppContainer(containers.DeclarativeContainer):
    """Main container."""

    features = providers.Container(FeatureContainer)

    routes = {
        ButtonText.HOME: features.main.home_view().content,
    }

    core = providers.Container(CoreContainer)

    # API
    navigator = core.navigator
