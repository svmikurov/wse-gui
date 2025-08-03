"""Defines the protocols for services interface."""

from typing import Protocol, Any

from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core.math.rest import SimpleCalcResult
from wse_exercises.core.math.task import SimpleCalcTask


class ISimpleCalcService(Protocol):
    """Protocols for Exercise Service interface."""

    def get_task(self, data: dict[str, Any]) -> SimpleCalcTask:
        """Get task."""

    def check_answer(self, user_answer: str) -> SimpleCalcResult:
        """Check the user answer."""
