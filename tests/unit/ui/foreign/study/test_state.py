"""Tests of Word study via presentation the ViewModel."""

from unittest.mock import Mock

import pytest

from wse.domain.foreign import WordStudyUseCaseABC
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
