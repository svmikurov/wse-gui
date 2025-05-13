"""Defines the Model for the Multiplication Exercise page."""

import logging
from dataclasses import dataclass

from wse.features.mathem.exercises.task import UserAnswer
from wse.features.mathem.interfaces.iexercise import IExerciseSwitcher
from wse.features.mathem.interfaces.ipages import (
    ICalculationModel,
)
from wse.features.mathem.interfaces.isubjects import ICalculationSubject
from wse.features.shared.enums.task import TaskState
from wse.interface.iexercise import (
    IAnswerChecker,
    ITaskStorage,
    ITextDisplayRenderer,
)

logger = logging.getLogger(__name__)


@dataclass
class CalculationModel(ICalculationModel):
    """Multiplication exercise page model."""

    # Exercise dependencies
    exercise_switcher: IExerciseSwitcher
    storage: ITaskStorage
    render: ITextDisplayRenderer
    checker: IAnswerChecker

    # MVC model dependencies
    _subject: ICalculationSubject

    def __post_init__(self) -> None:
        """Initialise attributes."""
        self._user_answer: str = ''
        self._task_state = TaskState.NO_TASK

    def start_exercise(self) -> None:
        """Initialize a new exercise task."""
        exercise = self.exercise_switcher.current_exercise
        task = exercise.create_task()
        self.storage.save_task(task)
        self._task_state = TaskState.QUESTION
        self.subject.notify_task_created(task.question.text)

    def handle_answer(self, user_input: str) -> None:
        """Handel user answer."""
        # Get the result of the user solution checking
        self.checker.check(
            UserAnswer(user_input),
            self.storage,
        )
        result = self.checker.result

        # Render the result of the check
        self.subject.notify_answer_checked(result.text)

        # Restart the exercise if the user solution is correct
        if result.is_correct:
            self.subject.notify_page_cleared()
            self._task_state = TaskState.NO_TASK
            self.start_exercise()
        else:
            self._task_state = TaskState.FAILED

    # Properties

    @property
    def subject(self) -> ICalculationSubject:
        """Get the model's subject instance."""
        return self._subject
