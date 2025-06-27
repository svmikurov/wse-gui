"""Defines protocols for common component interfaces."""

from typing_extensions import Protocol

from wse.config.layout import LoginStyle, LoginTheme

from ...interfaces import IAddObserver, IContainer, IContent, IGetContent

# NumPad


class INumPadModel(
    IAddObserver,
    Protocol,
):
    """Protocol for NumPad model interface."""

    def update_input(self, value: str) -> None:
        """Update the user input."""


class INumPadContainer(
    IAddObserver,
    IContainer,
    Protocol,
):
    """Protocol for NumPad container interface."""


class INumPadController(
    IAddObserver,
    IGetContent,
    Protocol,
):
    """Protocol for NumPad controller interface."""


# Login container


class ILoginModel(
    IAddObserver,
    Protocol,
):
    """Protocol for Login container model interface."""

    def confirm_login(self, username: str, password: str) -> None:
        """Confirm the user login."""


class ILoginContainer(
    IAddObserver,
    IContainer,
    Protocol,
):
    """Protocol for Login container interface."""

    def localize(self) -> None:
        """Localize the UI text."""

    def update_style(self, config: LoginStyle | LoginTheme) -> None:
        """Update UI style."""


class ILoginController(
    IAddObserver,
    IGetContent,
    Protocol,
):
    """Protocol for Login container controller interface."""

    @property
    def content(self) -> IContent:
        """Get page content."""
