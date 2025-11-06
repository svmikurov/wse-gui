"""Configuration for domain tests."""

import asyncio
import pytest
from unittest.mock import AsyncMock, Mock

from wse.domain.presentation import Presentation
from wse.data.repositories import foreign as repo
from wse.domain.foreign.study import WordStudyUseCase
from wse.feature.observer.subject import Subject

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
def mock_unpause_event() -> AsyncMock:
    """Mock unpause event."""
    return AsyncMock(spec=asyncio.Event)


@pytest.fixture
def mock_progress_queue() -> AsyncMock:
    """Mock progress queue."""
    return AsyncMock(spec=asyncio.Queue)


@pytest.fixture
def mock_presentation_domain(
    mock_start_case_event: AsyncMock,
    mock_definition_event: AsyncMock,
    mock_explanation_event: AsyncMock,
    mock_end_case_event: AsyncMock,
    mock_unpause_event: AsyncMock,
    mock_progress_queue: AsyncMock,
) -> Presentation:
    """Presentation domain fixture."""
    return Presentation(
        start_case_event=mock_start_case_event,
        definition_event=mock_definition_event,
        explanation_event=mock_explanation_event,
        end_case_event=mock_end_case_event,
        unpause_event=mock_unpause_event,
        progress_queue=mock_progress_queue,
    )


# Repository fixtures
# -------------------


@pytest.fixture
def mock_case_repo() -> Mock:
    """Mock the repo to get Word study case fixture."""
    return Mock(spec=repo.WordStudyCaseRepoABC)


@pytest.fixture
def mock_progress_repo() -> Mock:
    """Mock the Word study progress fixture."""
    return Mock(spec=repo.WordStudyProgressRepoABC)


@pytest.fixture
def mock_settings_repo() -> Mock:
    """Mock the Word study settings fixture."""
    return Mock(spec=repo.WordStudySettingsRepoABC)


# UseCase fixture
# ---------------

@pytest.fixture
def use_case(
    subject: Subject,
    mock_case_repo: Mock,
    mock_progress_repo: Mock,
    mock_settings_repo: Mock,
    mock_presentation_domain: Presentation,

) -> WordStudyUseCase:
    """Word study UseCase fixture."""
    return WordStudyUseCase(
        _subject=subject,
        _get_word_repo=mock_case_repo,
        _progress_repo=mock_progress_repo,
        _settings_repo=mock_settings_repo,
        _domain=mock_presentation_domain,
    )