"""Test configuration."""

import uuid
from unittest.mock import Mock

import pytest

from wse.api.foreign import schemas
from wse.core.navigation.navigator import Navigator
from wse.feature import observer
from wse.feature.observer.subject import Subject


@pytest.fixture
def mock_navigator() -> Mock:
    """Moc navigator fixture."""
    return Mock(spec=Navigator)


@pytest.fixture
def subject() -> Subject:
    """Mock container content fixture."""
    return Subject()


@pytest.fixture
def mock_subject() -> Mock:
    """Mock container content fixture."""
    return Mock(spec=observer.SubjectABC)


@pytest.fixture
def mock_observer() -> Mock:
    """Mock container content fixture."""
    return Mock()


# Data fixtures
# -------------


@pytest.fixture
def word_data() -> schemas.PresentationSchema:
    """Word data fixture."""
    return schemas.PresentationSchema(
        definition='test',
        explanation='тест',
        info=schemas.Info(
            progress=3,
        ),
    )


@pytest.fixture
def word_case(
    word_data: schemas.PresentationSchema,
) -> schemas.PresentationSchema:
    """Word study case fixture."""
    return schemas.PresentationCase(
        case_uuid=str(uuid.uuid4()),
        definition=word_data.definition,
        explanation=word_data.explanation,
    )
