"""Tests of Word study via presentation the ViewModel."""

from unittest.mock import Mock

import pytest

from wse.domain.foreign import WordStudyUseCaseABC
from wse.ui.containers.control import Action
from wse.ui.foreign.study.state import WordPresentationViewModel


@pytest.fixture
def mock_study_use_case() -> Mock:
    """Mock Word study UseCase."""
    return Mock(spec=WordStudyUseCaseABC)


@pytest.fixture
def view_model(
    mock_navigator: Mock,
    mock_subject: Mock,
    mock_study_use_case: Mock,
) -> WordPresentationViewModel:
    """Get Word study presentation ViewModel fixture."""
    return WordPresentationViewModel(
        _navigator=mock_navigator,
        _subject=mock_subject,
        _study_case=mock_study_use_case,
    )


class TestViewNotifications:
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
