"""Abstract base classes for Assigned exercises UI layer."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.core.navigation.nav_id import NavID
from wse.feature.base.mixins import AddObserverGenT
from wse.feature.shared.schemas.exercise import ExerciseInfo
from wse.ui.base.abc import CloseScreenABC, NavigateABC, ViewABC

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
    NavigateABC,
    CloseScreenABC,
    ABC,
):
    """ABC for Assigned exercises ViewModel."""

    @abstractmethod
    def navigate(self, nav_id: NavID) -> None:
        """Notify to navigate."""


# View


class AssignationsViewABC(
    AssignationsStateObserverABC,
    ViewABC,
    CloseScreenABC,
    ABC,
):
    """ABC for Assigned exercises UI view."""
