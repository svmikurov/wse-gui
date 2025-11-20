"""Word study Presentation params repository tests."""

from unittest.mock import Mock

import pytest

from wse.data.repos.foreign import params as repo
from wse.data.sources import foreign as source


@pytest.fixture
def mock_locale_source() -> Mock:
    """Mock the Word study progress source."""
    return Mock(spec=source.WordParamsLocaleSourceABC)


@pytest.fixture
def mock_network_source() -> Mock:
    """Mock the Word study Presentation params Network source."""
    return Mock(spec=source.WordParamsNetworkSourceABC)


@pytest.fixture
def params_repo(
    mock_network_source: Mock,
    mock_locale_source: Mock,
) -> repo.WordParamsRepo:
    """Provide Word study params repository."""
    return repo.WordParamsRepo(
        _network_source=mock_network_source,
        _local_source=mock_locale_source,
    )


class TestGetData:
    """Get data tests of Word study Presentation params repository."""

    def test_fetch_params(
        self,
        mock_network_source: Mock,
        mock_locale_source: Mock,
        params_repo: repo.WordParamsRepo,
    ) -> None:
        """Test that fetch params data."""
        # Arrange
        mock_network_data = Mock()
        mock_network_source.fetch_params.return_value = mock_network_data

        # Act
        params_repo.fetch_params()

        # Assert
        # - Locale source called with Network source data
        mock_locale_source.set_initial_params.assert_called_once_with(
            mock_network_data
        )

    def test_get_locale_source_data(
        self,
        mock_locale_source: Mock,
        params_repo: repo.WordParamsRepo,
    ) -> None:
        """Test that locale source called to get data."""
        # Act
        params_repo.get_params()

        # Assert
        mock_locale_source.get_params.assert_called_once_with()


class TestUpdateData:
    """Update data tests of Word study Presentation params repo."""

    def test_network_success_updated(
        self,
        mock_locale_source: Mock,
        mock_network_source: Mock,
        params_repo: repo.WordParamsRepo,
    ) -> None:
        """Test that Locale source called with Network source data."""
        # Arrange
        mock_state_data = Mock()
        mock_updated_data = Mock()

        mock_network_source.save_initial_params.return_value = (
            mock_updated_data
        )

        # Act
        params_repo.update_params(mock_state_data)

        # Assert
        # - Network source called with UIState data
        mock_network_source.save_initial_params.assert_called_once_with(
            mock_state_data
        )
        # - Locale source called with Network source updated data
        mock_locale_source.update_initial_params.assert_called_once_with(
            mock_updated_data
        )

    def test_network_update_error(
        self,
        mock_locale_source: Mock,
        mock_network_source: Mock,
        params_repo: repo.WordParamsRepo,
    ) -> None:
        """Test that Locale source called with data."""
        # Arrange
        mock_state_data = Mock()
        mock_network_source.save_initial_params.side_effect = Exception()

        # Act
        # - Network source raised an exception.
        params_repo.update_params(mock_state_data)

        # Assert
        mock_network_source.save_initial_params.assert_called_once_with(
            mock_state_data
        )
        # - Locale source called with UIState data
        mock_locale_source.update_initial_params.assert_called_once_with(
            mock_state_data
        )
