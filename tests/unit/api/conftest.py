"""API client test configuration."""

from unittest.mock import Mock

import pytest

from wse.config.api import APIConfigV1
from wse.core.http import AuthSchemaABC, HttpClientABC


@pytest.fixture
def mock_http_client() -> Mock:
    """Mock http client."""
    return Mock(spec=HttpClientABC)


@pytest.fixture
def mock_auth_schema() -> Mock:
    """Mock Authentication schema."""
    return Mock(spec=AuthSchemaABC)


@pytest.fixture
def mock_api_config() -> Mock:
    """Mock API config."""
    return Mock(spec=APIConfigV1)
