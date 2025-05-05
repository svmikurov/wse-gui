"""Defines exercise page model."""

import dataclasses
import logging

from wse.features.mathem.exercises.task import Answer
from wse.features.shared.enums import UIName
from wse.interface.iexercise import (
    IAnswerChecker,
    IExercise,
    ITaskStorage,
    ITextDisplayRenderer,
)
from wse.interface.ifeatures import IExerciseModel
from wse.interface.iobserver import ISubject
from wse.interface.iui.itext import IDisplayModel

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class CalculationModel(IExerciseModel):
    """Multiplication exercise page model."""

    # Exercise dependencies
    exercise: IExercise
    storage: ITaskStorage
    render: ITextDisplayRenderer
    checker: IAnswerChecker

    # MVC model dependencies
    _subject: ISubject
    display_question: IDisplayModel
    display_answer: IDisplayModel
    display_info: IDisplayModel

    def __post_init__(self) -> None:
        """Subscribe to notifications."""
        self.display_question.subscribe(UIName.QUESTION_DISPLAY, self)
        self.display_answer.subscribe(UIName.ANSWER_DISPLAY, self)
        self.display_info.subscribe(UIName.INFO_DISPLAY, self)

    # Exercise logic

    def start_exercise(self) -> None:
        """Start exercise."""
        task = self.exercise.create_task()
        self.storage.save_task(task)
        self.render.render(task.question.text, self.display_question)

    def handle_answer(self) -> None:
        """Handel user answer."""
        # Get the result of the user solution checking
        user_answer = Answer(self.display_answer.text)
        self.checker.check(user_answer, self.storage)
        result = self.checker.result

        # Render the result of the check
        self.render.render(result.text, self.display_info)

        # Restart the exercise if the user solution is correct
        if result.is_correct:
            self.start_exercise()
            self.display_answer.clean()

    # MVC model methods

    def on_open(self) -> None:
        """Call methods on page open event."""
        self.start_exercise()
        self.display_answer.clean()
        self.display_info.clean()

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
