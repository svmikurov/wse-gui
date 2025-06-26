"""Defines protocols for MVC model components interface."""

from typing import Protocol, runtime_checkable

from wse.config.layout import StyleConfig, ThemeConfig

from ..subapps.nav_id import NavID
from .icontainer import IContainer
from .icontent import IGetContent
from .iobserver import IAddObserver


class ILocalize(Protocol):
    """Protocol for localize feature interface."""

    def localize_ui(self) -> None:
        """Localize the UI text."""


class IModel(
    IAddObserver,
    Protocol,
):
    """Protocol for page model interface."""


class IView(
    IAddObserver,
    IContainer,
    ILocalize,
    Protocol,
):
    """Protocol for page view interface."""

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""


@runtime_checkable
class IController(
    IGetContent,
    Protocol,
):
    """Protocol for controller interface."""


class IPageController(
    IController,
    Protocol,
):
    """Protocol for page controller interface."""

    def navigate(self, nav_id: NavID) -> None:
        """Navigate to page."""
