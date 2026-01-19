"""Test configuration."""

import uuid
from unittest.mock import Mock

import pytest

from wse.core.navigation.navigator import Navigator
from wse.data.schemas import foreign as schemas
from wse.feature import observer
from wse.feature.observer.subject import Subject

# Data
# ~~~~


@pytest.fixture
def word_data() -> schemas.Presentation:
    """Word data fixture."""
    return schemas.Presentation(
        question='test',
        answer='тест',
        info=schemas.Info(
            progress=3,
        ),
    )


@pytest.fixture
def word_case(
    word_data: schemas.Presentation,
) -> schemas.Presentation:
    """Word study case fixture."""
    return schemas.PresentationCase(
        case_uuid=str(uuid.uuid4()),
        question=word_data.question,
        answer=word_data.answer,
    )


# Dependencies
# ~~~~~~~~~~~~


@pytest.fixture
def subject() -> Subject:
    """Provide Subject of Observer pattern."""
    return Subject()


# Mocked dependencies
# ~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def mock_navigator() -> Mock:
    """Moc navigator fixture."""
    return Mock(spec=Navigator)


@pytest.fixture
def mock_subject() -> Mock:
    """Mock container content fixture."""
    return Mock(spec=observer.SubjectABC)


@pytest.fixture
def mock_observer() -> Mock:
    """Mock container content fixture."""
    return Mock()
