"""Defines protocol interfaces for exercises."""

from typing import Protocol


class IExercise(Protocol):
    """Defines an exercise protocol."""

    def create_task(self) -> tuple[str, str]:
        """Create an exercise task."""


class ILesson(Protocol):
    """Defines a lesson protocol."""

    def create_task(self, exercise: IExercise) -> None:
        """Create a task."""

    def render_task(self) -> None:
        """Render a task."""
