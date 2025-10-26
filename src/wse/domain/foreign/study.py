"""Foreign word study presenter."""

import asyncio
import logging
from dataclasses import dataclass

import toga
from injector import inject

from wse.api.foreign.schemas import WordStudyPresentationSchema
from wse.core.navigation import NavID
from wse.data.repositories.foreign.abc import WordStudyNetworkRepoABC
from wse.domain.foreign.abc import (
    ExerciseAccessorT,
    UIStateNotifyT,
    WordStudyUseCaseABC,
)
from wse.feature.observer.mixins import NotifyAccessorGen
from wse.feature.timer.abc import TimerABC
from wse.ui.content import Content

NO_TEXT = ''

log = logging.getLogger(__name__)
audit = logging.getLogger('audit')


@inject
@dataclass
class WordStudyUseCase(
    WordStudyUseCaseABC,
    NotifyAccessorGen[UIStateNotifyT, ExerciseAccessorT],
):
    """Words study Use Case."""

    _words_study_repo: WordStudyNetworkRepoABC
    _main_window: toga.MainWindow
    _timer: TimerABC

    def __post_init__(self) -> None:
        """Construct the case."""
        self._study_data: WordStudyPresentationSchema | None = None

    def _update_study_data(self) -> None:
        self._study_data = self._words_study_repo.get_data()

    # Exercise management
    # -------------------

    def start(self) -> None:
        """Start exercise."""
        log.debug("Started 'Word study presentation'")
        try:
            asyncio.create_task(self.loop())
        except Exception:
            log.error('The exercise has been break')
            return

    async def loop(self) -> None:
        """Loop exercise."""
        while self.is_enable_exercise:
            try:
                self._study_data = self._words_study_repo.get_data()
            except Exception:
                log.error('Get word study error')
                break

            self._display_definition(self._study_data.definition)
            await self._timer.start(1)

            self._display_explanation(self._study_data.explanation)
            await self._timer.start(1)
            self._display_definition(NO_TEXT)
            self._display_explanation(NO_TEXT)

    @property
    def is_enable_exercise(self) -> bool:
        """Return `False` to cancel task update, `True` otherwise."""
        if not self._timer.is_pause():
            return self.is_visible_screen
        return False

    @property
    def is_visible_screen(self) -> bool:
        """Is the current screen visible."""
        if isinstance(self._main_window.content, Content):
            return self._main_window.content.test_id == NavID.FOREIGN_STUDY
        return False

    # UIState management
    # ------------------

    def _display_definition(self, value: str) -> None:
        self.notify('exercise_updated', accessor='definition', value=value)

    def _display_explanation(self, value: str) -> None:
        self.notify('exercise_updated', accessor='explanation', value=value)
