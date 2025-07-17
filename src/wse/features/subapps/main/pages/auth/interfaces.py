"""Defines Authentication page interfaces."""

from typing import Protocol

from wse.features.interfaces import IModel, IPageController, IView


class IAuthModel(
    IModel,
    Protocol,
):
    """Protocol for Authentication page model interface."""

    # API for controller

    def handle_success_authentication(self) -> None:
        """Handle the success authentication."""


class IAuthView(
    IView,
    Protocol,
):
    """Protocol for Authentication page view interface."""

    # Notifications from Login container

    def success_authentication(self) -> None:
        """Notify subjects about success authentication event ."""

    def clear_credential(self) -> None:
        """Clear the entered credential."""


class IAuthController(
    IPageController,
    Protocol,
):
    """Protocol for Authentication page controller interface."""

    # Notifications from View

    def success_authentication(self) -> None:
        """Handle the success authentication event."""

    # Notifications from Model

    def credential_clean(self) -> None:
        """Handle the credential clean."""
