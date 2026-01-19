"""Word study presentation domain."""

import asyncio
import logging
from dataclasses import dataclass
from typing import Final, override

from injector import inject

from wse.core import exceptions
from wse.data.repos import foreign as repos
from wse.data.schemas import foreign
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
    """Words study Presentation domain."""

    _get_word_repo: repos.WordPresentationRepoABC
    _progress_repo: repos.WordProgressRepoABC
    _settings_repo: repos.WordParametersRepo
    _domain: PresentationABC

    NO_TEXT: Final[str] = ''

    def __post_init__(self) -> None:
        """Initialize the presentation."""
        self._study_task: asyncio.Task[None] | None = None
        self._progress_task: asyncio.Task[None] | None = None

    def start(self) -> None:
        """Start exercise."""
        settings = self._settings_repo.get_settings()
        self._domain.set_timeout(settings)
        self._start_background_tasks()
        self._domain.start()

    def stop(self) -> None:
        """Stop exercise."""
        self._stop_background_tasks()
        self._domain.stop()
        self._notify_clean()

    # Background tasks
    # ----------------

    async def _loop_word_study(self) -> None:
        """Loop Word study exercise."""
        try:
            while True:
                # Start presentation case
                log.info('Presentation started')
                await self._domain.wait_start_case_event()

                try:
                    data = self._get_data()
                except exceptions.NoResponseDataError:
                    log.info('Presentation finished - no data')
                    self.stop()
                    break
                except Exception as e:
                    log.error(f'Error getting word data: {e}')
                    self.stop()
                    break

                # Definition presentation phase
                await self._domain.wait_definition_event()
                self._display_definition(data.question)
                if data.info:
                    self._display_info(data.info)

                # Explanation presentation phase
                await self._domain.wait_explanation_event()
                self._display_explanation(data.answer)

                # End presentation case
                await self._domain.wait_end_case_event()
                self._notify_clean()

        except asyncio.CancelledError:
            log.debug('Word study loop cancelled')
            raise

        finally:
            self._notify_clean()
            log.debug('Word study loop finished')

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

    def _display_info(self, data: object) -> None:
        self.notify('exercise_updated', accessor='info', value=data)

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

    @override
    def unpause(self) -> None:
        """Handle 'unpause' case user action of exercise."""
        self._domain.unpause()

    @override
    def display(self) -> None:
        """Handle 'display' case user action of exercise."""
        self._domain.complete_phase()
        self._domain.unpause()

    @override
    def next(self) -> None:
        """Handle 'next' case user action of exercise."""
        self.stop()
        self.start()

    @override
    def known(self) -> None:
        """Handle 'known' case user action of exercise."""
        self._progress_repo.increment()
        self.next()

    @override
    def unknown(self) -> None:
        """Handle 'unknown' case user action of exercise."""
        self._progress_repo.decrement()
        self._domain.complete_phase()
        self.unpause()

    # Utility methods
    # ---------------

    def _notify_clean(self) -> None:
        self._display_definition(WordStudyUseCase.NO_TEXT)
        self._display_explanation(WordStudyUseCase.NO_TEXT)

    def _start_background_tasks(self) -> None:
        """Start background tasks for word study."""
        self._study_task = asyncio.create_task(self._loop_word_study())
        self._progress_task = asyncio.create_task(self._monitor_progress())

    def _stop_background_tasks(self) -> None:
        """Cancel all background tasks."""
        for task in [self._study_task, self._progress_task]:
            if task is not None and not task.done():
                task.cancel()

    def _get_data(self) -> foreign.Presentation:
        try:
            return self._get_word_repo.get_word()

        # TODO: Fix asyncio executing WARNING log
        # Subject notification 'no_case' too long for asyncio
        except exceptions.NoResponseDataError:
            log.info('No case available')
            self._subject.notify('no_case')
            raise

        except Exception as e:
            log.error(f'Get word study error: {e}')
            raise
