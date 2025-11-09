"""Word study repository tests."""

import uuid
from unittest.mock import Mock

from wse.data import repos
from wse.data.sources.foreign import schemas


class TestProgress:
    """Test Word study progress repository."""

    def test_increment(
        self,
        mock_word_locale_source: Mock,
        mock_word_progress_source: Mock,
        word_study_progress_repo: repos.WordStudyProgressRepo,
    ) -> None:
        """Test the increment progress."""
        case_uuid = uuid.uuid4()
        mock_word_locale_source.get_case_uuid.return_value = case_uuid

        word_study_progress_repo.increment()

        mock_word_locale_source.get_case_uuid.assert_called_once_with()
        mock_word_progress_source.increment_progress.assert_called_once_with(
            case_uuid
        )

    def test_decrement(
        self,
        mock_word_locale_source: Mock,
        mock_word_progress_source: Mock,
        word_study_progress_repo: repos.WordStudyProgressRepo,
    ) -> None:
        """Test the increment progress."""
        case_uuid = uuid.uuid4()
        mock_word_locale_source.get_case_uuid.return_value = case_uuid

        word_study_progress_repo.decrement()

        mock_word_locale_source.get_case_uuid.assert_called_once_with()
        mock_word_progress_source.decrement_progress.assert_called_once_with(
            case_uuid
        )


class TestWordStudyRepo:
    """Test Word study repository."""

    def test_get_word(
        self,
        mock_word_locale_source: Mock,
        mock_word_network_source: Mock,
        word_case: schemas.WordStudyCaseSchema,
        word_data: schemas.WordPresentationSchema,
        word_study_repo: repos.WordStudyRepo,
    ) -> None:
        """Test the get word to study."""
        mock_word_network_source.fetch_presentation.return_value = word_case
        mock_word_locale_source.get_presentation_data.return_value = word_data

        data = word_study_repo.get_word()

        assert data == word_data
        mock_word_network_source.fetch_presentation.assert_called_once_with()
        mock_word_locale_source.set_case.assert_called_once_with(word_case)
        mock_word_locale_source.get_presentation_data.assert_called_once_with()
