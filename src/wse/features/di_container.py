"""Defines dependency injection containers for features package."""

from dependency_injector import containers, providers

from wse.features.base.context import Context
from wse.features.examples.di_container import ExamplesContainer
from wse.features.figaro.di_container import FigaroContainer
from wse.features.foreign.di_container import ForeignContainer
from wse.features.main.containers.di_container import LayerContainer
from wse.features.main.di_container import MainContainer
from wse.features.mathem.di_container import MathematicalContainer
from wse.features.shared.content import BaseContent
from wse.features.shared.observer import Subject


class FeatureContainer(containers.DeclarativeContainer):
    """Features package container."""

    # Services
    auth_service = providers.Dependency()
    api_client = providers.Dependency()

    # Styled general box for content
    content_box = providers.Factory(BaseContent)
    # The subject of observation in the Observer pattern
    subject = providers.Factory(Subject)
    # Context
    context = providers.Factory(Context)

    # Layer container (experimental)
    layer_container = providers.Container(
        LayerContainer,
        api_client=api_client,
        subject=subject,
        context=context,
        content_box=content_box,
    )

    # Basic containers
    main = providers.Container(
        MainContainer,
        auth_service=auth_service,
        api_client=api_client,
        content_box=content_box,
        subject=subject,
        layer_container=layer_container,
    )
    foreign = providers.Container(
        ForeignContainer,
        content_box=content_box,
        subject=subject,
    )
    mathematical = providers.Container(
        MathematicalContainer,
    )

    # Additional containers
    figaro = providers.Container(
        FigaroContainer,
        api_client=api_client,
        subject=subject,
        content_box=content_box,
        # Containers
        layer_container=layer_container,
    )
    examples = providers.Container(
        ExamplesContainer,
        layer_container=layer_container,
    )
