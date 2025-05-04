"""Defines protocol interfaces for exercises."""

from typing import Protocol

from typing_extensions import Self

from wse.interface.iui.itext import IDisplayModel

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off

class ITask(Protocol):
    """Interface protocol defining the structure of an exercise task."""
    @property
    def text(self) -> str:
        """Return a string representation of the task."""

class IQuestion(Protocol):
    """Interface protocol representing a user's question to a task."""
    @property
    def text(self) -> str:
        """Return a string representation of the task question."""

class IAnswer(Protocol):
    """Interface protocol representing a user's answer to a task."""
    @property
    def text(self) -> str:
        """Return a string representation of the task answer."""

class IResult(Protocol):
    """Defines interface for answer validation results."""
    @property
    def is_correct(self) -> bool:
        """Whether the user's answer matches the correct solution."""
    @property
    def text(self) -> str:
        """Return a string representation of the check result."""

class IOperandGenerator(Protocol):
    """Defines interface for generating numerical operands."""
    def generate_operand(self) -> int:
        """Generate an integer for use in exercise calculations."""

class IRender(Protocol):
    """Interface for rendering components."""
    def render_task(self, task: ITask) -> None:
        """Render task components."""
    def render_result(self, result: IResult) -> None:
        """Render result components."""

class ITextDisplayRenderer(Protocol):
    """Defines interface for presentation of exercise components."""
    @classmethod
    def render(cls, task: str, display: IDisplayModel) -> None:
        """Display the current task to the user."""

class IExercise(Protocol):
    """Interface protocol for complete exercise lifecycle management."""
    def create_task(self) -> Self:
        """Create and return a new task with its conditions."""
    @property
    def question(self) -> IQuestion:
        """Retrieve the current question instance."""
    @property
    def answer(self) -> IAnswer:
        """Get the verified correct answer for the current task."""

class ITaskStorage(Protocol):
    """Defines interface for storage of task conditions."""
    def save_task(self, task: IExercise) -> None:
        """Save the conditions of an exercise task to storage."""
    def retrieve_task(self) -> IExercise:
        """Retrieve the conditions of an exercise task from storage."""
    @property
    def answer(self) -> IAnswer:
        """Retrieve from storage the correct answer."""

class IAnswerChecker(Protocol):
    """Defines interface for validating user answers solutions."""
    def check(self, user_answer: IAnswer, storage: ITaskStorage) -> None:
        """Verify user's answer against stored correct solution."""
    @staticmethod
    def get_correct_answer(storage: ITaskStorage) -> IAnswer:
        """Retrieve from storage the correct answer."""
    @property
    def result(self) -> IResult:
        """The representation of user answer check."""
