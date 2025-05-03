"""Defines exercise page model."""

import dataclasses

from wse.interface.iexercise import (
    IAnswerChecker,
    IExercise,
    IResultReporter,
    ITaskConditionStorage,
    ITaskCreator,
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
    creator: ITaskCreator
    storage: ITaskConditionStorage
    render: ITaskRenderer
    checker: IAnswerChecker
    reporter: IResultReporter

    # MVC model dependencies
    _subject: ISubject
    display_question: IDisplayModel
    display_answer: IDisplayModel

    # MVC model methods

    def on_open(self) -> None:
        """Call methods on page open event."""

    @property
    def subject(self) -> ISubject:
        """Model subject."""
        return self._subject
