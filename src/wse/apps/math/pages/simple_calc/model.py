"""Defines Simple Math calculation page model."""

import logging
from dataclasses import dataclass

import httpx
from injector import inject
from typing_extensions import override
from wse_exercises.base.enums import ExerciseEnum

from wse.apps.math.pages.simple_calc.dto import CalcTaskDTO
from wse.core.exceptions import ExerciseError
from wse.features.base import BaseModel
from wse.features.services.interfaces import ICalcService

logger = logging.getLogger(__name__)

NO_TEXT = ''


@inject
@dataclass
class CalcModel(
    BaseModel,
):
    """Simple Math calculation page model."""

    _exercise_service: ICalcService

    @override
    def __post_init__(self) -> None:
        """Construct the model."""
        super().__post_init__()
        self._user_answer: str = NO_TEXT
        self._task: CalcTaskDTO | None = None
        self._current_exercise: ExerciseEnum | None = None

    # Business logic

    def start_new_task(self) -> None:
        """Start new task."""
        self._clear()

        try:
            self._set_task()
            self._notify_display_question()
        except ExerciseError:
            logger.error('Create task error')

    def _set_task(self) -> None:
        if self.current_exercise is None:
            raise ExerciseError('Current exercise is not defined')

        data = {
            'exercise_name': self._current_exercise,
            'config': {
                'min_value': '1',
                'max_value': '9',
            },
        }

        self._task = self._exercise_service.get_task(data)

    def _check_answer(self) -> None:
        if self._task is None:
            logger.error('Task is undefined')
            raise ExerciseError('Task is undefined')

        try:
            result_dto = self._exercise_service.check_answer(self._user_answer)

        except httpx.HTTPStatusError as e:
            logger.exception(f'Exercise service error:\n{e}')

        except ValueError:
            logger.exception('Entered answer error')

        else:
            self._clear_answer()

            if result_dto.is_correct:
                self._handle_correct_user_answer()

            else:
                self._handle_incorrect_user_answer(
                    f'{self._task.question} = {result_dto.correct_answer}'
                )

    def _handle_correct_user_answer(self) -> None:
        self.start_new_task()

    def _handle_incorrect_user_answer(self, correct_answer: str) -> None:
        self._notify_display_correct_answer(correct_answer)
        self._notify_clear_answer()

    def _clear(self) -> None:
        self._clear_question()
        self._clear_answer()

    def _clear_question(self) -> None:
        self._notify_clear_answer()

    def _clear_answer(self) -> None:
        self._user_answer = NO_TEXT
        self._notify_clear_answer()

    # Notifications about Self events

    def _notify_display_question(self) -> None:
        if self._task is not None:
            self._notify('question_updated', value=self._task.question)
        else:
            raise ExerciseError('Task is not defined')

    def _notify_clear_question(self) -> None:
        self._notify('question_cleared')

    def _notify_display_answer(self, value: str) -> None:
        self._notify('answer_updated', value=value)

    def _notify_clear_answer(self) -> None:
        self._notify('answer_cleared')

    def _notify_display_correct_answer(self, value: str) -> None:
        self._notify('correct_answer_received', value=value)

    # API for controller

    def on_open(self, exercise: ExerciseEnum) -> None:
        """Call model methods when page opens."""
        self._current_exercise = exercise
        self.start_new_task()

    def handle_answer_input(self, value: str) -> None:
        """Handel the user answer input."""
        self._user_answer = value
        self._notify_display_answer(value)

    def handle_submit(self) -> None:
        """Check the user's confirmed answer."""
        if self._user_answer:
            self._check_answer()
        else:
            # Ignore event
            pass

    # Properties

    @property
    def current_exercise(self) -> ExerciseEnum | None:
        """Current exercise to do."""
        return self._current_exercise

    @current_exercise.setter
    def current_exercise(self, value: ExerciseEnum) -> None:
        self._current_exercise = value
