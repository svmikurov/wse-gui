"""Test Word study UseCase."""

import asyncio
from typing import Generator
from unittest.mock import AsyncMock, Mock, patch

import pytest

from wse.data.sources.foreign.schema import WordPresentationSchema
from wse.domain.foreign.study import WordStudyUseCase
from wse.domain.presentation import Presentation


@pytest.fixture
def use_case(
    mock_subject: Mock,
    mock_get_word_repo: Mock,
    mock_progress_repo: Mock,
    presentation: Presentation,
) -> WordStudyUseCase:
    """Word study UseCase fixture."""
    return WordStudyUseCase(
        _subject=mock_subject,
        _get_word_repo=mock_get_word_repo,
        _progress_repo=mock_progress_repo,
        _domain=presentation,
    )


@pytest.fixture
def mock_get_data(
    word_data: WordPresentationSchema,
    use_case: WordStudyUseCase,
) -> Generator[Mock, None, None]:
    """Mock get Word study data fixture."""
    with patch.object(use_case, '_get_data', return_value=word_data) as mock:
        yield mock


# TODO: Add tests
class TestWordStudyExceptions:
    """Test the Word study exceptions."""

    @pytest.mark.skip('Add test')
    def test_no_word_data(self) -> None:
        """Test no word data to study case."""
        ...

    ...


class TestProgressRepoDependency:
    """Test Progress word study repository call."""

    def test_known_word_case(
        self,
        mock_progress_repo: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'known' word case."""
        use_case_di_mock.known()
        mock_progress_repo.increment.assert_called_once_with()

    def test_unknown_word_case(
        self,
        mock_progress_repo: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'unknown' word case."""
        use_case_di_mock.unknown()
        mock_progress_repo.decrement.assert_called_once_with()


class TestWordDataRepoDependency:
    """Test Get word data repository call."""

    def test_get_word_repo_call(
        self,
        mock_get_word_repo: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the get word repo call."""
        use_case_di_mock._get_data()
        mock_get_word_repo.get_word.assert_called_once_with()


class TestWordStudyCaseManagement:
    """Test Word study case management."""

    def test_pause_case(
        self,
        mock_domain: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'pause' call."""
        use_case_di_mock.pause()
        mock_domain.pause.assert_called_once_with()

    # TODO: Update `WordStudyUseCase.next` to 'unpause'
    def test_unpause_case(
        self,
        mock_domain: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'unpause' call."""
        use_case_di_mock.next()
        mock_domain.unpause.assert_called_once_with()

    @pytest.mark.skip('Implement functionality')
    def test_next_case(
        self,
        mock_domain: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'next' call."""


class TestWordStudyLoop:
    """Test Word study loop events."""

    async def _yield_control(self) -> None:
        """Yield control to event loop to allow other tasks to run."""
        await asyncio.sleep(0)

    @pytest.mark.asyncio
    @patch.object(WordStudyUseCase, '_display_explanation', return_value=None)
    @patch.object(WordStudyUseCase, '_display_definition', return_value=None)
    async def test_definition_event(
        self,
        mock_definition: Mock,
        mock_explanation: Mock,
        mock_get_data: Mock,
        word_data: WordPresentationSchema,
        presentation: Presentation,
        use_case: WordStudyUseCase,
    ) -> None:
        """Test the Word study loop."""
        # Run Word study loop
        use_case.start()

        # Start case event
        presentation._start_case_event.set()
        await self._yield_control()
        presentation._start_case_event.clear()  # Test only one loop cycle

        # Assert what only get data method was called
        mock_get_data.assert_called_once_with()
        mock_get_data.reset_mock()
        mock_definition.assert_not_called()
        mock_explanation.assert_not_called()

        # Set the definition phase event
        presentation._definition_event.set()
        await self._yield_control()

        # Assert what only definition notification was called
        mock_get_data.assert_not_called()
        mock_definition.assert_called_once_with(word_data.definition)
        mock_definition.reset_mock()
        mock_explanation.assert_not_called()

        # Set the explanation phase event
        presentation._explanation_event.set()
        await self._yield_control()

        # Assert what only explanation notification was called
        mock_get_data.assert_not_called()
        mock_definition.assert_not_called()
        mock_explanation.assert_called_once_with(word_data.explanation)
        mock_explanation.reset_mock()

        # Set the case end event
        presentation._end_case_event.set()
        await self._yield_control()

        # Assert what only clear notification was called
        mock_get_data.assert_not_called()
        mock_definition.assert_called_once_with(WordStudyUseCase.NO_TEXT)
        mock_explanation.assert_called_once_with(WordStudyUseCase.NO_TEXT)

        # Cancel Word study loop
        use_case.stop()


class TestUseCaseLifecycle:
    """Test suite for WordStudyUseCase start/stop functionality."""

    def test_start(
        self,
        mock_domain: AsyncMock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test start method.

        Verifies that:
        - Background tasks are created when start is called
        - Domain start method is invoked
        """
        with patch(
            'wse.domain.foreign.study.WordStudyUseCase._start_background_tasks'
        ) as mock_create_task:
            use_case_di_mock.start()
            # Verify background tasks creation was triggered
            mock_create_task.assert_called_once_with()
            # Verify domain layer was initialized
            mock_domain.start.assert_called_once_with()

    def test_stop(
        self,
        mock_domain: AsyncMock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test stop method."""
        with patch(
            'wse.domain.foreign.study.WordStudyUseCase._stop_background_tasks'
        ) as mock_stop_tasks:
            use_case_di_mock.stop()
            mock_stop_tasks.assert_called_once_with()
            mock_domain.stop.assert_called_once_with()

    @pytest.mark.asyncio
    async def test_start_background_tasks(
        self,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test background tasks creation without execution.

        Validates that:
        - Background tasks are properly instantiated as asyncio Tasks
        - Tasks are in active state (not done) after creation
        - Does not test task execution logic, only creation
        """
        use_case_di_mock._start_background_tasks()

        # Verify tasks are created as proper asyncio Task objects
        assert isinstance(use_case_di_mock._study_task, asyncio.Task)
        assert isinstance(use_case_di_mock._progress_task, asyncio.Task)

        # Verify tasks are active and not completed
        assert not use_case_di_mock._study_task.done()
        assert not use_case_di_mock._progress_task.done()

        # Cleanup: cancel tasks to prevent hanging
        use_case_di_mock._stop_background_tasks()

    @pytest.mark.asyncio
    async def test_stop_background_tasks(
        self,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test background tasks cancellation lifecycle.

        Verifies the complete cancellation flow:
        - Tasks enter cancelling state immediately after stop call
        - Tasks properly transition to done state after cancellation
          processing
        - Tasks are marked as cancelled after processing completes
        """
        use_case_di_mock._start_background_tasks()
        use_case_di_mock._stop_background_tasks()

        # Verify tasks are in cancelling state
        # (immediate response to cancel())
        assert use_case_di_mock._study_task.cancelling()  # type: ignore[union-attr]
        assert use_case_di_mock._progress_task.cancelling()  # type: ignore[union-attr]

        # Allow time for tasks to process cancellation
        # and raise CancelledError
        await asyncio.sleep(0.1)

        # Verify tasks are fully completed after cancellation processing
        assert use_case_di_mock._study_task.done()  # type: ignore[union-attr]
        assert use_case_di_mock._study_task.cancelled()  # type: ignore[union-attr]

        assert use_case_di_mock._progress_task.done()  # type: ignore[union-attr]
        assert use_case_di_mock._progress_task.cancelled()  # type: ignore[union-attr]
