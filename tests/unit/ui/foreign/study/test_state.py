"""Tests of Word study via presentation the ViewModel."""

from unittest.mock import Mock

import pytest

from wse.ui.containers.control import Action
from wse.ui.foreign.study import WordPresentationViewModelObserverABC
from wse.ui.foreign.study.state import WordPresentationViewModel


class TestOnOpen:
    """Test `on_open()` method."""

    def test_domain_call(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test that domain calls on screen open."""
        view_model.on_open()
        mock_study_use_case.start.assert_called_once_with()


class TestDomainObserve:
    """Test the correct handle of Domain notification."""

    @pytest.fixture
    def mock_state_observer(self) -> Mock:
        """Mock ViewModel observer."""
        return Mock(spec=WordPresentationViewModelObserverABC)

    def test_exercise_updated(
        self,
        mock_state_observer: Mock,
        mock_normalize_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle of notification of 'exercise_updated'."""
        # Arrange
        view_model.add_observer(mock_state_observer)
        mock_normalize_use_case.adapt.return_value = 'test'

        # Act
        view_model.exercise_updated(accessor='definition', value='test')

        # Assert
        mock_state_observer.change.assert_called_once_with(
            accessor='definition', value='test'
        )
        mock_normalize_use_case.adapt.assert_called_once_with('test')

    def test_timeout_updated(
        self,
        mock_state_observer: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle of notification of 'timeout_updated'."""
        view_model.add_observer(mock_state_observer)
        view_model.timeout_updated(accessor='timeout', max=0.1, value=0.2)

        mock_state_observer.timeout_updated.assert_called_once_with(
            accessor='timeout', max=0.1, value=0.2
        )


class TestActionHandle:
    """Test the correct handle of user actions by ViewModel."""

    def test_pause(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle 'pause' action."""
        view_model.handle(action=Action.PAUSE)

        mock_study_use_case.pause.assert_called_once()
        mock_study_use_case.unpause.assert_not_called()
        mock_study_use_case.next.assert_not_called()
        mock_study_use_case.known.assert_not_called()
        mock_study_use_case.unknown.assert_not_called()

    def test_unpause(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle 'unpause' action."""
        view_model.handle(action=Action.UNPAUSE)

        mock_study_use_case.pause.assert_not_called()
        mock_study_use_case.unpause.assert_called_once()
        mock_study_use_case.next.assert_not_called()
        mock_study_use_case.known.assert_not_called()
        mock_study_use_case.unknown.assert_not_called()

    def test_next(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle 'next' action."""
        view_model.handle(action=Action.NEXT)

        mock_study_use_case.pause.assert_not_called()
        mock_study_use_case.unpause.assert_not_called()
        mock_study_use_case.next.assert_called_once()
        mock_study_use_case.known.assert_not_called()
        mock_study_use_case.unknown.assert_not_called()

    def test_known(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle 'known' action."""
        view_model.handle(action=Action.KNOWN)

        mock_study_use_case.pause.assert_not_called()
        mock_study_use_case.unpause.assert_not_called()
        mock_study_use_case.next.assert_not_called()
        mock_study_use_case.known.assert_called_once()
        mock_study_use_case.unknown.assert_not_called()

    def test_unknown(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle 'unknown' action."""
        view_model.handle(action=Action.UNKNOWN)

        mock_study_use_case.pause.assert_not_called()
        mock_study_use_case.unpause.assert_not_called()
        mock_study_use_case.next.assert_not_called()
        mock_study_use_case.known.assert_not_called()
        mock_study_use_case.unknown.assert_called_once()


class TestViewModelInitialization:
    """Word study Presentation ViewModel initialization test."""

    def test_success_initialization(
        self,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test that the ViewModel is initialized successfully."""
        assert view_model
