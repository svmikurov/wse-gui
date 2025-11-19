"""Foreign repositories test configuration."""

from unittest.mock import Mock

import pytest

from tests.unit.api.foreign.presentation import cases
from wse.api.foreign import schemas
from wse.data.repos.foreign import WordParamsRepoABC, progress, study
from wse.data.sources import foreign as sources

# Data fixtures


@pytest.fixture
def presentation_params() -> schemas.PresentationParams:
    """Provide Presentation case params."""
    return schemas.PresentationParams.from_dict(cases.REQUEST_PAYLOAD)  # type: ignore[arg-type]


# Source fixtures
# ---------------


@pytest.fixture
def mock_word_progress_source() -> Mock:
    """Mock the Word study progress source."""
    return Mock(spec=sources.WordStudyProgressNetworkSourceABC)


@pytest.fixture
def mock_network_params_source() -> Mock:
    """Mock the Word study Presentation params Network source."""
    return Mock(spec=sources.WordParamsNetworkSourceABC)


@pytest.fixture
def mock_locale_params_source() -> Mock:
    """Mock the Word study Presentation params Locale source."""
    return Mock(spec=sources.WordParamsLocaleSourceABC)


# Repository fixtures
# -------------------


@pytest.fixture
def mock_word_study_params_repo() -> Mock:
    """Mock Word study params repository."""
    return Mock(spec=WordParamsRepoABC)


@pytest.fixture
def word_study_repo(
    mock_word_locale_source: Mock,
    mock_word_network_source: Mock,
    mock_word_study_params_repo: Mock,
) -> study.WordStudyRepo:
    """Word study repository."""
    return study.WordStudyRepo(
        _locale_source=mock_word_locale_source,
        _network_source=mock_word_network_source,
        _params_repo=mock_word_study_params_repo,
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
