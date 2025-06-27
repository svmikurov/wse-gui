"""Defines protocols for Simple Math Calculation page components."""

from typing import Protocol

from wse.config.layout import (
    TextTaskPanelStyle,
    TextTaskPanelTheme,
)
from wse.features.interfaces import (
    IGetContent,
    IModel,
    IObserver,
    IPageController,
    IView,
)


class ISimpleCalcModel(IModel):
    """Simple math calculation page view."""

    # Event notification

    def answer_updated(self, value: str) -> None:
        """Handle the user answer update."""

    # API for controller

    def handle_input_updated(self, value: str) -> None:
        """Handel the user input symbol."""


class ISimpleCalcView(IView):
    """Simple math calculation page view."""

    # Observer pattern methods

    def subscribe_to_numpad(self, observer: IObserver) -> None:
        """Subscribe observers to NumPad events."""

    # API for controller

    def display_question(self, value: str) -> None:
        """Display the question."""

    def clear_question(self) -> None:
        """Clear the question text."""

    def display_answer(self, value: str) -> None:
        """Display the user answer."""

    def clear_answer(self) -> None:
        """Clear the answer text."""


class ISimpleCalcController(IPageController, Protocol):
    """The controller of Simple Math calculation page."""

    # Model event notifications

    def question_updated(self, value: str) -> None:
        """Display the question."""

    def question_cleared(self) -> None:
        """Clear the question text."""

    def answer_updated(self, value: str) -> None:
        """Display the user answer."""

    def answer_cleared(self) -> None:
        """Clear the question text."""

    # NumPad event notifications

    def numpad_input_updated(self, value: str) -> None:
        """Update user input for model."""


class ISimpleCalcContainer(IGetContent, Protocol):
    """Protocol fot Simple Math calculation container interface."""

    # Layout methods

    def localize_ui(self) -> None:
        """Localize the UI text."""

    def update_style(
        self, config: TextTaskPanelStyle | TextTaskPanelTheme
    ) -> None:
        """Update widgets style."""

    # API for view

    def display_output(self, value: str) -> None:
        """Update the output text field."""

    def clear_output(self) -> None:
        """Clear the output text field."""

    def display_input(self, value: str) -> None:
        """Update the input text field."""

    def clear_input(self) -> None:
        """Clear the input text field."""
