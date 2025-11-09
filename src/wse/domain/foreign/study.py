"""Foreign word study presenter."""

import asyncio
import logging
from dataclasses import dataclass
from typing import override

from injector import inject

from wse.data.repos import foreign as repos
from wse.data.sources.foreign import schemas
from wse.domain import foreign as base
from wse.feature.observer.accessor import NotifyAccessorGen

from ..abc import PresentationABC

log = logging.getLogger(__name__)


@inject
@dataclass
class WordStudyUseCase(
    base.WordStudyUseCaseABC,
    NotifyAccessorGen[base.UIStateNotifyT, base.ExerciseAccessorT],
):
    """Words study Use Case."""

    _get_word_repo: repos.WordStudyRepoABC
    _progress_repo: repos.WordStudyProgressRepoABC
    _domain: PresentationABC

    NO_TEXT = ''

    def __post_init__(self) -> None:
        """Initialize UseCase attributes."""
        self._study_task: asyncio.Task[None] | None = None
        self._progress_task: asyncio.Task[None] | None = None

    def start(self) -> None:
        """Start exercise."""
        self._start_background_tasks()
        self._domain.start()

    def stop(self) -> None:
        """Stop exercise."""
        self._stop_background_tasks()
        self._domain.stop()

    # Background tasks
    # ----------------

    async def _loop_word_study(self) -> None:
        """Loop Word study exercise."""
        try:
            while True:
                # Start presentation case
                await self._domain.wait_start_case_event()
                try:
                    data = self._get_data()
                # TODO: Improve chained exception handling
                except Exception:
                    self.stop()
                    break

                # Definition presentation phase
                await self._domain.wait_definition_event()
                self._display_definition(data.definition)

                # Explanation presentation phase
                await self._domain.wait_explanation_event()
                self._display_explanation(data.explanation)

                # End presentation case
                await self._domain.wait_end_case_event()
                self._display_definition(WordStudyUseCase.NO_TEXT)
                self._display_explanation(WordStudyUseCase.NO_TEXT)

        except asyncio.CancelledError:
            log.debug('Word study loop cancelled')
            raise

        except Exception as e:
            log.error(f'Unexpected error in word study loop: {e}')

    async def _monitor_progress(self) -> None:
        """Monitor the Word study case event progress."""
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

    # Utility methods
    # ---------------

    def _start_background_tasks(self) -> None:
        """Start background tasks for word study."""
        self._study_task = asyncio.create_task(self._loop_word_study())
        self._progress_task = asyncio.create_task(self._monitor_progress())

    def _stop_background_tasks(self) -> None:
        """Cancel all background tasks."""
        for task in [self._study_task, self._progress_task]:
            if task is not None and not task.done():
                task.cancel()

    def _get_data(self) -> schemas.WordPresentationSchema:
        try:
            return self._get_word_repo.get_word()
        except Exception as e:
            log.error(f'Get word study error: {e}')
            raise
