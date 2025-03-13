"""Defines a Dependency Injection for features."""

from dependency_injector import containers, providers

from wse.core.navigation.navigator import Navigator
from wse.features.auth.container import AuthContainer
from wse.features.exercise.container import ExerciseContainer
from wse.features.main.container import MainContainer


class FeaturesContainer(containers.DeclarativeContainer):
    """Provides dependencies for the features and navigation."""

    container = providers.Self()
    settings = providers.Dependency()
    auth_service = providers.Dependency()
    i18n_service = providers.Dependency()

    # Navigate through features
    navigator = providers.Singleton(
        Navigator,
        container=container,
        settings=settings,
    )

    # Package containers
    auth = providers.Container(
        AuthContainer,
        navigator=navigator,
        auth_service=auth_service,
        i18n_service=i18n_service,
    )
    main = providers.Container(
        MainContainer,
        user_model=auth.user_model,
        navigator=navigator,
        i18n_service=i18n_service,
    )
    exercise = providers.Container(
        ExerciseContainer,
        user_model=auth.user_model,
        navigator=navigator,
        i18n_service=i18n_service,
    )
