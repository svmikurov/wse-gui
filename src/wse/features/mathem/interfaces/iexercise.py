"""Defines protocols for simple math exercise task and answer."""

from typing import Callable, Protocol, Type

from wse.features.shared.enums.exercises import Exercises
from wse.interfaces.iexercise import IAnswer, IQuestion, ITask

# fmt: off

class ISimpleMathQuestion(IQuestion, Protocol):
    """Protocol representing a task question."""
    _operand_1: int
    _operand_2: int
    def __init__(self, operand_1: int, operand_2: int) -> None: ...  # noqa: D107

class ISimpleMathAnswer(IAnswer, Protocol):
    """Protocol representing a task answer."""
    _operand_1: int
    _operand_2: int
    def __init__(self, operand_1: int, operand_2: int) -> None: ...  # noqa: D107

class ISimpleMathTask(ITask, Protocol):
    """Adds math-specific constraints to ITask."""
    min_value: int
    max_value: int
    operand_1: int
    operand_2: int
    question: ISimpleMathQuestion
    answer: ISimpleMathAnswer

class ISimpleMathExercise(Protocol):
    """Defines a task creation logic of simple calculation exercise."""
    _exercise_type: Exercises
    _question_class: Type[ISimpleMathQuestion]
    _answer_class: Type[ISimpleMathAnswer]
    def _create_question(self) -> ISimpleMathQuestion: ...
    def _create_answer(self) -> ISimpleMathAnswer: ...
    def _generate_operand(self) -> int: ...
    def create_task(self) -> ISimpleMathTask: ...


class IExerciseSwitcher(Protocol):
    """Exercise provider switcher."""
    def switch(self, exercise_name: str) -> None:
        """Set exercise type."""
    @property
    def current_exercise_name(self) -> Exercises:
        """Get current exercise name."""
    @property
    def current_exercise(self) -> ISimpleMathExercise:
        """Return current exercise."""
    @property
    def exercises(self) -> dict[Exercises, Callable]: ...
