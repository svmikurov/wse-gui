"""Defines ABC for exercise page MVC components."""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from typing_extensions import override

from ..interfaces.imvc_exercise import (
    ExerciseModelFeatureProto,
    ExerciseModelObserverProto,
    ExerciseViewObserverProto,
)

ModelT = TypeVar('ModelT', bound='ExerciseModelFeatureProto')

# Model


class ExerciseModelFeature(ABC, ExerciseModelFeatureProto):
    """Abstract base class for exercise page model."""

    @abstractmethod
    @override
    def update_task(self) -> None:
        """Start or update task."""

    @abstractmethod
    @override
    def set_answer(self, value: str) -> None:
        """Set the entered user answer."""

    @abstractmethod
    @override
    def check_answer(self) -> None:
        """Check the user's submitted answer."""


# Observing the model


class ExerciseModelObserver(ABC, ExerciseModelObserverProto):
    """Abstract base class of exercise model event observer."""

    @abstractmethod
    @override
    def task_updated(self, value: str) -> None:
        """Handle the model event on task update."""

    @abstractmethod
    @override
    def answer_updated(self, value: str) -> None:
        """Handle the model event on answer update."""

    @abstractmethod
    @override
    def answer_incorrect(self, value: str) -> None:
        """Handle the model event on success answer checking."""


# Observing the view


class BaseExerciseViewObserver(ABC, ExerciseViewObserverProto):
    """ABC for exercise view event observer."""

    @abstractmethod
    @override
    def task_started(self) -> None:
        """Handle the event of view on task start."""

    @abstractmethod
    @override
    def answer_entered(self, value: str) -> None:
        """Handle the event of view on answer enter."""

    @abstractmethod
    @override
    def answer_submitted(self) -> None:
        """Handle the event of view on answer submit."""


class ExerciseViewObserver(BaseExerciseViewObserver, Generic[ModelT]):
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
