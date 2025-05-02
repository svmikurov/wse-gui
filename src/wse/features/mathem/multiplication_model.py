"""Defines multiplication page model."""

import dataclasses
import logging

from wse.features.mathem.exercises.interfaces import IAnswerChecker, IExercise
from wse.features.mathem.multiplication_controller import UIName
from wse.interface.ifeatures import IContext, IModel
from wse.interface.iobserver import ISubject
from wse.interface.iui.itext import IDisplayModel

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class MultiplicationModel(IModel):
    """Multiplication page model."""

    exercise: IExercise
    _answer_checker: IAnswerChecker

    _subject: ISubject
    display_question: IDisplayModel
    display_answer: IDisplayModel
    _context: IContext

    def __post_init__(self) -> None:
        """Subscribe to notifications."""
        self.display_question.set_ui_name(UIName.QUESTION_DISPLAY)
        self.display_question.subject.add_listener(self)
        self.display_answer.set_ui_name(UIName.ANSWER_DISPLAY)
        self.display_answer.subject.add_listener(self)

    # Context

    def render_context(self) -> None:
        """Render the context to view."""
        self._set_context()
        self._notify_render_context()

    def _set_context(self) -> None:
        """Set view context for render into view."""
        self.display_answer.clean()
        self.exercise.create_task()
        self.context['question'] = self.exercise.task

    def _notify_render_context(self) -> None:
        """Notify controller to fill view with context."""
        self.change_ui_value(UIName.QUESTION_DISPLAY, self.context['question'])
        self.clean_ui_value(UIName.ANSWER_DISPLAY)

    # Exercise methods

    def check_answer(self) -> bool:
        """Check user answer."""
        user_answer = self.display_answer.text
        return self._answer_checker.check(user_answer, self.exercise.answer)

    # Notifications

    def change_ui_value(self, ui_name: UIName, value: str) -> None:
        """Change UI text value according UI name."""
        self.subject.notify('change_ui_value', ui_name=ui_name, value=value)

    def clean_ui_value(self, ui_name: UIName) -> None:
        """Change UI text value according UI name."""
        self.subject.notify('clean_ui_value', ui_name=ui_name)

    # Utility methods

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject

    @property
    def context(self) -> IContext:
        """Model subject."""
        return self._context
