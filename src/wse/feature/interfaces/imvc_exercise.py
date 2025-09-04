"""Defines protocols and ABC for exercise MVC components."""

from typing import Protocol

from wse.feature.interfaces.imvc import ModelProto

# Model


class ExerciseModelFeatureProto(ModelProto, Protocol):
    """Protocol for model interface of exercise page."""

    def update_task(self) -> None:
        """Start or update task."""

    def set_answer(self, value: str) -> None:
        """Set the entered user answer."""

    def check_answer(self) -> None:
        """Check the user's submitted answer."""


# Observing the model


class ExerciseModelObserverProto(Protocol):
    """Protocol of exercise model event observer interface."""

    def task_updated(self, value: str) -> None:
        """Handle the model event on task update."""

    def answer_updated(self, value: str) -> None:
        """Handle the model event on answer update."""

    def answer_incorrect(self, value: str) -> None:
        """Handle the model event on success answer checking."""


# View


class ExerciseViewFeatureProto(Protocol):
    """Protocol for view interface of exercise page."""

    def show_question(self, question: str) -> None:
        """Show the question."""

    def show_answer(self, value: str) -> None:
        """Show the user answer."""


# Observing the view


class ExerciseViewObserverProto(Protocol):
    """Protocol of exercise view event observer interface."""

    def task_started(self) -> None:
        """Handle the event of view on task start."""

    def answer_entered(self, value: str) -> None:
        """Handle the event of view on answer enter."""

    def answer_submitted(self) -> None:
        """Handle the event of view on answer submit."""
