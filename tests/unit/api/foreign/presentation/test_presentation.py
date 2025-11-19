"""Word study Presentation test."""

from unittest.mock import Mock

import pytest

from wse.api.foreign import schemas
from wse.api.foreign.study import WordStudyPresentationApi
from wse.config.api import APIConfigV1
from wse.core.http import AuthSchemaABC, HttpClientABC

from . import cases

# Request/Response data fixtures
# ------------------------------


@pytest.fixture
def request_payload() -> schemas.PresentationParams:
    """Provide request payload via Presentation params."""
    return schemas.PresentationParams(
        category=None,
        label=None,
    )


@pytest.fixture
def response_payload() -> cases.ResponseDict:
    """Provide Presentation case response fixture."""
    return cases.VALID_RESPONSE_PAYLOAD


# Mock api client dependency fixtures
# -----------------------------------


@pytest.fixture
def mock_http_client(
    response_payload: cases.ResponseDict,
) -> Mock:
    """Mock http client."""
    mock_client = Mock(spec=HttpClientABC)

    # Mock `json()` method return data
    payload = Mock()
    payload.json.return_value = response_payload

    # Mock `post()` method return response
    mock_client.post.return_value = payload
    return mock_client


@pytest.fixture
def mock_auth_scheme() -> Mock:
    """Mock Authentication scheme."""
    mock = Mock(spec=AuthSchemaABC)
    return mock


@pytest.fixture
def mock_api_config() -> Mock:
    """Mock Authentication scheme."""
    mock = Mock(spec=APIConfigV1)
    mock.word_presentation = 'url_path'
    return mock


# Api client fixture with mocked dependencies
# -------------------------------------------


@pytest.fixture
def api_deps_mock(
    mock_http_client: Mock,
    mock_auth_scheme: Mock,
    mock_api_config: Mock,
) -> WordStudyPresentationApi:
    """Provide api client with mocked dependency."""
    return WordStudyPresentationApi(
        http_client=mock_http_client,
        auth_scheme=mock_auth_scheme,
        api_config=mock_api_config,
    )


class TestResponse:
    """Test Presentation case."""

    def test_presentation_case_validation(
        self,
        request_payload: schemas.PresentationParams,
        api_deps_mock: WordStudyPresentationApi,
    ) -> None:
        """Test the Presentation case response validation."""
        # Act & Assert
        # Response payload success validated via `pydantic` schema
        assert api_deps_mock.fetch_presentation(request_payload)
