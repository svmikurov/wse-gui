"""Tests of Word study via presentation the ViewModel."""

from unittest.mock import Mock

import pytest

from wse.domain.foreign import WordStudyUseCaseABC
from wse.feature.observer.subject import Subject
from wse.ui.containers.control import Action
from wse.ui.foreign.study import WordPresentationViewModelObserverABC
from wse.ui.foreign.study.state import WordPresentationViewModel


@pytest.fixture
def mock_study_use_case() -> Mock:
    """Mock Word study UseCase."""
    return Mock(spec=WordStudyUseCaseABC)


@pytest.fixture
def view_model(
    mock_navigator: Mock,
    subject: Subject,
    mock_study_use_case: Mock,
) -> WordPresentationViewModel:
    """Get Word study presentation ViewModel fixture."""
    return WordPresentationViewModel(
        _navigator=mock_navigator,
        _subject=subject,
        _study_case=mock_study_use_case,
    )


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
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle of notification of 'exercise_updated'."""
        view_model.add_observer(mock_state_observer)
        view_model.exercise_updated(accessor='definition', value='test')

        mock_state_observer.change.assert_called_once_with(
            accessor='definition', value='test'
        )

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


class TestViewObserve:
    """Test the correct handle of View notification."""

    def test_pause(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle of notification with 'pause'."""
        view_model.handle(action=Action.PAUSE)

        mock_study_use_case.pause.assert_called_once()
        mock_study_use_case.next.assert_not_called()
        mock_study_use_case.known.assert_not_called()
        mock_study_use_case.unknown.assert_not_called()

    def test_next(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle of notification with 'next'."""
        view_model.handle(action=Action.NEXT)

        mock_study_use_case.pause.assert_not_called()
        mock_study_use_case.next.assert_called_once()
        mock_study_use_case.known.assert_not_called()
        mock_study_use_case.unknown.assert_not_called()

    def test_known(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle of notification with 'known'."""
        view_model.handle(action=Action.KNOWN)

        mock_study_use_case.pause.assert_not_called()
        mock_study_use_case.next.assert_not_called()
        mock_study_use_case.known.assert_called_once()
        mock_study_use_case.unknown.assert_not_called()

    def test_unknown(
        self,
        mock_study_use_case: Mock,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test the handle of notification with 'unknown'."""
        view_model.handle(action=Action.UNKNOWN)

        mock_study_use_case.pause.assert_not_called()
        mock_study_use_case.next.assert_not_called()
        mock_study_use_case.known.assert_not_called()
        mock_study_use_case.unknown.assert_called_once()


class TestWordPresentationViewModel:
    """Tests of Word study via presentation the ViewModel."""

    def test_view_model_has_correct_attributes(
        self,
        view_model: WordPresentationViewModel,
    ) -> None:
        """Test that ViewModel has all required attributes."""
        assert view_model._navigator is not None
        assert view_model._subject is not None
        assert view_model._study_case is not None
