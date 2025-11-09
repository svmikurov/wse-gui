"""Test configuration."""

import pytest
import uuid

from unittest.mock import Mock

from wse.core.navigation.navigator import Navigator
from wse.feature import observer
from wse.feature.observer.subject import Subject
from wse.data.sources.foreign import schema


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
def word_data() -> schema.WordPresentationSchema:
    """Word data fixture."""
    return schema.WordPresentationSchema(definition='test', explanation='тест')


@pytest.fixture
def word_case(
    word_data: schema.WordPresentationSchema,
) -> schema.WordPresentationSchema:
    """Word study case fixture."""
    return schema.WordStudyCaseSchema(
        case_uuid=uuid.uuid4(),
        definition=word_data.definition,
        explanation=word_data.explanation,
    )