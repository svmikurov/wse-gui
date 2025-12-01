"""Word study parameters API client tests."""

from unittest.mock import Mock

import pytest

from wse.api.foreign.params import WordParamsApi


@pytest.fixture
def api_client(
    mock_http_client: Mock,
    mock_auth_schema: Mock,
    mock_api_config: Mock,
) -> WordParamsApi:
    """Provide Word study parameters API client."""
    return WordParamsApi(
        _http_client=mock_http_client,
        _auth_scheme=mock_auth_schema,
        _api_config=mock_api_config,
    )
