"""Defines the base logic for creation a simple math task and answer."""

from abc import ABC, abstractmethod


class SimpleMathTaskComponent(ABC):
    """Defines the logic for creating a simple math task or answer."""

    def __init__(self, operand_1: int, operand_2: int) -> None:
        """Construct the logic creation."""
        self._operand_1 = operand_1
        self._operand_2 = operand_2
        self._create()

    @abstractmethod
    def _create(self) -> None:
        """Create a simple math task or answer."""


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


class SimpleTextQuestion(TextQuestionMixin, SimpleMathTaskComponent, ABC):
    """Combines simple task question creation and its property."""


class SimpleTextAnswer(TextAnswerMixin, SimpleTextQuestion, ABC):
    """Combines simple task answer creation and its property."""
