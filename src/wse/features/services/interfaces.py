"""Defines the protocols for services interface."""

from typing import Protocol

from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core.math.task import SimpleCalcTask


class ISimpleCalcService(Protocol):
    """Protocols for Exercise Service interface."""

    def get_task(self, exercise: ExerciseEnum) -> SimpleCalcTask:
        """Get task."""

    def check_answer(self, user_answer: str) -> bool:
        """Check the user answer."""
