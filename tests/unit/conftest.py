"""Test configuration."""

import pytest

from unittest.mock import Mock

from wse.core.navigation.navigator import Navigator


@pytest.fixture
def mock_navigator() -> Mock:
    """Moc navigator fixture."""
    return Mock(spec=Navigator)
