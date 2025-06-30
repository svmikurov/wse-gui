"""Defines protocols for API interfaces."""

from typing import Any, Protocol


class IExerciseApi(
    Protocol,
):
    """Defines protocol for exercise API."""

    def request_task(self) -> dict[str, Any]:
        """Request the task."""
