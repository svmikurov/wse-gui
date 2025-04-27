"""Defines protocol interfaces for exercises."""

from typing import Protocol

from wse.interface.ifeatures import IListener, ISubject

# ruff: noqa: D101, D102, E302
# fmt: off

class ITaskCreator(Protocol):
    """Defines interface for task creation functionality."""

    def create_task(self) -> None:
        """Generate and initialize a new task."""

class IOperandGenerator(Protocol):
    """Defines interface for numerical operand generation."""

    def generate_operand(self) -> int:
        """Generate a numerical value for use in calculations."""

class ITaskRenderer(Protocol):
    """Defines interface for task presentation functionality."""

    def render_task(self) -> None:
        """Display/formats the current task for user interaction."""

class IAnswerChecker(Protocol):
    """Defines interface for answer validation functionality."""

    def check_answer(self, answer: str) -> bool:
        """Verify user's answer against correct solution."""

class ILessonStarter(Protocol):
    """Defines interface to start lesson."""

    def start_lesson(self, listener: IListener) -> None:
        """Subscribe a listener and start a lesson."""

class IExercise(ITaskCreator, IAnswerChecker, Protocol):
    """Interface protocol for complete exercise management."""

    @property
    def task(self) -> str:
        """Get text representation of the current task."""

    @property
    def answer(self) -> str:
        """Get correct answer for the current task."""

    def check_answer(self, answer: str) -> bool:
        """Verify user's answer against correct solution."""

class ICalcExercise(IExercise, IOperandGenerator, Protocol):
    """Extended interface for arithmetic-based exercises."""

class ILesson(
    ITaskCreator,
    ITaskRenderer,
    IAnswerChecker,
    ISubject,
    ILessonStarter,
    Protocol,
):
    """Comprehensive interface for exercise lifecycle management."""

# fmt: on
