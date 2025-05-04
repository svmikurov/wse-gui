"""Defines mathematical exercises."""

import dataclasses
from abc import ABC, abstractmethod
from random import randint

from typing_extensions import Self

from wse.features.mathem.exercises.calculations import (
    AddAnswer,
    AddQuestion,
    MulAnswer,
    MulQuestion,
)
from wse.interface.iexercise import IAnswer, IQuestion


@dataclasses.dataclass
class CalculationExercise(ABC):
    """Exercise on multiplication."""

    _min_value: int = 1
    _max_value: int = 9
    _operand_1: int | None = None
    _operand_2: int | None = None
    _question: IQuestion | None = None
    _answer: IAnswer | None = None

    @abstractmethod
    def _get_question(self) -> IQuestion:
        pass

    @abstractmethod
    def _get_answer(self) -> IAnswer:
        pass

    # Business logic

    def create_task(self) -> Self:
        """Generate new multiplication task and calculate answer."""
        self._operand_1 = self._generate_operand()
        self._operand_2 = self._generate_operand()
        self._question = self._get_question()
        self._answer = self._get_answer()
        return self

    # Utility methods

    def _generate_operand(self) -> int:
        """Generate random integer within configured range."""
        return randint(self._min_value, self._max_value)

    @property
    def question(self) -> IQuestion:
        """Get formatted task for display."""
        return self._question

    @property
    def answer(self) -> IAnswer:
        """Get verified correct answer for current task."""
        return self._answer

    @property
    def min_value(self) -> int:
        """Min operand value."""
        return self._min_value

    @property
    def max_value(self) -> int:
        """Max operand value."""
        return self._max_value


class MultiplicationExercise(CalculationExercise):
    """Exercise on multiplication."""

    def _get_question(self) -> IQuestion:
        return MulQuestion(self._operand_1, self._operand_2)

    def _get_answer(self) -> IAnswer:
        return MulAnswer(self._operand_1, self._operand_2)


class AddingExercise(CalculationExercise):
    """Exercise on adding."""

    def _get_question(self) -> IQuestion:
        return AddQuestion(self._operand_1, self._operand_2)

    def _get_answer(self) -> IAnswer:
        return AddAnswer(self._operand_1, self._operand_2)
