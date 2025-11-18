"""Test Word study screen fixtures."""

from unittest.mock import Mock

import pytest
from injector import Injector

from wse import di
from wse.domain.foreign import WordStudyUseCaseABC
from wse.domain.text import TextHyphenationABC
from wse.feature.observer.subject import Subject
from wse.ui.foreign.study.state import WordPresentationViewModel
from wse.ui.foreign.study.view import StudyForeignView


@pytest.fixture
def injector() -> Injector:
    """Provide dependency injector fixture."""
    return di.create_injector()


@pytest.fixture
def word_study_view(
    injector: Injector,
) -> StudyForeignView:
    """Provide Word study View fixture."""
    return injector.get(StudyForeignView)


@pytest.fixture
def mock_study_use_case() -> Mock:
    """Mock Word study UseCase."""
    return Mock(spec=WordStudyUseCaseABC)


@pytest.fixture
def mock_normalize_use_case() -> Mock:
    """Mock text normalization UseCase."""
    return Mock(spec=TextHyphenationABC)


@pytest.fixture
def view_model(
    mock_navigator: Mock,
    subject: Subject,
    mock_study_use_case: Mock,
    mock_normalize_use_case: Mock,
) -> WordPresentationViewModel:
    """Get Word study presentation ViewModel fixture."""
    return WordPresentationViewModel(
        _navigator=mock_navigator,
        _subject=subject,
        _study_case=mock_study_use_case,
        _normalize_case=mock_normalize_use_case,
    )
