"""Word study Presentation params Network source tests."""

from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import parameters
from wse.api.foreign import WordParamsApiABC, requests, schemas
from wse.data.sources.foreign.params import WordParamsNetworkSource


@pytest.fixture
def api_schema() -> schemas.PresentationParams:
    """Provide Word study Presentation params schema from API."""
    return parameters.PRESENTATION_PARAMETERS_SCHEMA


@pytest.fixture
def expected_data() -> requests.PresentationParamsDTO:
    """Provide Word study Presentation params."""
    return parameters.PRESENTATION_PARAMETERS_DTO


@pytest.fixture
def mock_api_client(
    api_schema: schemas.PresentationParams,
) -> Mock:
    """Mock Word study Presentation params api client."""
    mock = Mock(spec=WordParamsApiABC)
    mock.fetch_params.return_value = api_schema
    return mock


@pytest.fixture
def source(
    mock_api_client: Mock,
) -> WordParamsNetworkSource:
    """Provide Word study Presentation params Network source."""
    return WordParamsNetworkSource(
        _api_client=mock_api_client,
    )


class TestConvertSchema:
    """Presentation params schema to DTO convert test."""

    def test_correct_convert(
        self,
        source: WordParamsNetworkSource,
        expected_data: requests.PresentationParamsDTO,
    ) -> None:
        """Test the correct convert schema to DTO."""
        # Act
        data = source.fetch_params()

        # Assert
        assert data == expected_data
