"""Defines protocols for MVC model components interface."""

from typing import Protocol, runtime_checkable

from wse.config.layout import StyleConfig, ThemeConfig

from .icontainer import IContainer
from .icontent import IGetContent
from .iobserver import IAddObserver


class IModel(
    IAddObserver,
    Protocol,
):
    """Protocol for page model interface."""


class IView(
    IContainer,
    Protocol,
):
    """Protocol for page view interface."""

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""

    def localize_ui(self) -> None:
        """Localize the UI text."""


@runtime_checkable
class IController(
    IGetContent,
    Protocol,
):
    """Protocol for page controller interface."""
