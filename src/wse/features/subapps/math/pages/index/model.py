"""Defines Index Math page model."""

from dataclasses import dataclass

from injector import inject
from typing_extensions import override
from wse_exercises.base.enums import ExerciseEnum
from wse_exercises.core import MathEnum

from wse.features.base import BaseModel
from wse.features.shared.containers.top_bar import TopBarModelMixin

from ...http import IMathAPI


@inject
@dataclass
class IndexMathModel(
    TopBarModelMixin,
    BaseModel,
):
    """Index Math page model."""

    _exercises: list[ExerciseEnum]
    _api: IMathAPI

    @override
    def __post_init__(self) -> None:
        """Construct the model."""
        super().__post_init__()
        self._default_exercise: ExerciseEnum = MathEnum.ADDING
        self._current_exercise: ExerciseEnum = self._default_exercise

    # Notifications about Self events

    def _notify_exercises_updated(self) -> None:
        self._notify('exercises_updated', values=self._exercises)

    def _notify_exercise_selected(self, value: ExerciseEnum) -> None:
        self._notify('exercise_selected', value=value)

    def _notify_exercise_started(self, value: ExerciseEnum) -> None:
        self._notify('exercise_started', value=value)

    # Api for controller

    def on_open(self) -> None:
        """Call methods when page opens."""
        self._update_page_context()

    def change_exersice(self, value: ExerciseEnum) -> None:
        """Change the exercise to perform."""
        self._current_exercise = value

    def start_exercise(self) -> None:
        """Handle the event to start exercise."""
        self._notify_exercise_started(value=self._current_exercise)

    # Update page context

    def _update_page_context(self) -> None:
        self._get_server_context()
        self._update_exercise_selection()

    def _update_exercise_selection(self) -> None:
        self._notify_exercises_updated()
        self._notify_exercise_selected(self._current_exercise)

    def _get_server_context(self) -> None:
        context = self._api.get_index_context()
        balance = context['balance']
        self._notify_balance_updated(balance)
        print(context)
