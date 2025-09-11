"""Defines Index Math screen model."""

from dataclasses import dataclass, replace
from typing import Literal, TypedDict

import toga
from injector import inject
from typing_extensions import Unpack
from wse_exercises.core import MathEnum

from wse.apps.nav_id import NavID
from wse.core.interfaces import Navigable
from wse.data.repositories.calculation_exercise import (
    CalculationExerciseRepo,
)
from wse.domain.task import SetCalculationExerciseUseCase
from wse.feature.base.mixins import AddObserverGen

from .abc import MathModelFeature

_NotifyType = Literal[
    'exercises_updated',
    'exercise_selected',
]


class _DataFieldType(TypedDict, total=False):
    """Field types for Calculation UI state data."""

    current: str
    exercises: list[MathEnum]


@dataclass(frozen=True)
class MathIndexUIState:
    """Math index screen UI state data."""

    current: str
    exercises: list[MathEnum]


@inject
@dataclass
class MathIndexViewModel(
    MathModelFeature,
    AddObserverGen[_NotifyType],
):
    """Index Math screen model."""

    _navigator: Navigable

    _exercise_repo: CalculationExerciseRepo
    _set_exercise_case: SetCalculationExerciseUseCase

    def __post_init__(self) -> None:
        """Construct the model."""
        self._create_state_data()

    # API

    def update_context(self) -> None:
        """Update screen context."""
        self._notify('exercises_updated', values=self._data.exercises)
        self._notify('exercise_selected', value=self._data.current)

    # UI callback

    def change_exercise(self, selection: toga.Selection) -> None:
        """Change the exercise to perform."""
        self._set_exercise_case.set_default(selection.value.entry)
        self._update_data(current=selection)

    def start_exercise(self, _: toga.Button) -> None:
        """Handle the event to start exercise."""
        self._navigator.navigate(NavID.CALCULATION)

    # Observe navigate event

    def navigate(self, nav_id: NavID) -> None:
        """Handle the navigate event, callback."""
        self._navigator.navigate(nav_id=nav_id)

    # Utility

    def _create_state_data(self) -> None:
        """Create UI state data."""
        self._data = MathIndexUIState(
            current=self._exercise_repo.default,
            exercises=self._exercise_repo.exercises,
        )

    def _update_data(self, **new_data: Unpack[_DataFieldType]) -> None:
        """Update UI state data."""
        self._data = replace(self._data, **new_data)
