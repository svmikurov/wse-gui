"""Word study parameters repository tests."""

from __future__ import annotations

from typing import TYPE_CHECKING
from unittest.mock import Mock

if TYPE_CHECKING:
    from wse.data.repos.foreign import params as repo


class TestGetData:
    """Get data tests of Word study Presentation params repository."""

    def test_fetch_params(
        self,
        mock_network_source: Mock,
        mock_locale_source: Mock,
        params_repo: repo.WordParametersRepo,
    ) -> None:
        """Test that fetch params data."""
        # Arrange
        mock_network_data = Mock()
        mock_network_source.fetch.return_value = mock_network_data

        # Act
        params_repo.fetch()

        # Assert
        # - Locale source called with Network source data
        mock_locale_source.update.assert_called_once_with(mock_network_data)


class TestUpdateData:
    """Update data tests of Word study Presentation params repo."""

    def test_network_success_updated(
        self,
        mock_locale_source: Mock,
        mock_network_source: Mock,
        params_repo: repo.WordParametersRepo,
    ) -> None:
        """Test that Locale source called with Network source data."""
        # Arrange
        mock_state_data = Mock()
        mock_updated_data = Mock()

        mock_network_source.save.return_value = mock_updated_data

        # Act
        params_repo.save(mock_state_data)

        # Assert
        # - Network source called with UIState data
        mock_network_source.save.assert_called_once_with(mock_state_data)

        # - Locale source called with Network source updated data
        mock_locale_source.update.assert_called_once_with(mock_updated_data)

    def test_network_update_error(
        self,
        mock_locale_source: Mock,
        mock_network_source: Mock,
        params_repo: repo.WordParametersRepo,
    ) -> None:
        """Test that Locale source called with data."""
        # Arrange
        mock_state_data = Mock()
        mock_network_source.save.side_effect = Exception()

        # Act
        # - Network source raised an exception.
        params_repo.save(mock_state_data)

        # Assert
        mock_network_source.save.assert_called_once_with(mock_state_data)

        # - Locale source called with UIState data
        mock_locale_source.update.assert_called_once_with(mock_state_data)
