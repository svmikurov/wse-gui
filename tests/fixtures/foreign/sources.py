"""Foreign discipline repository fixtures."""

from unittest.mock import Mock

import pytest

from wse.data.sources import foreign as sources

# Mock source
# -----------


@pytest.fixture
def mock_word_locale_source() -> Mock:
    """Mock Word study Locale source."""
    return Mock(spec=sources.WordStudyLocaleSourceABC)


@pytest.fixture
def mock_word_network_source() -> Mock:
    """Mock Word study Network source."""
    return Mock(spec=sources.WordStudyNetworkSourceABC)
