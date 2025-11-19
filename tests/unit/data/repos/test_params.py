"""Word study Presentation params repository tests."""

from unittest.mock import Mock

import pytest

from wse.api.foreign import requests, schemas
from wse.data.repos.foreign import params as repo


@pytest.fixture
def updated_params_data() -> requests.InitialParams:
    """Provide expected initial UIState data for network store."""
    return requests.InitialParams(
        category=requests.IdName(id=1, name='test category'),
        label=requests.IdName(id=7, name='test label'),
    )


class TestParams:
    """Word study Presentation params repository tests."""

    def test_get_presentation_params(
        self,
        mock_locale_params_source: Mock,
        presentation_params: schemas.PresentationCase,
        word_study_params_repo: repo.WordParamsRepo,
    ) -> None:
        """Test get presentation params."""
        # Arrange
        mock_locale_params_source.get_params.return_value = presentation_params

        # Act
        data = word_study_params_repo.get_params()

        # Assert
        mock_locale_params_source.get_params.assert_called_once_with()
        assert data == presentation_params

    def test_save_params_success(
        self,
        mock_locale_params_source: Mock,
        mock_network_params_source: Mock,
        word_study_params_repo: repo.WordParamsRepo,
        updated_params_data: requests.InitialParams,
    ) -> None:
        """Save initial params success test."""
        # Act
        word_study_params_repo.save_params(updated_params_data)

        # Assert
        mock_locale_params_source.update_initial_params.assert_called_once_with(
            updated_params_data
        )
        mock_network_params_source.save_initial_params.assert_called_once_with(
            updated_params_data
        )
