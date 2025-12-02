"""Word study Presentation repository tests."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any
from unittest.mock import Mock

if TYPE_CHECKING:
    from wse.data import repos
    from wse.data.dto import foreign as dto
    from wse.data.schemas import foreign as schemas


class TestWordPresentationRepo:
    """Word study Presentation repository tests."""

    def test_get_word(
        self,
        mock_http_client: Mock,
        word_params_repo: repos.WordParametersRepo,
        presentation_repo: repos.WordPresentationRepo,
        presentation_schema: schemas.Presentation,
        parameters_dto: dto.InitialParameters,
        presentation_request_payload: dict[str, Any],
    ) -> None:
        """Test the get word for presentation."""
        # Arrange
        # - Set Word study parameters
        word_params_repo.set(parameters_dto)

        # Act
        # - Get presentation data to display
        schema = presentation_repo.get_word()

        # TODO: Fix request payload, delete unnecessary fields

        # Assert
        # - That the HTTP request being sent has the correct payload
        _, kwargs = mock_http_client.post.call_args
        assert kwargs['json'] == presentation_request_payload

        # - That got the expected data to display
        assert schema == presentation_schema
