"""Defines protocol for Home page component interfaces."""

from typing import Protocol

from wse.features.interfaces.imvc import IModel, IPageController, IView


class IHomeModel(
    IModel,
    Protocol,
):
    """Protocol for Home page model interface."""

    def on_open(self) -> None:
        """Call model methods when page opens."""

    def handle_logout(self) -> None:
        """Handle the logout event."""


class IHomeView(
    IView,
    Protocol,
):
    """Protocol for Home page view interface."""

    def set_authenticated_content(self) -> None:
        """Set page content for authenticated user."""

    def set_anonymous_content(self) -> None:
        """Set page content for anonymous user."""


class IHomeController(
    IPageController,
    Protocol,
):
    """Protocol for Home page controller interface."""

    def user_authenticated(self) -> None:
        """Set content for authenticated user."""

    def user_anonymous(self) -> None:
        """Set content for anonymous user."""

    def logout(self) -> None:
        """Handle the logout event."""
