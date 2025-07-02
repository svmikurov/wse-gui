"""Defines the protocols for services interface."""

from typing import Protocol

from wse_exercises.core.mathem.enums import Exercises
from wse_exercises.core.mathem.interfaces import ISimpleCalcTask


class ISimpleCalcService(
    Protocol,
):
    """Protocols for Exercise Service interface."""

    def get_task(self, exercise: Exercises) -> ISimpleCalcTask:
        """Get task."""

    def check_answer(
        self,
        user_answer: str,
        task: ISimpleCalcTask,
    ) -> bool:
        """Check the user answer."""
