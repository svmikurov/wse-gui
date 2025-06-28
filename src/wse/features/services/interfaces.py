"""Defines the protocols for services interface."""

from ..interfaces import IAddObserver


class IExerciseService(
    IAddObserver,
):
    """Protocols for Exercise Service interface."""

    def update_answer(self, value: str) -> None:
        """Update user input answer."""
