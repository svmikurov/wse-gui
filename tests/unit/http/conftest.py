"""Http test configuration."""

from typing import Any
from unittest.mock import Mock, create_autospec

import httpx
import pytest

from wse.config.api import APIConfigV1
from wse.core.http import AuthSchemaABC, client


@pytest.fixture
def mock_http_client() -> Mock:
    """Mock HTTP client fixture."""
    return create_autospec(httpx.Client)  # type: ignore[no-any-return]


@pytest.fixture
def api_config() -> Mock:
    """Mock API config fixture."""
    mock_config = Mock(spec=APIConfigV1)
    mock_config.base_url = 'https://api.example.com'
    return mock_config


@pytest.fixture
def http_client_di_mock(
    mock_http_client: Mock,
    api_config: Mock,
) -> client.HttpClient:
    """HTTP client with mocked dependencies."""
    return client.HttpClient(mock_http_client, api_config)


@pytest.fixture
def mock_auth() -> Mock:
    """Mock Auth."""
    return create_autospec(AuthSchemaABC)  # type: ignore[no-any-return]


@pytest.fixture
def example_json() -> dict[str, Any]:
    """Get example json data."""
    return {'key': 'value'}
