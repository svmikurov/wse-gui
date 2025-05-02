"""Defines base calculations exercise."""

import logging
from abc import ABC, abstractmethod
from random import randint

logger = logging.getLogger(__name__)


class CalculationExercise(ABC):
    """Abstract base class for numerical calculation exercises."""

    def __init__(
        self,
        min_value: int,
        max_value: int,
    ) -> None:
        """Construct tne exercise."""
        self._min_value = min_value
        self._max_value = max_value
        self._task: str = ''
        self._answer: str = ''

    @abstractmethod
    def create_task(self) -> None:
        """Generate new task and calculate corresponding answer."""

    def _generate_operand(self) -> int:
        """Generate random integer within configured range."""
        return randint(self._min_value, self._max_value)

    @property
    def task(self) -> str:
        """Get formatted task for display."""
        return self._task

    @property
    def answer(self) -> str:
        """Get verified correct answer for current task."""
        return self._answer

    def check_answer(self, answer: str) -> bool:
        """Verify user's answer against correct solution."""
        is_correct = self._answer == answer
        logger.info(f'{is_correct = }')
        return is_correct
