"""Word study repository tests."""

import uuid
from unittest.mock import Mock

from wse.data import repos


class TestProgress:
    """Test Word study progress repository."""

    def test_increment(
        self,
        mock_word_study_locale_source: Mock,
        mock_word_progress_source: Mock,
        word_study_progress_repo: repos.WordStudyProgressRepo,
    ) -> None:
        """Test the increment progress."""
        # Arrange
        case_uuid = uuid.uuid4()
        mock_word_study_locale_source.get_case_uuid.return_value = case_uuid

        # Act
        word_study_progress_repo.increment()

        # Assert
        mock_word_study_locale_source.get_case_uuid.assert_called_once_with()
        mock_word_progress_source.increment_progress.assert_called_once_with(
            case_uuid
        )

    def test_decrement(
        self,
        mock_word_study_locale_source: Mock,
        mock_word_progress_source: Mock,
        word_study_progress_repo: repos.WordStudyProgressRepo,
    ) -> None:
        """Test the increment progress."""
        # Arrange
        case_uuid = uuid.uuid4()
        mock_word_study_locale_source.get_case_uuid.return_value = case_uuid

        # Act
        word_study_progress_repo.decrement()

        # Assert
        mock_word_study_locale_source.get_case_uuid.assert_called_once_with()
        mock_word_progress_source.decrement_progress.assert_called_once_with(
            case_uuid
        )
