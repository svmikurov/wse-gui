"""Defines dependency injection containers."""

from dependency_injector import containers, providers

from wse.core.navigaion.navigator import Navigator
from wse.features.foreign.home_ctrl import ForeignCtrl
from wse.features.foreign.home_view import ForeignView
from wse.features.foreign.tasks_ctrl import TasksController
from wse.features.foreign.tasks_view import TasksView
from wse.features.home.controller import HomeController
from wse.features.home.view import HomeView
from wse.features.shared.base_ui import BaseContent
from wse.features.shared.button_text import ButtonText


class MainContainer(containers.DeclarativeContainer):
    """Main pages container."""

    content_box = providers.Dependency()

    home_view = providers.Factory(HomeView, content_box=content_box)
    home_ctrl = providers.Factory(HomeController, view=home_view)


class ForeignContainer(containers.DeclarativeContainer):
    """Foreign pages container."""

    content_box = providers.Dependency()

    foreign_view = providers.Factory(ForeignView, content_box=content_box)
    foreign_ctrl = providers.Factory(ForeignCtrl, view=foreign_view)

    foreign_tasks_view = providers.Factory(TasksView, content_box=content_box)
    foreign_tasks_ctrl = providers.Factory(
        TasksController, view=foreign_tasks_view
    )


class FeatureContainer(ForeignContainer):
    """Features package container."""

    # Styled general box for content
    content_box = providers.Factory(BaseContent)

    main = providers.Container(
        MainContainer,
        content_box=content_box,
    )
    foreign = providers.Container(
        ForeignContainer,
        content_box=content_box,
    )


class CoreContainer(containers.DeclarativeContainer):
    """core package container."""

    navigator = providers.Singleton(Navigator)


class AppContainer(containers.DeclarativeContainer):
    """Main container."""

    features = providers.Container(FeatureContainer)

    routes = {
        ButtonText.HOME: features.main.home_view().content,
    }

    core = providers.Container(CoreContainer)

    # API
    navigator = core.navigator
