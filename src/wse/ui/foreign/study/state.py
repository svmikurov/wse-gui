"""Foreign words study ViewModel."""

import logging
from dataclasses import dataclass
from typing import Literal, TypeAlias, override

from injector import inject

from wse.domain.foreign import (
    ExerciseAccessorT,
    WordStudyUseCaseABC,
)
from wse.feature.observer import ChangeObserverABC
from wse.feature.observer.generic import HandleObserverGenABC
from wse.feature.observer.mixins import NotifyGen, ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.control import Action
from wse.utils import decorators

from . import ChangeNotifyT, WordPresentationViewModelABC

log = logging.getLogger(__name__)

NO_TEXT = ''

# TODO: Refactor
ProgressT = Literal[
    'timeout_updated',
    'pause_state_updated',
    'unknown_state_updated',
]
Observer: TypeAlias = (
    ChangeObserverABC[ChangeNotifyT] | HandleObserverGenABC[Action]
)


@inject
@dataclass
class WordPresentationViewModel(
    NavigateStateMixin,
    ObserverManagerGen[Observer],
    NotifyGen[ChangeNotifyT | ProgressT | Action],
    WordPresentationViewModelABC,
):
    """Foreign words study ViewModel."""

    _study_case: WordStudyUseCaseABC

    def __post_init__(self) -> None:
        """Construct the ViewModel."""
        self._study_case.add_observer(self)
        # TODO: Is pause a UIState or attribute value?
        self._pause: bool = False

    def on_open(self) -> None:
        """Call methods on open the screen."""
        self._study_case.start()

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
        if accessor == 'definition':
            self._reset_unknown_state()

    @override
    def timeout_updated(
        self,
        accessor: ExerciseAccessorT,
        max: float,
        value: float,
    ) -> None:
        """Notify that timeout of exercise phase was updated."""
        self.notify('timeout_updated', accessor=accessor, max=max, value=value)

    # Development mode implementation
    @decorators.log_unimplemented_call
    def _update_info(self) -> None:
        """Update Word study info."""
        self.notify('change', accessor='progress', value='test')

    @override
    def handle(self, action: Action) -> None:
        """Handle user action."""
        match action:
            case Action.PAUSE:
                self._study_case.pause()
                self._set_pause()
                return
            case Action.UNPAUSE:
                self._study_case.unpause()
            case Action.NEXT:
                self._study_case.next()
            case Action.KNOWN:
                self._study_case.known()
            case Action.UNKNOWN:
                self._study_case.unknown()
                self._set_unknown_state()

        self._reset_pause()

    # Utility methods
    # ---------------

    def _set_pause(self) -> None:
        self._pause = True
        self.notify('pause_state_updated', value=True)

    def _reset_pause(self) -> None:
        """Reset pause."""
        if self._pause:
            self.notify('pause_state_updated', value=False)
            self._pause = False

    def _set_unknown_state(self) -> None:
        self.notify('unknown_state_updated', value=False)

    def _reset_unknown_state(self) -> None:
        self.notify('unknown_state_updated', value=True)
