"""Defines exercise page model."""

import dataclasses

from wse.interface.iexercise import (
    IAnswer,
    IAnswerChecker,
    IExercise,
    ITaskConditionStorage,
    ITaskRenderer,
)
from wse.interface.ifeatures import IExerciseModel
from wse.interface.iobserver import ISubject
from wse.interface.iui.itext import IDisplayModel


@dataclasses.dataclass
class ExerciseModel(IExerciseModel):
    """Exercise page model."""

    # Exercise dependencies
    exercise: IExercise
    storage: ITaskConditionStorage
    render: ITaskRenderer
    checker: IAnswerChecker

    # MVC model dependencies
    _subject: ISubject
    display_question: IDisplayModel
    display_answer: IDisplayModel

    # Exercise logic

    def start_exercise(self) -> None:
        """Start exercise."""
        task_conditions = self.exercise.create_task()
        self.storage.save_task_conditions(task_conditions)
        task = task_conditions.task
        self.render.render_task(task)

    def handel_answer(self, user_answer: IAnswer) -> None:
        """Handel user answer."""
        result = self.checker.check_answer(user_answer, self.storage)
        self.render.render_result(result)
        if result.is_correct:
            self.start_exercise()

    # MVC model methods

    def on_open(self) -> None:
        """Call methods on page open event."""

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject
