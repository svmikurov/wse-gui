"""Foreign repositories test configuration."""

from unittest.mock import Mock

import pytest

from wse.data.repos.foreign import study, progress
from wse.data.sources import foreign as sources


# Source fixtures
# ---------------


@pytest.fixture
def mock_word_locale_source() -> Mock:
    """Mock Word study Locale source."""
    return Mock(spec=sources.WordStudyLocaleSourceABC)


@pytest.fixture
def mock_word_network_source() -> Mock:
    """Mock Word study Network source."""
    return Mock(spec=sources.WordStudyNetworkSourceABC)


@pytest.fixture
def mock_word_progress_source() -> Mock:
    """Mock the Word study progress source."""
    return Mock(spec=sources.WordStudyProgressNetworkSourceABC)


# Repository fixtures
# -------------------


@pytest.fixture
def word_study_repo(
    mock_word_locale_source: Mock,
    mock_word_network_source: Mock,
) -> study.WordStudyRepo:
    """Word study repository."""
    return study.WordStudyRepo(
        _locale_source=mock_word_locale_source,
        _network_source=mock_word_network_source,
    )


@pytest.fixture
def word_study_progress_repo(
    mock_word_locale_source: sources.WordStudyLocaleSourceABC,
    mock_word_progress_source: sources.WordStudyProgressNetworkSourceABC,
) -> progress.WordStudyProgressRepo:
    """Word study progress repository fixture."""
    return progress.WordStudyProgressRepo(
        case_source=mock_word_locale_source,
        progress_source=mock_word_progress_source,
    )
