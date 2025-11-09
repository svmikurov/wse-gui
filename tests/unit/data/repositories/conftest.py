"""Foreign repositories test configuration."""

from unittest.mock import Mock

import pytest

from wse.data.repositories.foreign import study as repos
from wse.data.sources import foreign as sources


@pytest.fixture
def mock_locale_source() -> Mock:
    """Mock Word study Locale source."""
    return Mock(spec=sources.WordStudyLocaleSourceABC)


@pytest.fixture
def mock_network_source() -> Mock:
    """Mock Word study Network source."""
    return Mock(spec=sources.WordStudyNetworkSourceABC)


@pytest.fixture
def word_study_repo(
    mock_locale_source: Mock,
    mock_network_source: Mock,
) -> repos.WordStudyRepo:
    """Word study repo fixture."""
    return repos.WordStudyRepo(
        _locale_source=mock_locale_source,
        _network_source=mock_network_source,
    )
