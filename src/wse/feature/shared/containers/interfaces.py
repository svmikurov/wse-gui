"""Defines protocols for containers interfaces."""

from typing import Any, Iterable

from typing_extensions import Protocol

from wse.config.layout import StyleConfig, ThemeConfig
from wse.feature.interfaces.icontainer import Containerizable
from wse.feature.interfaces.icontent import GetContentProto
from wse.feature.interfaces.iobserver import AddObserverProto

# Text task container


class TextTaskContainerProto(
    Containerizable,
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

    @property
    def answer(self) -> str:
        """Get text."""


# Select container


class SelectionContainerProto(
    AddObserverProto,
    Containerizable,
    Protocol,
):
    """Protocol for Select container interface."""

    def update_items(self, items: Iterable[Any]) -> None:
        """Update select items."""


class SelectionControllerProto(
    AddObserverProto,
    GetContentProto,
    Protocol,
):
    """Protocol for Select container controller interface."""

    def update_items(self, items: Iterable[Any]) -> None:
        """Update select items."""
