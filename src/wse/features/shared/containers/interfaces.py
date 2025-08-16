"""Defines protocols for containers interfaces."""

from typing import Any, Iterable

from typing_extensions import Protocol

from wse.config.layout import StyleConfig, ThemeConfig

from ...interfaces.icontainer import IAddObserver, IContainer
from ...interfaces.icontent import IGetContent

# Text task container


class ITextTaskContainer(
    IContainer,
    Protocol,
):
    """Protocol for Texet task container interface."""

    def display_question(self, value: str) -> None:
        """Update the question text field."""

    def clear_question(self) -> None:
        """Clear the question text field."""

    def display_answer(self, value: str) -> None:
        """Update the answer text field."""

    def clear_answer(self) -> None:
        """Clear the answer text field."""

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update widgets style."""

    def display_correct_answer(self, expression: str) -> None:
        """Display the correct answer."""


# NumPad


class INumPadModel(
    IAddObserver,
    Protocol,
):
    """Protocol for NumPad model interface."""

    def update_input(self, value: str) -> None:
        """Update the user input."""

    def clear_input(self) -> None:
        """Clear the entered data."""


class INumPadContainer(
    IAddObserver,
    IContainer,
    Protocol,
):
    """Protocol for NumPad container interface."""

    def update_enabled(self, enabled: bool) -> None:
        """Update buttons enabled features."""


class INumPadController(
    IAddObserver,
    IGetContent,
    Protocol,
):
    """Protocol for NumPad controller interface."""

    # Notification from View

    def button_pressed(self, value: str) -> None:
        """Handle the button press event."""

    # Notification for outer component

    def numpad_input_updated(self, value: str) -> None:
        """Handle the input update event."""

    # API for outer component

    def clear_input(self) -> None:
        """Clear the entered data."""

    def disable_buttons(self) -> None:
        """Disable numpad buttons."""

    def enable_buttons(self) -> None:
        """Enable numpad buttons."""


# Login container


class ILoginModel(
    IAddObserver,
    Protocol,
):
    """Protocol for Login container model interface."""

    def authenticate(self, username: str, password: str) -> None:
        """Authenticate the user."""


class ILoginContainer(
    IAddObserver,
    IContainer,
    Protocol,
):
    """Protocol for Login container interface."""

    def localize(self) -> None:
        """Localize the UI text."""

    def update_style(self, config: StyleConfig | ThemeConfig) -> None:
        """Update UI style."""

    def clear_credential(self) -> None:
        """Clear the entered credential."""


class ILoginController(
    IAddObserver,
    IGetContent,
    Protocol,
):
    """Protocol for Login container controller interface."""

    # Notifications from Container

    def login_confirm(self, username: str, password: str) -> None:
        """Handle the login confirmation."""

    def clear_credential(self) -> None:
        """Clear the entered credential."""

    def success_authentication(self) -> None:
        """Notify about successful authentication."""


# Selection container


class ISelectionContainer(
    IAddObserver,
    IContainer,
    Protocol,
):
    """Protocol for Select container interface."""

    def update_items(self, items: Iterable[Any]) -> None:
        """Update selection items."""


class ISelectionController(
    IAddObserver,
    IGetContent,
    Protocol,
):
    """Protocol for Select container controller interface."""

    def update_items(self, items: Iterable[Any]) -> None:
        """Update selection items."""
