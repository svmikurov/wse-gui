"""Defines ABC for exercise page MVC components."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from typing_extensions import override

from ..interfaces.imvc_exercise import (
    ExerciseModelFeatureProto,
)

ModelT = TypeVar('ModelT', bound='ExerciseModelFeatureProto')

# Model


class ExerciseModelFeatureABC(ABC):
    """Abstract base class for exercise page model."""

    @abstractmethod
    def update_task(self) -> None:
        """Start or update task."""

    @abstractmethod
    def set_answer(self, value: str) -> None:
        """Set the entered user answer."""

    @abstractmethod
    def check_answer(self) -> None:
        """Check the user's submitted answer."""


# Observing the model


class ExerciseModelObserverABC(ABC):
    """Abstract base class of exercise model event observer."""

    @abstractmethod
    def task_updated(self, value: str) -> None:
        """Handle the model event on task update."""

    @abstractmethod
    def answer_updated(self, value: str) -> None:
        """Handle the model event on answer update."""

    @abstractmethod
    def answer_incorrect(self, value: str) -> None:
        """Handle the model event on success answer checking."""


# Observing the view


class ExerciseViewObserverABC(ABC):
    """ABC for exercise view event observer."""

    @abstractmethod
    def task_started(self) -> None:
        """Handle the event of view on task start."""

    @abstractmethod
    def answer_entered(self, value: str) -> None:
        """Handle the event of view on answer enter."""

    @abstractmethod
    def answer_submitted(self) -> None:
        """Handle the event of view on answer submit."""


class ExerciseViewObserver(ExerciseViewObserverABC, Generic[ModelT]):
    """Mixin providing observe of calculation view event."""

    _model: ModelT

    @override
    def task_started(self) -> None:
        """Handle the event of view on task start."""
        self._model.update_task()

    @override
    def answer_entered(self, value: str) -> None:
        """Handle the event of view on answer enter."""
        self._model.set_answer(value)

    @override
    def answer_submitted(self) -> None:
        """Handle the event of view on answer submit."""
        self._model.check_answer()
