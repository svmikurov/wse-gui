"""Defines dependency injection containers."""

from dependency_injector import containers, providers

from wse.core.navigaion.navigator import Navigator
from wse.features.foreign.home_ctrl import ForeignCtrl
from wse.features.foreign.home_view import ForeignView
from wse.features.home.controller import HomeController
from wse.features.home.view import HomeView
from wse.features.shared.base import BaseBox
from wse.features.shared.button_text import ButtonText


class FeatureContainer(containers.DeclarativeContainer):
    """Features package container."""

    # Styled general box for content
    content_box = providers.Factory(BaseBox)

    # Main
    home_view = providers.Factory(HomeView, content=content_box)
    home_ctrl = providers.Factory(HomeController, view=home_view)

    # Foreign
    foreign_view = providers.Factory(ForeignView, content=content_box)
    foreign_ctrl = providers.Factory(ForeignCtrl, view=foreign_view)


class CoreContainer(containers.DeclarativeContainer):
    """core package container."""

    navigator = providers.Singleton(Navigator)


class MainContainer(containers.DeclarativeContainer):
    """Main container."""

    features = providers.Container(FeatureContainer)

    routes = {
        ButtonText.HOME: features.home_view().content,
    }

    core = providers.Container(CoreContainer)

    # API
    navigator = core.navigator
