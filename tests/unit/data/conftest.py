"""Foreign discipline fixtures."""

from unittest.mock import Mock

import pytest

from tests.unit.api.foreign.presentation import cases
from wse.api.foreign import WordStudyPresentationApiABC
from wse.data.sources.foreign import schemas, study

# Data fixtures
# -------------


@pytest.fixture
def presentation_params() -> schemas.PresentationParams:
    """Provide Presentation params."""
    return schemas.PresentationParams.from_dict(cases.REQUEST_PAYLOAD)  # type: ignore[arg-type]


@pytest.fixture
def response_payload() -> cases.ResponseDict:
    """Provide Presentation response payload."""
    return cases.VALID_RESPONSE_PAYLOAD


@pytest.fixture
def presentation_data() -> schemas.PresentationCase:
    """Provide Presentation case."""
    return schemas.PresentationCase.from_dict(
        cases.VALID_RESPONSE_PAYLOAD['data']  # type: ignore[arg-type]
    )


# Dependency fixures
# ------------------


@pytest.fixture
def mock_api_client(
    presentation_data: schemas.PresentationCase,
) -> Mock:
    """Mock Presentation api client."""
    mock = Mock(spec=WordStudyPresentationApiABC)
    mock.fetch_presentation.return_value = presentation_data
    return mock


@pytest.fixture
def network_source(
    mock_api_client: Mock,
) -> study.WordStudyPresentationNetworkSource:
    """Provide Presentation Network source."""
    return study.WordStudyPresentationNetworkSource(
        _presentation_api=mock_api_client,
    )
