"""Assigned exercise entity."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AssignedExercise:
    """Assigned exercise.

    Exercise that was selected by user to complete.
    """

    question_url_path: str
    check_url_path: str

    task_io: str
