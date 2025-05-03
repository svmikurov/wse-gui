"""Defines protocol interfaces for exercises."""

from typing import Protocol

from wse.interface.ifeatures import ISubject
from wse.interface.iobserver import IListener

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off

class ITask(Protocol):
    """Interface protocol for exercise task."""

class ITaskConditions(Protocol):
    """Interface protocol for task conditions."""
    @property
    def task(self) -> ITask:
        """Get text representation of the current task."""

class IAnswer(Protocol):
    """Interface protocol for answer."""

class ICheckResult(Protocol):
    """Defines interface for result of answer validation."""
    @property
    def is_correct(self) -> bool:
        """Is user answer is correct."""

class IOperandGenerator(Protocol):
    """Defines interface for numerical operand generation."""
    def generate_operand(self) -> int:
        """Generate a numerical value for use in calculations."""

class ITaskConditionStorage(Protocol):
    """Defines interface for task condition storage."""
    def save_task_conditions(self, task_conditions: ITaskConditions) -> None:
        """Save a exercise task conditions."""

class ITaskRenderer(Protocol):
    """Defines interface for task presentation functionality."""
    def render_task(self, task: ITask) -> None:
        """Render the current task for user interaction."""
    def render_result(self, result: ICheckResult) -> None:
        """Render the report of task result validation."""

class IAnswerChecker(Protocol):
    """Defines interface for answer validation functionality."""
    def check_answer(
        self,
        answer: IAnswer,
        storage: ITaskConditionStorage,
    ) -> ICheckResult:
        """Verify user's answer against correct solution."""

class IExercise(Protocol):
    """Interface protocol for complete exercise management."""
    def create_task(self) -> ITaskConditions:
        """Create task."""
    @property
    def task(self) -> ITask:
        """Get text representation of the current task."""
    @property
    def answer(self) -> IAnswer:
        """Get correct answer for the current task."""
