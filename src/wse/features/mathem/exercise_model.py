"""Defines exercise page model."""

import dataclasses
import logging

from wse.features.shared.enums.ui_names import UIName
from wse.interface.iexercise import (
    IAnswer,
    IAnswerChecker,
    IExercise,
    IExerciseRenderer,
    ITaskConditionStorage,
)
from wse.interface.ifeatures import IExerciseModel
from wse.interface.iobserver import ISubject
from wse.interface.iui.itext import IDisplayModel

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class ExerciseModel(IExerciseModel):
    """Exercise page model."""

    # Exercise dependencies
    exercise: IExercise
    storage: ITaskConditionStorage
    render: IExerciseRenderer
    checker: IAnswerChecker

    # MVC model dependencies
    _subject: ISubject
    display_question: IDisplayModel
    display_answer: IDisplayModel

    def __post_init__(self) -> None:
        """Subscribe to notifications."""
        self.display_question.set_ui_name(UIName.QUESTION_DISPLAY)
        self.display_question.subject.add_listener(self)
        self.display_answer.set_ui_name(UIName.ANSWER_DISPLAY)
        self.display_answer.subject.add_listener(self)

    # Exercise logic

    def start_exercise(self) -> None:
        """Start exercise."""
        self.exercise.create_task()
        task_conditions = self.exercise.task_conditions
        self.storage.save_task_conditions(task_conditions)
        task = task_conditions.task
        self.render.render_task(task)

    def handel_answer(self) -> None:
        """Handel user answer."""
        user_answer = self.get_user_answer()
        result = self.checker.check(user_answer, self.storage)
        self.render.render_result(result)
        if result.is_correct:
            self.start_exercise()

    def get_user_answer(self) -> IAnswer:
        """Get user answer."""

    # MVC model methods

    def on_open(self) -> None:
        """Call methods on page open event."""
        logger.debug('On open called')
        self.start_exercise()

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject

    # -=== Notifications by UI name ===-

    def change_ui_value(self, ui_name: UIName, value: str) -> None:
        """Change UI text value according UI name."""
        self.subject.notify('change_ui_value', ui_name=ui_name, value=value)

    def clean_ui_value(self, ui_name: UIName) -> None:
        """Change UI text value according UI name."""
        self.subject.notify('clean_ui_value', ui_name=ui_name)
