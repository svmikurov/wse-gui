"""Defines mathematical exercises."""

import dataclasses
import logging
from random import randint

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class MultiplicationExercise:
    """Exercise on multiplication."""

    _min_value: int = 1
    _max_value: int = 9
    _operand_1: int | None = None
    _operand_2: int | None = None
    _task: str | None = None
    _answer: str | None = None

    # Business logic

    def create_task(self) -> None:
        """Generate new multiplication task and calculate answer."""
        self._operand_1 = self._generate_operand()
        self._operand_2 = self._generate_operand()
        self._task = f'{self._operand_1} x {self._operand_2}'
        self._answer = str(self._operand_1 * self._operand_2)
        logger.debug(f'Created multiplication task: {self._task}')

    # Utility methods

    def _generate_operand(self) -> int:
        """Generate random integer within configured range."""
        return randint(self._min_value, self._max_value)

    # Properties

    @property
    def min_value(self) -> int:
        """Min operand value."""
        return self._min_value

    @min_value.setter
    def min_value(self, value: int | str) -> None:
        self._min_value = int(value)

    @property
    def max_value(self) -> int:
        """Max operand value."""
        return self._max_value

    @max_value.setter
    def max_value(self, value: int | str) -> None:
        self._max_value = int(value)

    @property
    def task(self) -> str:
        """Get formatted task for display."""
        return self._task

    @property
    def answer(self) -> str:
        """Get verified correct answer for current task."""
        return self._answer
