"""Abstract base classes for Index Math page components."""

from abc import ABC, abstractmethod

from wse_exercises.base.enums import ExerciseEnum

from wse.apps.math.api import Calculation

# Model


class MathModelFeature(ABC):
    """Abstract base classes for Index Math page model feature."""

    @abstractmethod
    def update_page_context(self) -> None:
        """Update page content."""

    @abstractmethod
    def change_exercise(self, value: ExerciseEnum) -> None:
        """Change the exercise to perform."""

    @abstractmethod
    def start_exercise(self) -> None:
        """Handle the event to start exercise."""


class MathModelObserver(ABC):
    """Protocol for Index Math page model observer interface."""

    @abstractmethod
    def exercises_updated(self, values: list[ExerciseEnum]) -> None:
        """Update exercises select data source."""

    @abstractmethod
    def exercise_selected(self, value: ExerciseEnum) -> None:
        """Set selected exercise to choices."""


class MathModelNavigateObserver(ABC):
    """Protocol for Index Math page model observer interface."""

    @abstractmethod
    def exercise_started(self, value: Calculation) -> None:
        """Navigate to exercise page."""
