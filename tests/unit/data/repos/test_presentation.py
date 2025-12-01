"""Word study repository tests."""

from unittest.mock import Mock

from wse.data import repos
from wse.data.schemas import foreign as schemas


class TestWordStudyRepo:
    """Test Word study repository."""

    def test_get_word(
        self,
        mock_word_params_repo: Mock,
        mock_word_study_locale_source: Mock,
        mock_word_study_network_source: Mock,
        word_study_repo: repos.WordPresentationRepo,
        word_case: schemas.PresentationCase,
        word_data: schemas.Presentation,
    ) -> None:
        """Test the Word study Presentation data query to display."""
        # Arrange
        # - Word study Locale parameter
        #   to request the case from the Network
        presentation_params = Mock()
        mock_word_params_repo.get.return_value = presentation_params

        # - Word study case with additional info
        #   (e.g. `case_uuid`) from Network
        mock_word_study_network_source.fetch_presentation.return_value = (
            word_case
        )

        # - Word study presentation data to display
        mock_word_study_locale_source.get_presentation_data.return_value = (
            word_data
        )

        # Act
        # - Get presentation data to display
        data = word_study_repo.get_word()

        # Assert
        # - That got the expected data to display
        assert data == word_data

        # - That presentation data was requested from the
        #   Network source using Word study parameters
        mock_word_study_network_source.fetch_presentation.assert_called_once_with(
            presentation_params
        )

        # - That correct case data has been set
        #   in the Locale source
        mock_word_study_locale_source.set_case.assert_called_once_with(
            word_case
        )

        # - That the Locale source method was called
        #   to retrieve data to display
        mock_word_study_locale_source.get_presentation_data.assert_called_once_with()
