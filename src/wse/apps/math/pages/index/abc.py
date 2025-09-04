"""Abstract base classes for Index Math page components."""

from abc import ABC, abstractmethod

from typing_extensions import override
from wse_exercises.base.enums import ExerciseEnum

from wse.apps.math.api import Calculation

from ..index import (
    MathModelFeatureProto,
    MathModelObserverProto,
)

# Model


class MathModelFeature(ABC, MathModelFeatureProto):
    """Abstract base classes for Index Math page model feature."""

    @abstractmethod
    @override
    def update_page_context(self) -> None:
        """Update page content."""

    @abstractmethod
    @override
    def change_exercise(self, value: ExerciseEnum) -> None:
        """Change the exercise to perform."""

    @abstractmethod
    @override
    def start_exercise(self) -> None:
        """Handle the event to start exercise."""


class MathModelObserver(ABC, MathModelObserverProto):
    """Protocol for Index Math page model observer interface."""

    @abstractmethod
    @override
    def exercises_updated(self, values: list[ExerciseEnum]) -> None:
        """Update exercises select data source."""

    @abstractmethod
    @override
    def exercise_selected(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""


class MathModelNavigateObserver(ABC, MathModelObserverProto):
    """Protocol for Index Math page model observer interface."""

    @abstractmethod
    @override
    def exercise_started(self, value: Calculation) -> None:
        """Navigate to exercise page."""


# View
