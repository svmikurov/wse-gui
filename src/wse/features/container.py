"""Defines dependency injection containers for features package."""

from dependency_injector import containers, providers

from wse.features.foreign.container import ForeignContainer
from wse.features.main.container import MainContainer
from wse.features.shared.base_ui import BaseContent


class FeatureContainer(containers.DeclarativeContainer):
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
