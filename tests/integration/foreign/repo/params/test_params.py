"""Word study presentation Parameters tests."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import params as fixtures
from wse.data.dto import foreign as dto

if TYPE_CHECKING:
    from wse.data.repos import foreign as repos
    from wse.data.sources import foreign as sources


@pytest.fixture
def expected_settings() -> dto.PresentationSettings:
    """Provide expected presentation settings."""
    return dto.PresentationSettings(
        question_timeout=fixtures.SETTINGS['question_timeout'],
        answer_timeout=fixtures.SETTINGS['answer_timeout'],
    )


class TestPresentationSettings:
    """Presentation settings tests."""

    def test_request_settings(
        self,
        mock_http_client: Mock,
        locale_parameters_source: sources.WordParametersLocaleSource,
        word_params_repo: repos.WordParametersRepo,
        expected_settings: dto.PresentationSettings,
    ) -> None:
        """Test that settings has been request if it not set."""
        # Act
        settings = word_params_repo.get_settings()

        # Assert
        assert vars(locale_parameters_source._data) == vars(
            fixtures.PARAMETERS_DTO
        )
        assert expected_settings == settings
        mock_http_client.get.assert_called_once()

    def test_get_requested_settings(
        self,
        mock_http_client: Mock,
        locale_parameters_source: sources.WordParametersLocaleSource,
        word_params_repo: repos.WordParametersRepo,
        expected_settings: dto.PresentationSettings,
    ) -> None:
        """Test the getting of already requested settings."""
        # Arrange
        locale_parameters_source.set_initial(fixtures.INITIAL_PARAMETERS_DTO)

        # Act
        settings = word_params_repo.get_settings()

        # Assert
        assert expected_settings == settings
        mock_http_client.get.assert_not_called()
