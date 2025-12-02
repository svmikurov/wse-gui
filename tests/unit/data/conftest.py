"""Foreign discipline fixtures."""

from dataclasses import asdict
from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import params as fixtures
from tests.unit.api.foreign.presentation import cases
from wse.api.foreign import WordPresentationApiABC
from wse.data.dto import foreign as dto
from wse.data.repos.foreign import WordParametersRepoABC
from wse.data.schemas import foreign as schemas
from wse.data.sources.foreign import (
    WordParametersLocaleSourceABC,
    WordParametersNetworkSourceABC,
    WordStudyProgressNetworkSourceABC,
)
from wse.data.sources.foreign.study import (
    WordPresentationNetworkSource,
)

# Data
# ~~~~


@pytest.fixture
def presentation_response_payload() -> cases.ResponseDict:
    """Provide Presentation response payload."""
    return cases.VALID_RESPONSE_PAYLOAD


@pytest.fixture
def presentation_schema() -> schemas.PresentationCase:
    """Provide Presentation case schema."""
    return schemas.PresentationCase.from_dict(
        cases.VALID_RESPONSE_PAYLOAD['data']  # type: ignore[arg-type]
    )


@pytest.fixture(scope='package')
def initial_parameters_dto() -> dto.InitialParameters:
    """Provide Word study initial parameters DTO."""
    return fixtures.INITIAL_PARAMETERS_DTO


@pytest.fixture
def presentation_request_schema(
    initial_parameters_dto: dto.InitialParameters,
) -> schemas.RequestPresentation:
    """Provide Presentation response payload."""
    return schemas.RequestPresentation.from_dict(
        asdict(initial_parameters_dto)
    )


# Mocked dependencies
# ~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def mock_word_progress_source() -> Mock:
    """Mock the Word study progress source."""
    return Mock(spec=WordStudyProgressNetworkSourceABC)


@pytest.fixture
def mock_network_source() -> Mock:
    """Mock the Word study parameters Network source."""
    return Mock(spec=WordParametersNetworkSourceABC)


@pytest.fixture
def mock_locale_source() -> Mock:
    """Mock the Word study parameters Locale source."""
    return Mock(spec=WordParametersLocaleSourceABC)


@pytest.fixture
def mock_word_params_repo() -> Mock:
    """Mock the Word study parameters repository."""
    return Mock(spec=WordParametersRepoABC)


# Dependencies
# ~~~~~~~~~~~~


@pytest.fixture
def mock_api_client(
    presentation_schema: schemas.PresentationCase,
) -> Mock:
    """Mock Presentation api client."""
    mock = Mock(spec=WordPresentationApiABC)
    mock.fetch.return_value = presentation_schema
    return mock


@pytest.fixture
def network_source(
    mock_api_client: Mock,
) -> WordPresentationNetworkSource:
    """Provide Presentation Network source."""
    return WordPresentationNetworkSource(
        _presentation_api=mock_api_client,
    )
