"""Defines protocol interfaces for application components."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from wse.features.shared.button_text import ButtonText


class INavigator(Protocol):
    """Protocol defining the interface for navigator."""

    def navigate(self, button_text: ButtonText) -> None:
        """Navigate to page by button text."""
