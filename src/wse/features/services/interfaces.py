"""Defines the protocols for services interface."""

from typing import Protocol


class ITask(
    Protocol,
):
    """Exercise task."""

    question: str
    answer: str


class IExerciseService(
    Protocol,
):
    """Protocols for Exercise Service interface."""

    def update_answer(self, value: str) -> None:
        """Update user input answer."""

    def get_task(self) -> ITask:
        """Get task."""
