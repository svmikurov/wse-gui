"""Foreign repositories test configuration."""

from unittest.mock import Mock

import pytest

from tests.unit.api.foreign.presentation import cases
from wse.data.repos.foreign import progress, study
from wse.data.sources import foreign as sources
from wse.data.sources.foreign import schemas

# Data fixtures


@pytest.fixture
def params() -> schemas.PresentationParams:
    """Provide Presentation case params."""
    return schemas.PresentationParams.from_dict(cases.REQUEST_PAYLOAD)  # type: ignore[arg-type]


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
