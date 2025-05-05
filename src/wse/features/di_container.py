"""Defines dependency injection containers for features package."""

from dependency_injector import containers, providers

from wse.features.examples.di_container import ExamplesContainer
from wse.features.figaro.di_container import FigaroContainer
from wse.features.foreign.di_container import ForeignContainer
from wse.features.main.containers.di_container import LayerContainer
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

    # Layer container (experimental)
    layer_container = providers.Container(
        LayerContainer,
        api_client=api_client,
        subject=share_container.subject,
        context=share_container.context,
        content_box=share_container.content_box,
    )

    # Basic "WSE" containers
    main = providers.Container(
        MainContainer,
        auth_service=auth_service,
        api_client=api_client,
        content_box=share_container.content_box,
        subject=share_container.subject,
        layer_container=layer_container,
    )
    foreign = providers.Container(
        ForeignContainer,
        content_box=share_container.content_box,
        subject=share_container.subject,
    )
    mathematical = providers.Container(
        MathematicalContainer,
        share_container=share_container,
    )

    # Additional containers
    figaro = providers.Container(
        FigaroContainer,
        api_client=api_client,
        subject=share_container.subject,
        content_box=share_container.content_box,
        # Containers
        layer_container=layer_container,
    )
    examples = providers.Container(
        ExamplesContainer,
        content=share_container.simple_content,
        style_config=share_container.style_config,
        button_handler=share_container.button_handler,
        subject=share_container.subject,
    )
