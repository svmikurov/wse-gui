"""Foreign words study ViewModel."""

import logging
from dataclasses import dataclass
from typing import Any, Literal, override

from injector import inject

from wse.domain.foreign import (
    ExerciseAccessorT,
    ExerciseNotifyABC,
    WordStudyUseCaseABC,
)
from wse.feature.observer import UpdateObserverABC
from wse.feature.observer.accessor import NotifyAccessorGen
from wse.feature.observer.mixins import ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin

from . import StudyForeignViewModelABC

log = logging.getLogger(__name__)

_PresenterNotifyT = Literal['change']

NO_TEXT = ''


@inject
@dataclass
class StudyForeignViewModel(
    NavigateStateMixin,
    ObserverManagerGen[UpdateObserverABC[Any]],
    NotifyAccessorGen[_PresenterNotifyT, ExerciseAccessorT],
    ExerciseNotifyABC,
    StudyForeignViewModelABC,
):
    """Foreign words study ViewModel."""

    _study_case: WordStudyUseCaseABC

    def __post_init__(self) -> None:
        """Construct the ViewModel."""
        self._study_case.add_observer(self)

    def on_open(self) -> None:
        """Call methods on open the screen."""
        self._study_case.start()

    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._study_case.remove_observer(self)

    @override
    def exercise_updated(
        self,
        accessor: ExerciseAccessorT,
        value: str,
    ) -> None:
        self.notify('change', accessor=accessor, value=value)
