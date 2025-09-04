"""Base Exercise page model."""

import logging
from typing import Generic, Literal

from typing_extensions import override

from wse.feature.base.mixins import AddObserverGeneric
from wse.feature.services import (
    Answer,
    Question,
)

from .protocol import (
    ExerciseModelProto,
    ExerciseT_contra,
    ServiceT,
)

logger = logging.getLogger(__name__)

NO_QUESTION = ''
NO_ANSWER = ''

_NotifyType = Literal[
    'task_updated',
    'answer_updated',
    'answer_incorrect',
]
"""Literal types to notifying model observer.
"""


class ExerciseModel(
    AddObserverGeneric[_NotifyType],
    ExerciseModelProto[ExerciseT_contra],
    Generic[ExerciseT_contra, ServiceT],
):
    """Exercise page model."""

    _exercise_service: ServiceT

    _exercise_meta: ExerciseT_contra | None = None
    _task: Question | None = None
    _user_answer: str = NO_ANSWER

    @override
    def set_exercise(self, exercise_meta: ExerciseT_contra) -> None:
        """Set the exercise with and it conditions."""
        self._exercise_meta = exercise_meta
        self._reset_task_state()
        self.update_task()

    @override
    def update_task(self) -> None:
        """Start or update task."""
        if not self._exercise_meta:
            logger.error('Exercise not set, aborting task update')
            return

        self._task, related_data = self._exercise_service.get_task(
            self._exercise_meta,
        )
        if isinstance(self._task, Question):
            self._notify('task_updated', value=self._task.question)
            self.set_answer(NO_ANSWER)

    @override
    def set_answer(self, value: str) -> None:
        """Set the entered user answer."""
        self._user_answer = value
        self._notify('answer_updated', value=value)

    @override
    def check_answer(self) -> None:
        """Check the user submitted answer."""
        if self._user_answer == NO_ANSWER:
            # Checking for empty answers is ignored.
            return

        if self._task is None or self._exercise_meta is None:
            logger.error(
                f'Answer check error ({self._task = }; '
                f'{self._exercise_meta = })'
            )
            return

        answer = Answer(uid=self._task.uid, answer=self._user_answer)

        result, related_data = self._exercise_service.check_answer(
            answer,
            self._exercise_meta,
        )

        if result:
            if result.is_correct:
                self.update_task()
            else:
                self._notify(
                    'answer_incorrect',
                    value=f'{self._task.question} = {result.correct_answer}',
                )

    def _reset_task_state(self) -> None:
        self._task = None
        self._notify('task_updated', value=NO_QUESTION)
        self.set_answer(NO_ANSWER)
