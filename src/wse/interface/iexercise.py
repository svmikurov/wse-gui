"""Defines protocol interfaces for exercises."""

from typing import Protocol

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off

class ITask(Protocol):
    """Interface protocol defining the structure of an exercise task."""

class ITaskConditions(Protocol):
    """Interface protocol for managing task conditions."""
    @property
    def task(self) -> ITask:
        """Return the current task instance."""
    @task.setter
    def task(self, value: ITask) -> None: ...

class IAnswer(Protocol):
    """Interface protocol representing a user's answer to a task."""

class ICheckResult(Protocol):
    """Defines interface for answer validation results."""
    @property
    def is_correct(self) -> bool:
        """Whether the user's answer matches the correct solution."""
    @is_correct.setter
    def is_correct(self, value: bool) -> None: ...

class IOperandGenerator(Protocol):
    """Defines interface for generating numerical operands."""
    def generate_operand(self) -> int:
        """Generate an integer for use in exercise calculations."""

class ITaskConditionStorage(Protocol):
    """Defines interface for storage of task conditions."""
    def save_task_conditions(self, task_conditions: ITaskConditions) -> None:
        """Save the conditions of an exercise task to storage."""

class IExerciseRenderer(Protocol):
    """Defines interface for presentation of exercise components."""
    def render_task(self, task: ITask) -> None:
        """Display the current task to the user."""
    def render_result(self, result: ICheckResult) -> None:
        """Present the outcome of answer validation to the user."""

class IAnswerChecker(Protocol):
    """Defines interface for validating user answers solutions."""
    def check(
        self,
        answer: IAnswer,
        storage: ITaskConditionStorage,
    ) -> ICheckResult:
        """Verify user's answer against stored correct solution."""

class IExercise(Protocol):
    """Interface protocol for complete exercise lifecycle management."""
    def create_task(self) -> None:
        """Create and return a new task with its conditions."""
    @property
    def task_conditions(self) -> ITaskConditions:
        """Return the current task conditions instance."""
    @property
    def task(self) -> ITask:
        """Retrieve the current task instance."""
    @property
    def answer(self) -> IAnswer:
        """Get the verified correct answer for the current task."""
