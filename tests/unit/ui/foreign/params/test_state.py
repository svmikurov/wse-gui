"""Test Word study params ViewModel."""

from unittest.mock import Mock, call

import pytest

from wse.api.foreign import requests
from wse.data.repos import foreign as repo
from wse.feature.observer.subject import Subject
from wse.ui.foreign import params
from wse.ui.foreign.params import state

# Test data fixtures
# ------------------


@pytest.fixture
def params_dto() -> requests.PresentationParamsDTO:
    """Presentation parameters DTO to updated UIState."""
    # Presentation parameters
    category = requests.IdName(id=1, name='category 1')
    mark = requests.IdName(id=1, name='mark 1')
    source = requests.IdName(id=1, name='source 1')

    return requests.PresentationParamsDTO(
        # - Choices
        categories=[category],
        marks=[mark],
        sources=[source],
        # - Initial choice
        category=category,
        mark=mark,
        word_source=source,
    )


@pytest.fixture
def state_data(
    params_dto: requests.PresentationParamsDTO,
) -> state.PresentationParamsData:
    """Provide UIState data."""
    return state.PresentationParamsData(
        category=params_dto.category,
        mark=params_dto.mark,
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
    subject: Subject,
    state_data: state.PresentationParamsData,
) -> state.WordStudyParamsViewModel:
    """Provide ViewModel."""
    return state.WordStudyParamsViewModel(
        _subject=subject,
        _navigator=Mock(),
        _data=state_data,
        _repo=mock_repo,
        _source_subscriber=Mock(),
    )


class TestViewApiContract:
    """View api contract test."""

    # TODO: Add tests:
    # - Test that UIState success updated with widget data.
    # - Reset selected params success test

    def test_save_params_success(
        self,
        mock_repo: Mock,
        view_model_di_mock: state.WordStudyParamsViewModel,
        params_dto: requests.PresentationParamsDTO,
    ) -> None:
        """Save initial params success test."""
        # Arrange
        expected_call = requests.InitialParams(
            category=params_dto.category,
            mark=params_dto.mark,
        )
        # Act
        view_model_di_mock.save_params()

        # Assert
        mock_repo.update_params.assert_called_once_with(expected_call)


class TestViewModelNotifications:
    """Parameters ViewModel notifications tests."""

    def test_parameters_updated_notification(
        self,
        view_model_di_mock: state.WordStudyParamsViewModel,
        params_dto: requests.PresentationParamsDTO,
    ) -> None:
        """Test that View was notified with Parameters."""
        # Arrange
        # - Expected notifications
        choices = [
            call(accessor='mark', values=[params_dto.mark]),
            call(accessor='category', values=[params_dto.category]),
            call(accessor='word_source', values=[params_dto.word_source]),
        ]
        initial_choice = [
            call(accessor='mark', value=params_dto.mark),
            call(accessor='category', value=params_dto.category),
            call(accessor='word_source', value=params_dto.word_source),
        ]
        # - Mock and subscribe View to notifications
        mock_view = Mock(spec=params.WordStudyParamsViewABC)
        view_model_di_mock.add_observer(mock_view)

        # Act
        view_model_di_mock.initial_params_updated(params_dto)

        # Assert
        assert mock_view.values_updated.call_args_list == choices
        assert mock_view.value_updated.call_args_list == initial_choice


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
