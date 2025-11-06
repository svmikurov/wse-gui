"""Foreign word study presenter."""

import asyncio
import logging
from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.repositories import foreign as repo
from wse.data.sources.foreign import schemas
from wse.domain.foreign.abc import (
    ExerciseAccessorT,
    UIStateNotifyT,
    WordStudyUseCaseABC,
)
from wse.feature.observer.accessor import NotifyAccessorGen

from ..abc import PresentationABC

NO_TEXT = ''

log = logging.getLogger(__name__)


@inject
@dataclass
class WordStudyUseCase(
    WordStudyUseCaseABC,
    NotifyAccessorGen[UIStateNotifyT, ExerciseAccessorT],
):
    """Words study Use Case."""

    _get_word_repo: repo.WordStudyCaseRepoABC
    _progress_repo: repo.WordStudyProgressRepoABC
    _settings_repo: repo.WordStudySettingsRepoABC
    _domain: PresentationABC

    def __post_init__(self) -> None:
        """Construct the case."""
        self._settings = self._settings_repo.get_settings()

    def start(self) -> None:
        """Start exercise."""
        asyncio.create_task(self._loop_word_study())
        self._domain.start()

    async def _loop_word_study(self) -> None:
        """Loop Word study exercise."""
        asyncio.create_task(self._monitor_progress())

        while True:
            # Start presentation case
            await self._domain.wait_start_case_event()
            if not (data := self._get_data()):
                break

            # Definition presentation phase
            await self._domain.wait_definition_event()
            self._display_definition(data.definition)

            # Explanation presentation phase
            await self._domain.wait_explanation_event()
            self._display_explanation(data.explanation)

            # End presentation case
            await self._domain.wait_end_case_event()
            self._display_definition(NO_TEXT)
            self._display_explanation(NO_TEXT)

    # Word study case event progress
    # ------------------------------

    async def _monitor_progress(self) -> None:
        while True:
            max, value = await self._domain.get_progress()
            self._display_timeout(max, value)

    # Notifications
    # -------------

    def _display_definition(self, value: str) -> None:
        self.notify('exercise_updated', accessor='definition', value=value)

    def _display_explanation(self, value: str) -> None:
        self.notify('exercise_updated', accessor='explanation', value=value)

    # TODO: Refactor, remove accessor='timeout'
    def _display_timeout(self, max: float, value: float) -> None:
        self.notify(
            'timeout_updated', accessor='timeout', max=max, value=value
        )

    # Exercise user actions
    # ---------------------

    @override
    def pause(self) -> None:
        """Handle 'pause' case user action of exercise."""
        self._domain.pause()

    # TODO: Add `unpause` method, update `next` method
    @override
    def next(self) -> None:
        """Handle 'next' case user action of exercise."""
        self._domain.unpause()

    @override
    def known(self) -> None:
        """Handle 'known' case user action of exercise."""
        self._progress_repo.increment()

    @override
    def unknown(self) -> None:
        """Handle 'unknown' case user action of exercise."""
        self._progress_repo.decrement()

    def stop(self) -> None:
        """Stop exercise."""
        self._domain.stop()

    # Utility methods
    # ---------------

    def _get_data(self) -> schemas.WordPresentationSchema | None:
        try:
            return self._get_word_repo.get_word()
        except Exception as e:
            log.error(f'Get word study error: {e}')
            return None
