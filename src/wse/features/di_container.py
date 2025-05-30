"""Defines dependency injection containers for features package."""

from dependency_injector import containers, providers

from wse.features.examples.di_container import ExamplesContainer
from wse.features.main.containers.login import LoginContainer
from wse.features.main.di_container import MainContainer
from wse.features.mathem.di_container import MathematicalContainer
from wse.features.shared.di_container import ShareContainer


class FeatureContainer(containers.DeclarativeContainer):
    """Features package container."""

    # Service dependencies
    auth_service = providers.Dependency()
    api_client = providers.Dependency()

    # Containers
    share_container = providers.Container(
        ShareContainer,
    )

    login_container = providers.Factory(
        LoginContainer,
        content_box=share_container.content_box,
        subject=share_container.subject,
    )

    # Basic "WSE" containers
    main = providers.Container(
        MainContainer,
        auth_service=auth_service,
        api_client=api_client,
        content_box=share_container.content_box,
        subject=share_container.subject,
        login_container=login_container,
    )
    mathematical = providers.Container(
        MathematicalContainer,
        share_container=share_container,
    )

    # Additional containers
    examples = providers.Container(
        ExamplesContainer,
        simple_content=share_container.simple_content,
        style_config=share_container.style_config,
        button_handler=share_container.button_handler,
        subject=share_container.subject,
    )
