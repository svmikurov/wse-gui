"""Defines protocol interfaces for exercises."""

from typing import Protocol

from wse.interface.ifeatures import ISubject
from wse.interface.iobserver import IListener

# ruff: noqa: D101, D102, D204, E301, E302
# fmt: off

class ITaskCreator(Protocol):
    """Defines interface for task creation functionality."""
    def create_task(self) -> None:
        """Generate and initialize a new task."""

class IOperandGenerator(Protocol):
    """Defines interface for numerical operand generation."""
    def generate_operand(self) -> int:
        """Generate a numerical value for use in calculations."""

class ITaskConditionStorage(Protocol):
    """Defines interface for task condition storage."""

class ITaskRenderer(Protocol):
    """Defines interface for task presentation functionality."""
    def render_task(self) -> None:
        """Display/formats the current task for user interaction."""

class IAnswerChecker(Protocol):
    """Defines interface for answer validation functionality."""
    def check_answer(self, answer: str) -> bool:
        """Verify user's answer against correct solution."""

class IResultReporter:
    """Defines interface for result reporter."""

class IExercise(Protocol):
    """Interface protocol for complete exercise management."""
    @property
    def task(self) -> str:
        """Get text representation of the current task."""
    @property
    def answer(self) -> str:
        """Get correct answer for the current task."""
