"""Defines exercise render."""

import logging

from wse.interface.iexercise import ICheckResult, IExerciseRenderer, ITask

logger = logging.getLogger(__name__)


class ExerciseRenderer(IExerciseRenderer):
    """Exercise render."""

    @classmethod
    def render_task(cls, task: ITask) -> None:
        """Render the task."""
        logger.debug(f'Render task: "{task}"')

    @classmethod
    def render_result(cls, result: ICheckResult) -> None:
        """Render the checking result."""
        logger.debug(f'Render result: "{result}"')
