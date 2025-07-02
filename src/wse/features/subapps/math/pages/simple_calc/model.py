"""Defines Simple Math calculation page model."""

import logging
from dataclasses import dataclass

from injector import inject
from typing_extensions import override
from wse_exercises.core.mathem.enums import Exercises
from wse_exercises.core.mathem.interfaces import ISimpleCalcTask

from wse.features.base import BaseModel
from wse.features.exceptions import ExerciseError
from wse.features.services.interfaces import ISimpleCalcService
from wse.features.subapps.math.pages.simple_calc.interfaces import (
    ISimpleCalcModel,
)

logger = logging.getLogger(__name__)

NO_TEXT = ''


@inject
@dataclass
class SimpleCalcModel(
    BaseModel,
    ISimpleCalcModel,
):
    """Simple Math calculation page model."""

    _exercise_service: ISimpleCalcService

    @override
    def __post_init__(self) -> None:
        """Construct the model."""
        super().__post_init__()
        self._user_answer: str = NO_TEXT
        self._task: ISimpleCalcTask | None = None
        self._current_exercise: Exercises | None = None

    # Business logic

    def _start_new_task(self) -> None:
        try:
            self._get_task()
            self._notify_display_question()
        except ExerciseError as e:
            logger.error('Create task error:\n%s', str(e))

    def _get_task(self) -> None:
        if self.current_exercise is None:
            raise ExerciseError('Current exercise is not defined')

        self._task = self._exercise_service.get_task(self.current_exercise)

    def _check_answer(self) -> None:
        if self._task is not None:
            is_correct = self._exercise_service.check_answer(
                self._user_answer,
                self._task,
            )

            if is_correct:
                self._handle_correct_user_answer()
            else:
                # TODO: Add event handling
                pass

        else:
            # Ignore event
            pass

    def _handle_correct_user_answer(self) -> None:
        self._clear_answer()
        self._start_new_task()

    def _clear_answer(self) -> None:
        self._user_answer = NO_TEXT
        self._notify_clear_answer()

    # Notifications about Self events

    def _notify_display_question(self) -> None:
        if self._task is not None:
            self._notify('question_updated', value=self._task.question.text)
        else:
            raise ExerciseError('Task is not defined')

    def _notify_clear_question(self) -> None:
        self._notify('question_cleared')

    def _notify_display_answer(self, value: str) -> None:
        self._notify('answer_updated', value=value)

    def _notify_clear_answer(self) -> None:
        self._notify('answer_cleared')

    # API for controller

    @override
    def on_open(self, exercise: Exercises) -> None:
        """Call model methods when page opens."""
        self._current_exercise = exercise
        self._start_new_task()

    @override
    def handle_answer_input(self, value: str) -> None:
        """Handel the user answer input."""
        self._user_answer = value
        self._notify_display_answer(value)

    @override
    def handle_submit(self) -> None:
        """Check the user's confirmed answer."""
        if self._user_answer:
            self._check_answer()
        else:
            # Ignore event
            pass

    # Properties

    @property
    def current_exercise(self) -> Exercises | None:
        """Current exercise to do."""
        return self._current_exercise

    @current_exercise.setter
    def current_exercise(self, value: Exercises) -> None:
        self._current_exercise = value
