"""Defines protocols for common container interfaces."""

from typing import Protocol

from wse.config.layout import TextTaskPanelStyle, TextTaskPanelTheme

from ...interfaces.icontainer import IContainer


class ITextTaskPanel(IContainer, Protocol):
    """Protocol for task panel interface."""

    def display_question(self, value: str) -> None:
        """Update the output text field."""

    def clear_question(self) -> None:
        """Clear the output text field."""

    def display_answer(self, value: str) -> None:
        """Update the input text field."""

    def clear_answer(self) -> None:
        """Clear the input text field."""

    def update_style(
        self, config: TextTaskPanelStyle | TextTaskPanelTheme
    ) -> None:
        """Update widgets style."""
