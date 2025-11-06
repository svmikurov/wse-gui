"""Test configuration."""

import pytest

from unittest.mock import Mock

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