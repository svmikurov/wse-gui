"""Assigned exercise entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AssignedExercise:
    """Assigned exercise.

    Exercise that was selected by user to complete.
    """

    assignation_id: str | None = None

    question_url_path: str | None = None
    check_url_path: str | None = None

    task_io: str | None = None
