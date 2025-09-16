"""Assigned exercises UI state."""

import logging
from dataclasses import dataclass, replace
from typing import TypedDict

from injector import inject
from typing_extensions import Unpack, override

from wse.core.interfaces import Navigable
from wse.core.navigation.nav_id import NavID
from wse.domain.abc import SetAssignedExerciseUseCaseABC
from wse.feature.api.main.abc import AssignationsApiABC
from wse.feature.shared.schemas.exercise import (
    Assigned,
    ExerciseInfo,
)

from .abc import AssignationsViewModelABC

audit = logging.getLogger(__name__)


class _DataFieldType(TypedDict, total=False):
    """Fields for Assigned exercises UI state data."""

    exercises: list[ExerciseInfo]


@dataclass(frozen=True)
class _AssignationsUIState:
    """Assigned exercises UI state data."""

    exercises: list[ExerciseInfo] | None = None


@inject
@dataclass
class AssignationsViewModel(AssignationsViewModelABC):
    """Assignations of exercises UI the ViewModel."""

    _navigator: Navigable
    _api_service: AssignationsApiABC
    _assigned_exercise_case: SetAssignedExerciseUseCaseABC

    def __post_init__(self) -> None:
        """Construct the state."""
        self._create_data()

    # TODO: Move to base class.
    def refresh_context(self) -> None:
        """Refresh screen context."""
        self._fetch_exercises()

    @override
    def start_exercise(self, assignation_id: str) -> None:
        """Start selected assigned exercise.."""
        if assigned_exercise := self._fetch_exercise(assignation_id):
            self._assigned_exercise_case.set_exercise(assigned_exercise)
            self._navigator.navigate(nav_id=NavID.EXERCISE)

    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""
        self._navigator.navigate(nav_id=nav_id)

    # Utility methods

    def _fetch_exercises(self) -> None:
        """Fetch assigned exercises."""
        if exercises := self._api_service.request_all_exercises():
            self._update_data(exercises=exercises)

        if self._data.exercises is not None:
            self._notify('exercises_updated', exercises=self._data.exercises)

    def _fetch_exercise(
        self,
        assignation_id: str,
    ) -> Assigned | None:
        """Fetch assigned exercise meta data."""
        return self._api_service.request_selected(assignation_id)

    # TODO: Move to ABC Generic[...UIState] class.
    def _create_data(self) -> None:
        """Create UI state data."""
        self._data = _AssignationsUIState()

    # TODO: Move to ABC Generic[...UIState] class.
    def _update_data(self, **data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        self._data = replace(self._data, **data)

    def on_close(self) -> None:
        """Call methods before close the screen."""
        audit.debug(
            f'Not implemented `on_close()` for {self.__class__.__name__}'
        )
