"""Defines exercise render."""

import logging

from wse.interface.iexercise import ICheckResult

logger = logging.getLogger(__name__)


class ExerciseRenderer:
    """Exercise render."""

    @classmethod
    def render_result(cls, result: ICheckResult) -> None:
        """Render the checking result."""
        logger.debug(f'Render result: "{result}"')
