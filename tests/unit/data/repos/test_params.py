"""Word study Presentation params repository tests."""

from unittest.mock import Mock

from wse.data.repos.foreign.params import WordParamsRepo
from wse.data.sources.foreign import schemas


class TestParams:
    """Word study Presentation params repository tests."""

    def test_get_presentation_params(
        self,
        mock_locale_params_source: Mock,
        presentation_params: schemas.PresentationCase,
        word_study_params_repo: WordParamsRepo,
    ) -> None:
        """Test get presentation params."""
        # Arrange
        mock_locale_params_source.get_params.return_value = presentation_params

        # Act
        data = word_study_params_repo.get_params()

        # Assert
        mock_locale_params_source.get_params.assert_called_once_with()
        assert data == presentation_params
