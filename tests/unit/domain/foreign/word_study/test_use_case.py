"""Test Word study UseCase."""

from unittest.mock import AsyncMock, patch

from wse.domain.foreign.study import WordStudyUseCase


class TestUseCaseStart:
    """Test start UseCase call."""

    def test_start(
        self,
        mock_domain: AsyncMock,
        use_case: WordStudyUseCase,
    ) -> None:
        """Test call `start()` method."""
        with patch(
            'wse.domain.foreign.study.WordStudyUseCase._create_background_tasks'
        ) as mock_create_task:
            use_case.start()
            mock_create_task.assert_called_once_with()
            mock_domain.start.assert_called_once_with()
