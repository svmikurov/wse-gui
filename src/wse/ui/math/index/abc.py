"""Abstract base classes for Index Math page components."""

from abc import ABC, abstractmethod

import toga
from wse_exercises.core import MathEnum

from wse.feature.api.math import Calculation
from wse.feature.base import ViewABC
from wse.ui.base.abc import CloseScreenABC

# ViewModel


class MathModelFeature(ABC):
    """ABC for Index Math screen model feature."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh screen content."""

    @abstractmethod
    def change_exercise(self, value: MathEnum) -> None:
        """Change the exercise to perform."""

    @abstractmethod
    def start_exercise(self, _: toga.Button) -> None:
        """Handle the event to start exercise."""


class MathModelObserver(ABC):
    """Protocol for Index Math screen model observer interface."""

    @abstractmethod
    def exercises_updated(self, values: list[MathEnum]) -> None:
        """Update exercises select data source."""

    @abstractmethod
    def exercise_selected(self, value: MathEnum) -> None:
        """Set selected exercise to choices."""


class MathModelNavigateObserver(ABC):
    """Protocol for Index Math screen model observer interface."""

    @abstractmethod
    def exercise_started(self, value: Calculation) -> None:
        """Navigate to exercise screen."""


class MathIndexModelViewABC(
    CloseScreenABC,
    ABC,
):
    """ABC for Math index screen View."""


# View


class MathIndexViewABC(
    MathModelObserver,
    ViewABC,
    CloseScreenABC,
    ABC,
):
    """ABC for Math index screen View."""
