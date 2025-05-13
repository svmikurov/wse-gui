"""Defines protocol interfaces for exercises."""

from typing import Protocol

from wse.features.shared.enums.exercises import Exercises
from wse.interfaces.iui.itext import IDisplayModel

# fmt: off

class IQuestion(Protocol):
    """Interface protocol representing a task question."""
    @property
    def text(self) -> str: ...

class IAnswer(Protocol):
    """Interface protocol representing a task answer."""
    @property
    def text(self) -> str: ...

class ITask(Protocol):
    """Base protocol for all exercise tasks."""
    exercise_type: Exercises
    timestamp: float

class IExercise(Protocol):
    """Protocol for exercises with task creation logic."""
    def create_task(self) -> ITask:
        """Create a new task instance with generated conditions."""

class IResult(Protocol):
    """Defines interface for answer validation results."""
    @property
    def is_correct(self) -> bool: ...
    @property
    def text(self) -> str:
        """Return a string representation of the check result."""
    def __str__(self) -> str:
        """Return the string representation of check result."""

# ----------------------------------------------------------------------
# Exercise services
# ----------------------------------------------------------------------

class IRender(Protocol):
    """Interface for rendering components."""
    def render_task(self, task: ITask) -> None: ...
    def render_result(self, result: IResult) -> None: ...

class ITextDisplayRenderer(Protocol):
    """Protocol for presentation of exercise components."""
    def render(self, task: str, display: IDisplayModel) -> None: ...

class ITaskStorage(Protocol):
    """Defines interface for storage of task conditions."""
    def save_task(self, task: ITask) -> None: ...
    def retrieve_task(self) -> ITask: ...
    @property
    def answer(self) -> IAnswer: ...

class IAnswerChecker(Protocol):
    """Defines interface for validating user answers solutions."""
    def check(self, user_answer: IAnswer, storage: ITaskStorage) -> None:
        """Verify user's answer against stored correct solution."""
    def get_correct_answer(self, storage: ITaskStorage) -> IAnswer: ...
    @property
    def result(self) -> IResult:
        """Return the representation of user answer check."""
