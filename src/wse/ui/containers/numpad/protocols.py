"""Protocols for numpad components and numpad observer."""

from typing import Protocol

from wse.feature.interfaces.icontainer import Containerizable
from wse.feature.interfaces.icontent import GetContentProto
from wse.feature.interfaces.iobserver import AddObserverProto


class NumpadObserverProto(Protocol):
    """Protocol for numpad observer interface."""

    def numpad_entered(self, value: str) -> None:
        """Notification about updating the entered value."""


class NumpadModelProto(
    AddObserverProto,
    Protocol,
):
    """Protocol for NumPad model interface."""

    def update_input(self, value: str) -> None:
        """Update the user input."""

    def clear_input(self) -> None:
        """Clear the entered data."""


class NumpadContainerProto(
    AddObserverProto,
    Containerizable,
    Protocol,
):
    """Protocol for NumPad container interface."""

    def update_enabled(self, enabled: bool) -> None:
        """Update buttons enabled features."""


class NumpadControllerProto(
    AddObserverProto,
    GetContentProto,
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
