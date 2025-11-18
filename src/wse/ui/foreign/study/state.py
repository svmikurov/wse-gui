"""Foreign words study ViewModel."""

import logging
from dataclasses import dataclass
from typing import Literal, NamedTuple, TypeAlias, override

from injector import inject

from wse.data.sources.foreign import schemas
from wse.domain.foreign import ExerciseAccessorT, WordStudyUseCaseABC
from wse.domain.text import TextHyphenationABC
from wse.feature.observer import ChangeObserverABC
from wse.feature.observer.generic import HandleObserverGenABC
from wse.feature.observer.mixins import NotifyGen, ObserverManagerGen
from wse.ui.base.navigate.mixin import NavigateStateMixin
from wse.ui.containers.control import Action
from wse.utils import I18N

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


class TextInfo(NamedTuple):
    """Textual representation of Presentation Info."""

    progress: str


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
    _normalize_case: TextHyphenationABC

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
        value: object,
    ) -> None:
        """Notify that exercise case was updated."""
        match accessor:
            case 'definition':
                self._reset_unknown_state()
                adapted_text = self._adapt_text(value)
                self.notify('change', accessor=accessor, value=adapted_text)

            case 'explanation':
                adapted_text = self._adapt_text(value)
                self.notify('change', accessor=accessor, value=adapted_text)

            case 'info':
                if isinstance(value, schemas.Info):
                    text = self._update_info(value)
                    self.notify('change', accessor=accessor, value=text)

            case _:
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

    def _update_info(self, data: schemas.Info) -> TextInfo:
        """Update Word study Presentation info."""
        return TextInfo(
            progress=I18N.EXERCISE('progress') + f': {data.progress or "-"}'
        )

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
            case Action.DISPLAY:
                self._study_case.display()
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

    def _adapt_text(self, text: object) -> str:
        return self._normalize_case.adapt(str(text))
