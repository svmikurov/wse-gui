"""Foreign word study presenter."""

import asyncio
import logging
from dataclasses import dataclass
from typing import Any

import toga
from injector import inject

from wse.core.navigation import NavID
from wse.data.repositories.foreign.abc import WordsStudyNetworkRepoABC
from wse.domain.foreign.abc import (
    ExerciseAccessorT,
    UIStateNotifyT,
    WordsStudyUseCaseABC,
)
from wse.feature.observer.mixins import NotifyAccessorGen
from wse.feature.timer.abc import TimerABC
from wse.ui.content import Content

NO_TEXT = ''

log = logging.getLogger(__name__)


@inject
@dataclass
class WordsStudyUseCase(
    WordsStudyUseCaseABC,
    NotifyAccessorGen[UIStateNotifyT, ExerciseAccessorT],
):
    """Words study Use Case."""

    _words_study_repo: WordsStudyNetworkRepoABC
    _main_window: toga.MainWindow
    _timer: TimerABC

    def __post_init__(self) -> None:
        """Construct the case."""
        self._study_data: dict[str, Any] | None = None

    def _update_study_data(self) -> None:
        self._study_data = self._words_study_repo.get_data()

    # Exercise management

    def start(self) -> None:
        """Start exercise."""
        self._update_study_data()
        asyncio.create_task(self.loop())

    async def loop(self) -> None:
        """Loop exercise."""
        if not self._study_data:
            log.error('No words study data')
            return

        while self.is_enable_exercise:
            self._study_data = self._words_study_repo.get_data()

            self._display_definition(self._study_data['definition'])
            await self._timer.start(1)

            self._display_explanation(self._study_data['explanation'])
            await self._timer.start(1)
            self._display_definition(NO_TEXT)
            self._display_explanation(NO_TEXT)

            print('End cycle')

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

    def _display_definition(self, value: str) -> None:
        self.notify('exercise_updated', accessor='definition', value=value)

    def _display_explanation(self, value: str) -> None:
        self.notify('exercise_updated', accessor='explanation', value=value)
