"""Defines Simple Math calculation page model."""

import logging

from injector import inject

from wse.features.base.mixins import AddObserverMixin
from wse.features.exceptions import ExerciseError
from wse.features.interfaces import ISubject
from wse.features.services.interfaces import IExerciseService, ITask

logger = logging.getLogger(__name__)


@inject
class SimpleCalcModel(
    AddObserverMixin,
):
    """Simple Math calculation page model."""

    def __init__(
        self,
        subject: ISubject,
        exercise: IExerciseService,
    ) -> None:
        """Construct the model."""
        self._subject = subject
        self._exercise = exercise
        self._task: ITask | None = None

    # Exercise methods

    def _start_exercise(self) -> None:
        self._get_task()
        try:
            self._display_question()
        except ExerciseError:
            logger.exception('Question display error')

    def _get_task(self) -> None:
        self._task = self._exercise.get_task()

    # Notifications about Model events

    def _display_question(self) -> None:
        if self._task is not None:
            self._notify('question_updated', value=self._task.question)
        else:
            raise ExerciseError('Task is not defined')

    def _clear_question(self) -> None:
        self._notify('question_cleared')

    def _display_answer(self, value: str) -> None:
        self._notify('answer_updated', value=value)

    def _clear_answer(self) -> None:
        self._notify('answer_cleared')

    # API for controller

    def on_open(self) -> None:
        """Call model methods when page opens."""
        self._start_exercise()

    def handle_answer_input(self, value: str) -> None:
        """Handel the user answer input."""
        self._display_answer(value)

    def check_answer(self) -> None:
        """Check the user's confirmed answer."""
        pass

    # Utility methods

    def _notify(self, notification: str, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)
