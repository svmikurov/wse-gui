"""Defines Index Math page model."""

from dataclasses import dataclass
from typing import Literal

from injector import inject
from typing_extensions import override
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core import MathEnum

from wse.apps.math.api.schema import (
    Calculation,
    CalculationCondition,
    CalculationConfig,
)
from wse.config.enums import TaskIO
from wse.feature.base.mixins import AddObserverGen

from .abc import MathModelFeature

_NotifyType = Literal[
    'exercises_updated',
    'exercise_selected',
    'exercise_started',
]


class _Feature(
    MathModelFeature,
    AddObserverGen[_NotifyType],
):
    """Index Math page model feature."""

    _exercises: list[ExerciseEnum]
    _current_exercise: ExerciseEnum

    @override
    def update_page_context(self) -> None:
        """Update page content."""
        self._notify('exercises_updated', values=self._exercises)
        self._notify('exercise_selected', value=self._current_exercise)

    @override
    def change_exercise(self, value: ExerciseEnum) -> None:
        """Change the exercise to perform."""
        self._current_exercise = value

    # TODO: Refactor, use only in development
    @override
    def start_exercise(self) -> None:
        """Handle the event to start exercise."""
        exercise = Calculation(
            question_url_path='/api/v1/math/exercise/calculation/',
            check_url_path='/api/v1/math/exercise/calculation/validate/',
            task_io=TaskIO.TEXT,
            condition=CalculationCondition(
                exercise_name=self._current_exercise,
                config=CalculationConfig(min_value='1', max_value='9'),
            ),
        )
        self._notify('exercise_started', value=exercise)


@inject
@dataclass
class MathModel(
    _Feature,
):
    """Index Math page model."""

    _exercises: list[ExerciseEnum]

    def __post_init__(self) -> None:
        """Construct the model."""
        self._default_exercise: ExerciseEnum = MathEnum.ADDING
        self._current_exercise: ExerciseEnum = self._default_exercise
