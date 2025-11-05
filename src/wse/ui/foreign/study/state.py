"""Foreign words study ViewModel."""

import logging
from dataclasses import dataclass
from typing import Literal, override

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

from . import PresenterNotifyT, WordPresentationViewModelABC

log = logging.getLogger(__name__)

NO_TEXT = ''

# TODO: Refactor
ProgressT = Literal['timeout_updated']


@inject
@dataclass
class WordPresentationViewModel(
    NavigateStateMixin,
    ObserverManagerGen[
        ChangeObserverABC[PresenterNotifyT] | HandleObserverABC[Action]
    ],
    NotifyGen[PresenterNotifyT | ProgressT | Action],
    WordPresentationViewModelABC,
):
    """Foreign words study ViewModel."""

    _study_case: WordStudyUseCaseABC

    def __post_init__(self) -> None:
        """Construct the ViewModel."""
        self._study_case.add_observer(self)

    def on_open(self) -> None:
        """Call methods on open the screen."""
        self._study_case.start()

    @decorators.log_func_call
    @override
    def on_close(self) -> None:
        """Call methods before close the screen."""
        self._study_case.remove_observer(self)
        self._study_case.stop()

    @override
    def exercise_updated(
        self,
        accessor: ExerciseAccessorT,
        value: str,
    ) -> None:
        """Notify that exercise case was updated."""
        self.notify('change', accessor=accessor, value=value)

    @override
    def timeout_updated(
        self,
        accessor: ExerciseAccessorT,
        max: float,
        value: float,
    ) -> None:
        """Notify that timeout of exercise phase was updated."""
        self.notify('timeout_updated', accessor=accessor, max=max, value=value)

    @override
    def handle(self, action: Action) -> None:
        """Handle user action."""
        match action:
            case Action.PAUSE:
                self._study_case.pause()
            case Action.NEXT:
                self._study_case.next()
            case Action.KNOWN:
                self._study_case.known()
            case Action.UNKNOWN:
                self._study_case.unknown()
