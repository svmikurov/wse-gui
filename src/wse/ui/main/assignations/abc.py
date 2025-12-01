"""Abstract base classes for Assigned exercises UI layer."""

from abc import ABC, abstractmethod
from typing import Literal

from wse.core.navigation.nav_id import NavID
from wse.data.schemas.exercise import ExerciseInfo
from wse.feature.observer.mixins import SubjectGen
from wse.ui.base.navigate import NavigateABC, OnCloseABC
from wse.ui.base.view.abc import ViewABC

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
    SubjectGen[AssignationsStateObserverABC, _StateNotifyT],
    NavigateABC,
    OnCloseABC,
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
    OnCloseABC,
    ABC,
):
    """ABC for Assigned exercises UI view."""
