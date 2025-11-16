"""Word study Presentation Network sources."""

from unittest.mock import Mock

import pytest
from injector import Injector

from tests.unit.api.foreign.presentation import cases
from wse.api.foreign import WordStudyPresentationApiABC
from wse.data.sources.di_module import SourceModule
from wse.data.sources.foreign import schemas, study

# Data fixtures
# -------------


@pytest.fixture
def params() -> schemas.PresentationParams:
    """Provide Presentation params."""
    return schemas.PresentationParams(
        category=None,
        label=None,
    )


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


class TestLocaleSource:
    """Word study Presentation Locale sources."""

    def test_set_case(
        self,
        presentation_data: schemas.PresentationCase,
    ) -> None:
        """Test the set Presentation case into locale source."""
        # Arrange
        injector = Injector(SourceModule())
        locale_source = injector.get(study.WordStudyLocaleSource)

        # Act
        locale_source.set_case(presentation_data)

        # Assert
        presentation_uuid = locale_source.get_case_uuid()
        assert presentation_uuid == presentation_data.case_uuid

        presentation_case = locale_source.get_presentation_data()
        assert presentation_case.definition == presentation_data.definition
        assert presentation_case.explanation == presentation_data.explanation
        assert presentation_case.info == presentation_data.info


class TestNetworkSource:
    """Word study Presentation Network sources."""

    def test_fetch_presentation_case(
        self,
        params: schemas.PresentationParams,
        presentation_data: schemas.PresentationCase,
        mock_api_client: Mock,
        network_source: study.WordStudyPresentationNetworkSource,
    ) -> None:
        """Test the fetch presentation case."""
        # Act
        presentation_case = network_source.fetch_presentation(params)

        # Assert
        assert presentation_case == presentation_data
        mock_api_client.fetch_presentation.assert_called_once_with(params)
