"""Abstract base classes for Assigned exercises UI layer."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.feature.base.mixins import AddObserverGenT
from wse.feature.base.mvc import ViewABC
from wse.feature.shared.containers.top_bar import TopBarViewMixin
from wse.feature.shared.schemas.exercise import ExerciseInfo

# State

_StateNotifyT = Literal['exercises_updated']


class AssignationsStateFeatureABC(ABC):
    """ABC for Assigned exercises UI state feature."""

    @abstractmethod
    def refresh_context(self) -> None:
        """Refresh screen context."""

    @abstractmethod
    def start_exercise(self, assignation_id: str) -> None:
        """Start selected exercise."""


class AssignationsStateObserverABC(ABC):
    """ABC for Assigned exercises IU state observer."""

    @abstractmethod
    def exercises_updated(self, exercises: list[ExerciseInfo]) -> None:
        """Handle the 'assigned exercises updated' the state event."""


class AssignationsViewModelABC(
    AssignationsStateFeatureABC,
    AddObserverGenT[AssignationsStateObserverABC, _StateNotifyT],
    ABC,
):
    """ABC for Assigned exercises ViewModel."""


# View


class AssignationsViewABC(
    TopBarViewMixin,
    AssignationsStateObserverABC,
    ViewABC,
    ABC,
):
    """ABC for Assigned exercises UI view."""
