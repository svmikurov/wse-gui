"""Foreign repositories test configuration."""

from unittest.mock import Mock

import pytest

from wse.data.repos.foreign import params, progress, study
from wse.data.sources import foreign as sources


@pytest.fixture
def mock_word_study_locale_source() -> Mock:
    """Mock Word study Locale source."""
    return Mock(spec=sources.WordPresentationLocaleSourceABC)


@pytest.fixture
def mock_word_study_network_source() -> Mock:
    """Mock Word study Network source."""
    return Mock(spec=sources.WordPresentationNetworkSourceABC)


@pytest.fixture
def params_repo(
    mock_network_source: Mock,
    mock_locale_source: Mock,
) -> params.WordParametersRepo:
    """Provide Word study params repository."""
    return params.WordParametersRepo(
        _network_source=mock_network_source,
        _local_source=mock_locale_source,
    )


@pytest.fixture
def word_study_repo(
    mock_word_study_locale_source: Mock,
    mock_word_study_network_source: Mock,
    mock_word_params_repo: Mock,
) -> study.WordPresentationRepo:
    """Word study repository."""
    return study.WordPresentationRepo(
        _locale_source=mock_word_study_locale_source,
        _network_source=mock_word_study_network_source,
        _params_repo=mock_word_params_repo,
    )


@pytest.fixture
def word_study_progress_repo(
    mock_word_study_locale_source: sources.WordPresentationLocaleSourceABC,
    mock_word_progress_source: sources.WordStudyProgressNetworkSourceABC,
) -> progress.WordStudyProgressRepo:
    """Word study progress repository fixture."""
    return progress.WordStudyProgressRepo(
        case_source=mock_word_study_locale_source,
        progress_source=mock_word_progress_source,
    )
