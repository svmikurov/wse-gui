"""Word study Presentation params Network source tests."""

from unittest.mock import Mock

import pytest

from wse.api.foreign import WordParamsApiABC, requests, schemas
from wse.api.schemas import base as base_schemas
from wse.data.sources.foreign.params import WordParamsNetworkSource


@pytest.fixture
def response_schema() -> schemas.PresentationParams:
    """Provide Word study Presentation params schema from Response."""
    return schemas.PresentationParams(
        categories=[
            base_schemas.IdNameSchema(id=1, name='category 1'),
            base_schemas.IdNameSchema(id=2, name='category 2'),
        ],
        labels=[
            base_schemas.IdNameSchema(id=1, name='label 1'),
            base_schemas.IdNameSchema(id=2, name='label 2'),
        ],
        category=base_schemas.IdNameSchema(id=1, name='category 1'),
        label=base_schemas.IdNameSchema(id=2, name='label 2'),
        question_timeout=1.5,
        answer_timeout=1.5,
    )


@pytest.fixture
def expected_data() -> requests.PresentationParamsDTO:
    """Provide Word study Presentation params."""
    return requests.PresentationParamsDTO(
        categories=[
            requests.IdName(id=1, name='category 1'),
            requests.IdName(id=2, name='category 2'),
        ],
        labels=[
            requests.IdName(id=1, name='label 1'),
            requests.IdName(id=2, name='label 2'),
        ],
        category=requests.IdName(id=1, name='category 1'),
        label=requests.IdName(id=2, name='label 2'),
        question_timeout=1.5,
        answer_timeout=1.5,
    )


@pytest.fixture
def mock_api_client() -> Mock:
    """Mock Word study Presentation params api client."""
    return Mock(spec=WordParamsApiABC)


@pytest.fixture
def source(
    mock_api_client: Mock,
    response_schema: schemas.PresentationParams,
) -> WordParamsNetworkSource:
    """Provide Word study Presentation params Network source."""
    mock_api_client.fetch_initial_params.return_value = response_schema
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
        data = source.fetch_initial_params()

        # Assert
        assert data == expected_data
