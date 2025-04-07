"""Defines dependency injection container for core package."""

from dependency_injector import containers, providers

from wse.core.navigation.navigator import Navigator


class CoreContainer(containers.DeclarativeContainer):
    """Core package container for dependency injection."""

    navigator = providers.Singleton(Navigator)
