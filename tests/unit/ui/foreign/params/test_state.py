"""Test Word study params ViewModel."""

from unittest.mock import Mock, call

import pytest

from tests.fixtures.foreign import parameters as fixtures
from wse.data.dto import foreign as dto
from wse.data.repos import foreign as repo
from wse.feature.observer.subject import Subject
from wse.ui.foreign.params import WordStudyParamsViewABC, state

# Test data fixtures
# ------------------


@pytest.fixture(scope='session')
def parameters_dto() -> dto.PresentationParameters:
    """Provide Word study parameters DTO."""
    return fixtures.PARAMETERS_DTO


@pytest.fixture
def state_data(
    parameters_dto: dto.PresentationParameters,
) -> state.WordParametersUIState:
    """Provide UIState data."""
    return state.WordParametersUIState(
        category=parameters_dto.category,
        mark=parameters_dto.mark,
    )


# Dependency mock fixtures
# ------------------------


@pytest.fixture
def mock_repo() -> Mock:
    """Mock repository."""
    return Mock(spec=repo.WordParametersRepoABC)


# Test ViewModel fixture
# ----------------------


@pytest.fixture
def view_model_di_mock(
    mock_repo: Mock,
    subject: Subject,
    state_data: state.WordParametersUIState,
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

    def test_save_params_success(
        self,
        mock_repo: Mock,
        view_model_di_mock: state.WordStudyParamsViewModel,
        parameters_dto: dto.PresentationParameters,
    ) -> None:
        """Save initial params success test."""
        # Arrange
        expected_call = dto.InitialParameters(
            category=parameters_dto.category,
            mark=parameters_dto.mark,
        )
        # Act
        view_model_di_mock.save_params()

        # Assert
        mock_repo.save.assert_called_once_with(expected_call)


class TestViewModelNotifications:
    """Parameters ViewModel notifications tests."""

    def test_parameter_values_updated_notification(
        self,
        view_model_di_mock: state.WordStudyParamsViewModel,
        parameters_dto: dto.PresentationParameters,
    ) -> None:
        """Test that View was notified with **options**."""
        # Arrange
        # - Expected notifications
        choices = [
            call(
                accessor='category',
                values=[dto.NOT_SELECTED, *parameters_dto.categories],
            ),
            call(
                accessor='mark',
                values=[dto.NOT_SELECTED, *parameters_dto.marks],
            ),
            call(
                accessor='word_source',
                values=[dto.NOT_SELECTED, *parameters_dto.sources],
            ),
            call(
                accessor='start_period',
                values=[dto.NOT_SELECTED, *parameters_dto.periods],
            ),
            call(
                accessor='end_period',
                values=[dto.NOT_SELECTED, *parameters_dto.periods],
            ),
            call(
                accessor='translation_order',
                values=parameters_dto.translation_orders,
            ),
        ]
        # - Mock and subscribe View to notifications
        mock_view = Mock(spec=WordStudyParamsViewABC)
        view_model_di_mock.add_observer(mock_view)

        # Act
        view_model_di_mock.params_updated(parameters_dto)

        # Assert
        assert mock_view.values_updated.call_args_list == choices

    def test_parameter_value_updated_notification(
        self,
        view_model_di_mock: state.WordStudyParamsViewModel,
        parameters_dto: dto.PresentationParameters,
    ) -> None:
        """Test that View was notified with **initial value**."""
        # - Expected notifications
        initial_choice = [
            call(accessor='question_timeout', value=2),
            call(accessor='answer_timeout', value=2),
            call(accessor='word_count', value=90),
            call(accessor='is_study', value=True),
            call(accessor='is_repeat', value=False),
            call(accessor='is_examine', value=True),
            call(accessor='is_know', value=False),
            call(accessor='category', value=dto.IdName('2', 'category 2')),
            call(accessor='mark', value=dto.IdName('2', 'mark')),
            call(accessor='word_source', value=dto.IdName('2', 'source 2')),
            call(
                accessor='translation_order',
                value=dto.CodeName('to_native', 'На родной язык'),
            ),
            call(
                accessor='start_period', value=dto.IdName('2', 'week_before')
            ),
            call(accessor='end_period', value=dto.IdName('2', 'week_before')),
        ]
        # - Mock and subscribe View to notifications
        mock_view = Mock(spec=WordStudyParamsViewABC)
        view_model_di_mock.add_observer(mock_view)

        # Act
        view_model_di_mock.params_updated(parameters_dto)

        # Assert
        assert mock_view.value_updated.call_args_list == initial_choice


class TestInitialization:
    """Word study params ViewModel instance initialization test."""

    def test_instance_initialization_success(
        self,
        view_model_di_mock: state.WordStudyParamsViewModel,
    ) -> None:
        """Test success view model instance initialization."""
        assert view_model_di_mock
