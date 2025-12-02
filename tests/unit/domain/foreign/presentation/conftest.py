"""Configuration for domain tests."""

import asyncio
from unittest.mock import AsyncMock, Mock

import pytest

from wse.data.repos import foreign as repos
from wse.domain.abc import PresentationABC
from wse.domain.foreign.presentation import WordStudyUseCase
from wse.domain.presentation import Presentation

# Domain fixtures
# ---------------


@pytest.fixture
def mock_start_case_event() -> AsyncMock:
    """Mock start case event."""
    return AsyncMock(spec=asyncio.Event)


@pytest.fixture
def mock_definition_event() -> AsyncMock:
    """Mock definition event."""
    return AsyncMock(spec=asyncio.Event)


@pytest.fixture
def mock_explanation_event() -> AsyncMock:
    """Mock explanation event."""
    return AsyncMock(spec=asyncio.Event)


@pytest.fixture
def mock_end_case_event() -> AsyncMock:
    """Mock end case event."""
    return AsyncMock(spec=asyncio.Event)


@pytest.fixture
def mock_complete_phase_event() -> AsyncMock:
    """Mock complete phase event."""
    return AsyncMock(spec=asyncio.Event)


@pytest.fixture
def mock_unpause_event() -> AsyncMock:
    """Mock unpause event."""
    return AsyncMock(spec=asyncio.Event)


@pytest.fixture
def mock_progress_queue() -> AsyncMock:
    """Mock progress queue."""
    return AsyncMock(spec=asyncio.Queue)


@pytest.fixture
def mock_domain() -> AsyncMock:
    """Mock domain."""
    return Mock(spec=PresentationABC)


@pytest.fixture
def mock_presentation_domain(
    mock_start_case_event: AsyncMock,
    mock_definition_event: AsyncMock,
    mock_explanation_event: AsyncMock,
    mock_end_case_event: AsyncMock,
    mock_unpause_event: AsyncMock,
    mock_progress_queue: AsyncMock,
    mock_complete_phase_event: AsyncMock,
) -> Presentation:
    """Presentation domain fixture."""
    return Presentation(
        start_case_event=mock_start_case_event,
        definition_event=mock_definition_event,
        explanation_event=mock_explanation_event,
        end_case_event=mock_end_case_event,
        unpause_event=mock_unpause_event,
        progress_queue=mock_progress_queue,
        complete_phase_event=mock_complete_phase_event,
    )


@pytest.fixture
def presentation() -> Presentation:
    """Presentation domain fixture."""
    return Presentation(
        start_case_event=asyncio.Event(),
        definition_event=asyncio.Event(),
        explanation_event=asyncio.Event(),
        end_case_event=asyncio.Event(),
        unpause_event=asyncio.Event(),
        complete_phase_event=asyncio.Event(),
        progress_queue=asyncio.Queue(),
    )


# Domain dependencies
# ~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def mock_get_word_repo() -> Mock:
    """Mock the repo to get Word study case fixture."""
    return Mock(spec=repos.WordPresentationRepoABC)


@pytest.fixture
def mock_progress_repo() -> Mock:
    """Mock the Word study progress fixture."""
    return Mock(spec=repos.WordProgressRepoABC)


@pytest.fixture
def mock_settings_repo() -> Mock:
    """Mock the Word study progress fixture."""
    return Mock(spec=repos.WordParametersRepoABC)


# Tested domain
# ~~~~~~~~~~~~~


@pytest.fixture
def use_case_di_mock(
    mock_subject: Mock,
    mock_get_word_repo: Mock,
    mock_progress_repo: Mock,
    mock_settings_repo: Mock,
    mock_domain: Mock,
) -> WordStudyUseCase:
    """Word study UseCase fixture."""
    return WordStudyUseCase(
        _subject=mock_subject,
        _get_word_repo=mock_get_word_repo,
        _progress_repo=mock_progress_repo,
        _settings_repo=mock_settings_repo,
        _domain=mock_domain,
    )
