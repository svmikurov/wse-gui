"""Defines dependency injection containers."""

from dependency_injector import containers, providers

from wse.core.di_container import CoreContainer
from wse.features.di_container import FeatureContainer
from wse.features.shared.button_text import ButtonText


class AppContainer(containers.DeclarativeContainer):
    """Main container."""

    features = providers.Container(FeatureContainer)

    routes = providers.Dict(
        {
            ButtonText.HOME: features.main.home_ctrl().content,
            ButtonText.FOREIGN: features.foreign.home_ctrl().content,
            ButtonText.FOREIGN_TASKS: features.foreign.tasks_ctrl().content,
        }
    )

    core = providers.Container(CoreContainer)

    # API
    navigator = core.navigator
