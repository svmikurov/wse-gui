"""Word study Presentation Network sources."""

from unittest.mock import Mock

from injector import Injector

from wse.api.foreign import schemas
from wse.data.sources.di_module import SourceModule
from wse.data.sources.foreign import study


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
        presentation_params: schemas.PresentationParams,
        presentation_data: schemas.PresentationCase,
        mock_api_client: Mock,
        network_source: study.WordStudyPresentationNetworkSource,
    ) -> None:
        """Test the fetch presentation case."""
        # Act
        presentation_case = network_source.fetch_presentation(
            presentation_params
        )

        # Assert
        assert presentation_case == presentation_data
        mock_api_client.fetch_presentation.assert_called_once_with(
            presentation_params
        )
