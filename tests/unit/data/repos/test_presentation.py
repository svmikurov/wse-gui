"""Word study repository tests."""

from unittest.mock import Mock

from wse.api.foreign import schemas
from wse.data import repos


class TestWordStudyRepo:
    """Test Word study repository."""

    def test_get_word(
        self,
        presentation_params: schemas.PresentationParams,
        mock_word_locale_source: Mock,
        mock_word_network_source: Mock,
        mock_word_study_params_repo: Mock,
        word_case: schemas.PresentationCase,
        word_data: schemas.PresentationSchema,
        word_study_repo: repos.WordStudyRepo,
    ) -> None:
        """Test the get word to study."""
        # Arrange
        mock_word_network_source.fetch_presentation.return_value = word_case
        mock_word_locale_source.get_presentation_data.return_value = word_data
        mock_word_study_params_repo.get_params.return_value = (
            presentation_params
        )

        # Act
        data = word_study_repo.get_word()

        # Assert
        assert data == word_data
        mock_word_network_source.fetch_presentation.assert_called_once_with(
            presentation_params
        )
        mock_word_locale_source.set_case.assert_called_once_with(word_case)
        mock_word_locale_source.get_presentation_data.assert_called_once_with()
