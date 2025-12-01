"""Word study Presentation test."""

from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import params as fixtures
from wse.api.foreign.presentation import WordPresentationApi
from wse.core.http import HttpClientABC
from wse.data.schemas import foreign as schemas

from . import cases

# Request/Response data fixtures
# ------------------------------


@pytest.fixture
def request_payload() -> schemas.RequestPresentation:
    """Provide request payload via Presentation params."""
    return schemas.RequestPresentation(
        **fixtures.PRESENTATION_REQUEST_PAYLOAD  # type: ignore[arg-type]
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


# Api client fixture with mocked dependencies
# -------------------------------------------


@pytest.fixture
def api_deps_mock(
    mock_http_client: Mock,
    mock_auth_schema: Mock,
    mock_api_config: Mock,
) -> WordPresentationApi:
    """Provide api client with mocked dependency."""
    mock_api_config.word_presentation = 'url_path'
    return WordPresentationApi(
        _http_client=mock_http_client,
        _auth_scheme=mock_auth_schema,
        _api_config=mock_api_config,
    )


class TestResponse:
    """Test Presentation case."""

    def test_presentation_case_validation(
        self,
        request_payload: schemas.RequestPresentation,
        api_deps_mock: WordPresentationApi,
    ) -> None:
        """Test the Presentation case response validation."""
        # Act & Assert
        # Response payload success validated via `pydantic` schema
        assert api_deps_mock.fetch(request_payload)
