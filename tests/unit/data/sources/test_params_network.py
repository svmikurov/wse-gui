"""Word study Presentation params Network source tests."""

from unittest.mock import Mock

import pytest

from tests.fixtures.foreign import parameters as fixtures
from wse.api.foreign import WordParametersApiABC
from wse.data.dto import foreign as dto
from wse.data.schemas import foreign
from wse.data.sources.foreign.params import WordParametersNetworkSource


@pytest.fixture
def api_schema() -> foreign.PresentationParameters:
    """Provide Word study Presentation params schema from API."""
    return fixtures.PARAMETERS_SCHEMA


@pytest.fixture(scope='session')
def expected_data() -> dto.PresentationParameters:
    """Provide Word study Presentation params."""
    return fixtures.PARAMETERS_DTO


@pytest.fixture
def mock_api_client(
    api_schema: foreign.PresentationParameters,
) -> Mock:
    """Mock Word study Presentation params api client."""
    mock = Mock(spec=WordParametersApiABC)
    mock.fetch.return_value = api_schema
    return mock


@pytest.fixture
def source(
    mock_api_client: Mock,
) -> WordParametersNetworkSource:
    """Provide Word study Presentation params Network source."""
    return WordParametersNetworkSource(
        _api_client=mock_api_client,
    )


class TestConvertSchema:
    """Presentation params schema to DTO convert test."""

    def test_correct_convert(
        self,
        source: WordParametersNetworkSource,
        expected_data: dto.PresentationParameters,
    ) -> None:
        """Test the correct convert schema to DTO."""
        # Act
        data = source.fetch()

        # Assert
        assert data == expected_data
