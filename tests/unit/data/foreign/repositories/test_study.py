"""Word study repository tests."""

from unittest.mock import Mock

from wse.data.repositories.foreign import study as repos
from wse.data.sources.foreign import schemas


class TestWordStudyRepo:
    """Test Word study repository."""

    def test_get_word(
        self,
        mock_locale_source: Mock,
        mock_network_source: Mock,
        word_case: schemas.WordStudyCaseSchema,
        word_data: schemas.WordPresentationSchema,
        word_study_repo: repos.WordStudyRepo,
    ) -> None:
        """Test the get word to study."""
        mock_network_source.fetch_presentation.return_value = word_case
        mock_locale_source.get_presentation_data.return_value = word_data

        data = word_study_repo.get_word()

        assert data == word_data
        mock_network_source.fetch_presentation.assert_called_once_with()
        mock_locale_source.set_case.assert_called_once_with(word_case)
        mock_locale_source.get_presentation_data.assert_called_once_with()
