"""Defines Simple Math calculation page model."""

import logging

from injector import inject
from wse_exercises.core.mathem.interfaces import ISimpleCalcTask

from wse.features.base.mixins import AddObserverMixin
from wse.features.exceptions import ExerciseError
from wse.features.interfaces import ISubject
from wse.features.services.interfaces import ISimpleCalcService

logger = logging.getLogger(__name__)

NO_TEXT = ''


@inject
class SimpleCalcModel(
    AddObserverMixin,
):
    """Simple Math calculation page model."""

    def __init__(
        self,
        subject: ISubject,
        exercise_service: ISimpleCalcService,
    ) -> None:
        """Construct the model."""
        self._subject = subject
        self._exercise_service = exercise_service
        self._user_answer: str = NO_TEXT
        self._task: ISimpleCalcTask | None = None

    # Business logic

    def _start_new_task(self) -> None:
        self._task = self._exercise_service.get_task()

        try:
            self._notify_display_question()
        except ExerciseError:
            logger.exception('Question display error')

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

    def on_open(self) -> None:
        """Call model methods when page opens."""
        self._start_new_task()

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

    # Utility methods

    def _notify(self, notification: str, **kwargs: object) -> None:
        self._subject.notify(notification, **kwargs)
