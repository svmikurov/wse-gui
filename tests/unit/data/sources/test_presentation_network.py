"""Word study Presentation Network sources."""

from unittest.mock import Mock

from injector import Injector

from wse.data.dto import foreign as dto
from wse.data.schemas import foreign as schemas
from wse.data.sources.di_module import SourceModule
from wse.data.sources.foreign import study


class TestLocaleSource:
    """Word study Presentation Locale sources."""

    def test_set_case(
        self,
        presentation_schema: schemas.PresentationCase,
    ) -> None:
        """Test the set Presentation case into locale source."""
        # Arrange
        injector = Injector(SourceModule())
        locale_source = injector.get(study.WordPresentationLocaleSource)

        # Act
        locale_source.set_case(presentation_schema)

        # Assert
        presentation_uuid = locale_source.get_case_uuid()
        assert presentation_uuid == presentation_schema.case_uuid

        presentation_case = locale_source.get_presentation_data()
        assert presentation_case.definition == presentation_schema.definition
        assert presentation_case.explanation == presentation_schema.explanation
        assert presentation_case.info == presentation_schema.info


class TestNetworkSource:
    """Word study Presentation Network sources."""

    def test_fetch_presentation_case(
        self,
        presentation_schema: schemas.PresentationCase,
        mock_api_client: Mock,
        initial_parameters_dto: dto.InitialParameters,
        network_source: study.WordPresentationNetworkSource,
        presentation_request_schema: schemas.RequestPresentation,
    ) -> None:
        """Test the fetch presentation case."""
        # Act
        presentation_case = network_source.fetch_presentation(
            initial_parameters_dto
        )

        # Assert
        assert presentation_case == presentation_schema
        mock_api_client.fetch.assert_called_once_with(
            presentation_request_schema
        )
