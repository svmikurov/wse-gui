"""ABC and protocols for widget containers interface."""

from typing import Protocol

from wse.feature.interfaces.types import StyleT_co, ThemeT_co

from ..interfaces.icontent import GetContentProto


class Stylizable(
    Protocol[StyleT_co, ThemeT_co],
):
    """Protocol for UI style updating interface."""

    def update_style(self, config: StyleT_co | ThemeT_co) -> None:
        """Update widgets style."""


class Localizable(
    Protocol,
):
    """Protocol for UI localisation interface."""

    def localize_ui(self) -> None:
        """Localize the UI text."""


class Containerizable(
    GetContentProto,
    Protocol,
):
    """Protocol for common widget container interface."""
