"""Test Word study UseCase."""

import asyncio
from typing import Generator
from unittest.mock import AsyncMock, Mock, patch

import pytest

from wse.data.sources.foreign.schemas import PresentationSchema
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
    word_data: PresentationSchema,
    use_case: WordStudyUseCase,
) -> Generator[Mock, None, None]:
    """Mock get Word study data fixture."""
    with patch.object(use_case, '_get_data', return_value=word_data) as mock:
        yield mock


class TestPresentationInfo:
    """Test Presentation info."""

    @pytest.mark.asyncio
    async def test_info_notification_called(
        self,
        word_data: PresentationSchema,
        mock_get_data: Mock,  # Mock to return presentation case data
        use_case: WordStudyUseCase,
    ) -> None:
        """Test that exercise info updated notification was called."""
        # Act
        with patch.object(use_case, '_display_info') as mock:
            use_case.start()
            await asyncio.sleep(0.05)

        # Assert
        mock.assert_called_once_with(word_data.info)


# TODO: Add tests
class TestWordStudyExceptions:
    """Test the Word study exceptions."""

    @pytest.mark.skip('Add test')
    def test_no_word_data(self) -> None:
        """Test no word data to study case."""
        ...

    ...


class TestDataRepo:
    """Test Get word data repository call."""

    def test_get_word_repo_call(
        self,
        mock_get_word_repo: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the get word repo call."""
        # Act
        use_case_di_mock._get_data()

        # Assert
        mock_get_word_repo.get_word.assert_called_once_with()


class TestActions:
    """Test Word study case user actions."""

    def test_known(
        self,
        mock_progress_repo: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'known' call."""
        with patch.object(use_case_di_mock, 'next') as mock_next:
            # Act
            use_case_di_mock.known()

        # Assert
        mock_next.assert_called_once_with()
        mock_progress_repo.increment.assert_called_once_with()

    def test_unknown(
        self,
        mock_domain: Mock,
        mock_progress_repo: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'unknown' call."""
        with patch.object(use_case_di_mock, 'unpause') as mock_unpause:
            # Act
            use_case_di_mock.unknown()

        # Assert
        mock_progress_repo.decrement.assert_called_once_with()
        mock_domain.complete_phase.assert_called_once_with()
        mock_unpause.assert_called_once_with()

    def test_pause(
        self,
        mock_domain: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'pause' call."""
        # Act
        use_case_di_mock.pause()

        # Assert
        mock_domain.pause.assert_called_once_with()

    def test_unpause(
        self,
        mock_domain: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'unpause' call."""
        # Act
        use_case_di_mock.unpause()

        # Assert
        mock_domain.unpause.assert_called_once_with()

    @patch.object(WordStudyUseCase, '_start_background_tasks')
    @patch.object(WordStudyUseCase, '_stop_background_tasks')
    @patch.object(WordStudyUseCase, '_notify_clean')
    def test_next(
        self,
        mock_start_background: Mock,
        mock_stop_background: Mock,
        mock_notify_clean: Mock,
        mock_domain: Mock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test the 'next' call."""
        # Act
        use_case_di_mock.next()

        # Verify correct cancel current case
        mock_stop_background.assert_called_once_with()
        mock_domain.stop.assert_called_once_with()
        mock_notify_clean.assert_called_once_with()

        # Verify correct start new case
        mock_start_background.assert_called_once_with()
        mock_domain.start.assert_called_once_with()


class TestLifecycle:
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
        with patch.object(
            use_case_di_mock, '_start_background_tasks'
        ) as mock_create_task:
            # Act
            use_case_di_mock.start()

            # Assert
            mock_create_task.assert_called_once_with()
            mock_domain.start.assert_called_once_with()

    def test_stop(
        self,
        mock_domain: AsyncMock,
        use_case_di_mock: WordStudyUseCase,
    ) -> None:
        """Test stop method."""
        with patch.object(
            use_case_di_mock, '_stop_background_tasks'
        ) as mock_stop_tasks:
            # Act
            use_case_di_mock.stop()

            # Assert
            mock_stop_tasks.assert_called_once_with()
            mock_domain.stop.assert_called_once_with()


class TestStudyLoop:
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
        word_data: PresentationSchema,
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


class TestBackgroundTasks:
    """Test Word study background tasks."""

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
