"""Foreign words study ViewModel."""

import logging
from dataclasses import dataclass
from typing import override

from injector import inject

from wse.domain.foreign import (
    ExerciseAccessorT,
    WordStudyUseCaseABC,
)
from wse.feature.observer import ChangeObserverABC
from wse.feature.observer.generic import HandleObserverABC
from wse.feature.observer.mixins import NotifyGen, ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.control import Action
from wse.utils import decorators

from . import PresenterNotifyT, StudyForeignViewModelABC

log = logging.getLogger(__name__)

NO_TEXT = ''


@inject
@dataclass
class StudyForeignViewModel(
    NavigateStateMixin,
    ObserverManagerGen[
        ChangeObserverABC[PresenterNotifyT] | HandleObserverABC[Action],
    ],
    NotifyGen[PresenterNotifyT | Action],
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

    @decorators.log_unimplemented_call
    @override
    def handle(self, action: Action) -> None:
        """Handle user action."""
        match action:
            case Action.PAUSE:
                pass
            case Action.NEXT:
                pass
            case Action.KNOWN:
                pass
            case Action.UNKNOWN:
                pass
