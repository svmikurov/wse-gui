"""Test Word study params ViewModel."""

from unittest.mock import Mock

import pytest

from wse.api.foreign import requests
from wse.data.repos import foreign as repo
from wse.ui.foreign.params import state

# Test data fixtures
# ------------------


@pytest.fixture
def state_data() -> state.PresentationParamsData:
    """Provide UIState data."""
    return state.PresentationParamsData(
        category=requests.IdName(id=1, name='test category'),
        label=requests.IdName(id=7, name='test label'),
    )


@pytest.fixture
def expected_initial_data() -> requests.InitialParams:
    """Provide expected initial UIState data for network store."""
    return requests.InitialParams(
        category=requests.IdName(id=1, name='test category'),
        label=requests.IdName(id=7, name='test label'),
    )


# Dependency mock fixtures
# ------------------------


@pytest.fixture
def mock_repo() -> Mock:
    """Mock repository."""
    return Mock(spec=repo.WordParamsRepoABC)


# Test ViewModel fixture
# ----------------------


@pytest.fixture
def view_model_di_mock(
    mock_repo: Mock,
    state_data: state.PresentationParamsData,
) -> state.WordStudyParamsViewModel:
    """Provide ViewModel."""
    return state.WordStudyParamsViewModel(
        _subject=Mock(),
        _navigator=Mock(),
        _data=state_data,
        _repo=mock_repo,
        _source_subscriber=Mock(),
    )


class TestViewApiContract:
    """View api contract test."""

    @pytest.mark.skip('Add test')
    def test_update_widget_state_success(
        self,
    ) -> None:
        """Test that UIState success updated with widget data."""

    def test_save_params_success(
        self,
        mock_repo: Mock,
        view_model_di_mock: state.WordStudyParamsViewModel,
        expected_initial_data: requests.InitialParams,
    ) -> None:
        """Save initial params success test."""
        # Act
        view_model_di_mock.save_params()

        # Assert
        mock_repo.update_params.assert_called_once_with(expected_initial_data)

    @pytest.mark.skip('Add test')
    def test_reset_params_success(
        self,
    ) -> None:
        """Reset selected params success test."""


class TestNotificationObserve:
    """Dependency notification observe test."""


class TestInitialization:
    """Word study params ViewModel instance initialization test."""

    def test_instance_initialization_success(
        self,
        view_model_di_mock: state.WordStudyParamsViewModel,
    ) -> None:
        """Test success view model instance initialization."""
        assert view_model_di_mock
