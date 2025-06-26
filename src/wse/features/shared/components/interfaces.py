"""Defines protocols for common component interfaces."""

from ...interfaces import IAddObserver, IContainer, IGetContent


class INumPadModel(
    IAddObserver,
):
    """Protocol for NumPad model interface."""

    def update_input(self, value: str) -> None:
        """Update the user input."""


class INumPadContainer(
    IAddObserver,
    IContainer,
):
    """Protocol for NumPad container interface."""


class INumPadController(
    IAddObserver,
    IGetContent,
):
    """Protocol for NumPad controller interface."""
