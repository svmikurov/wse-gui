"""Defines mathematical calculations."""

import dataclasses


@dataclasses.dataclass
class SimpleCalculation:
    """A simple calculation task creator."""

    _operand_1: int
    _operand_2: int


class TextQuestionMixin:
    """Mixin for string representation of the task question."""

    _question: str

    @property
    def text(self) -> str:
        """Return a string representation of the task question."""
        return self._question


class TextAnswerMixin:
    """Mixin for string representation of the task answer."""

    _answer: int

    @property
    def text(self) -> str:
        """Return a string representation of the task answer."""
        return str(self._answer)


@dataclasses.dataclass()
class MulQuestion(TextQuestionMixin, SimpleCalculation):
    """A multiplication task question."""

    def __post_init__(self) -> None:
        """Create a task question."""
        self._question = f'{self._operand_1} x {self._operand_2}'


@dataclasses.dataclass()
class MulAnswer(TextAnswerMixin, SimpleCalculation):
    """A multiplication task answer."""

    def __post_init__(self) -> None:
        """Create a task answer."""
        self._answer = self._operand_1 * self._operand_2


@dataclasses.dataclass()
class AddQuestion(TextQuestionMixin, SimpleCalculation):
    """A multiplication task question."""

    def __post_init__(self) -> None:
        """Create a task question."""
        self._question = f'{self._operand_1} + {self._operand_2}'


@dataclasses.dataclass()
class AddAnswer(TextAnswerMixin, SimpleCalculation):
    """A multiplication task answer."""

    def __post_init__(self) -> None:
        """Create a task answer."""
        self._answer = self._operand_1 + self._operand_2
