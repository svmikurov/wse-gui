"""Defines the base logic for creation a simple math exercise."""

import logging
import time
from dataclasses import dataclass, field
from typing import Type

from wse.features.mathem.interfaces.iexercise import (
    ISimpleMathAnswer,
    ISimpleMathExercise,
    ISimpleMathQuestion,
    ISimpleMathTask,
)
from wse.features.mathem.interfaces.iservices import (
    IOperandGenerator,
)
from wse.features.shared.enums.exercises import Exercises

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SimpleMathTask(ISimpleMathTask):
    """Mathematical task DTO."""

    min_value: int
    max_value: int
    operand_1: int
    operand_2: int
    question: ISimpleMathQuestion
    answer: ISimpleMathAnswer
    exercise_type: Exercises
    timestamp: float = field(default_factory=time.time)


class SimpleCalculationExercise(ISimpleMathExercise):
    """Defines a base logic of simple calculation exercise creation."""

    _exercise_type: Exercises
    _question_class: Type[ISimpleMathQuestion]
    _answer_class: Type[ISimpleMathAnswer]
    _operand_1: int
    _operand_2: int

    def __init__(
        self,
        operand_generator: IOperandGenerator,
        config: dict | None = None,
    ) -> None:
        """Construct the task creation."""
        if config is not None and not isinstance(config, dict):
            logger.debug(
                f'Invalid config type: {type(config).__name__}, using empty.'
            )
            config = {}
        self._exercise_config = config or {}

        self._min_value = self._exercise_config.get('min_value', 2)
        self._max_value = self._exercise_config.get('max_value', 9)
        self._operand_generator = operand_generator

    def create_task(self) -> ISimpleMathTask:
        """Create new calculation task data transfer object."""
        self._operand_1 = self._generate_operand()
        self._operand_2 = self._generate_operand()

        return SimpleMathTask(
            min_value=self._min_value,
            max_value=self._max_value,
            operand_1=self._operand_1,
            operand_2=self._operand_2,
            exercise_type=self._exercise_type,
            question=self._create_question(),
            answer=self._create_answer(),
        )

    # Utility methods

    def _create_question(self) -> ISimpleMathQuestion:
        return self._question_class(self._operand_1, self._operand_2)

    def _create_answer(self) -> ISimpleMathAnswer:
        return self._answer_class(self._operand_1, self._operand_2)

    def _generate_operand(self) -> int:
        """Generate random integer within configured range."""
        return self._operand_generator.generate(
            self._min_value, self._max_value
        )
